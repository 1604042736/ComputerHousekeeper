import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import re
import bs4
import urllib.parse
import urllib.request
import time
import os

try:
    from __pyqt__.GetVirus import *
except ImportError:
    from AntiVirus.__pyqt__.GetVirus import *


class GetVirusUi(QWidget, Ui_GetVirus):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.getvirus = GetVirus(self)
        self.getvirus.processBar_update.connect(self.update_processBar)
        self.getvirus.processBar2_update.connect(self.update_processBar2)
        self.getvirus.textEdit_output_update.connect(self.write)
        self.pushButton_start.clicked.connect(self.start)

        if (os.path.exists('.computerhousekeeper\\img\\getvirus.jpg')):
            self.setWindowIcon(QIcon('.computerhousekeeper\\img\\getvirus.jpg'))
        else:
            self.setWindowIcon(QIcon('..\\.computerhousekeeper\\img\\getvirus.jpg'))

    def start(self):
        self.getvirus.start()

    def resizeEvent(self, a0: QtGui.QResizeEvent):
        self.progressBar.resize(self.width() - self.pushButton_start.width(), self.progressBar.height())
        self.progressBar2.resize(self.width() - self.pushButton_start.width(), self.progressBar2.height())
        self.textEdit_output.resize(self.width(), self.height() - self.pushButton_start.height())

    def write(self, text):
        self.textEdit_output.append(text)

    def update_processBar(self, process):
        self.progressBar.setValue(process)

    def update_processBar2(self, process):
        self.progressBar2.setValue(process)


class GetVirus(QThread):
    processBar_update = pyqtSignal(int)
    processBar2_update = pyqtSignal(int)
    textEdit_output_update = pyqtSignal(str)

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.virusliburl = 'https://www.virscan.org/reportlist'
        self.reponse = urllib.request.Request(self.virusliburl)
        self.html = urllib.request.urlopen(self.reponse).read().decode("utf-8")
        # 解析html
        self.soup = bs4.BeautifulSoup(self.html, 'html.parser')
        self.maxpage, self.pageurls = self.GetMaxPage()

    def run(self):
        # self.parent.textEdit_output.setText('')
        self.Get()

    def Get(self):
        if (os.path.exists('VirusInfomation.log')):
            file = open('VirusInfomation.log', 'w')
        else:
            file = open('AntiVirus\\VirusInfomation.log', 'w')
        file.write('')
        file.close()
        self.parent.progressBar.setMaximum(self.maxpage)
        process = 1
        for url in self.pageurls:
            self.processBar_update.emit(process)
            try:
                self.GetReport(url)
            except Exception as e:
                print(e)
            process += 1
        self.processBar_update.emit(0)

    def GetMaxPage(self):
        pattern = r'/reportlist/\w+'
        liResult = self.soup.find_all('a', href=re.compile(pattern))

        # 找到页面最大值
        maxPage = 1
        for link in liResult:
            url2 = link['href']
            page = url2.split('/')[-1]
            if maxPage < int(page):
                maxPage = int(page)

        return maxPage, [self.virusliburl + '/%d' % (x) for x in range(1, maxPage + 1)]

    def GetReport(self, url):
        reponse = urllib.request.Request(url)
        html = urllib.request.urlopen(reponse).read().decode("utf-8")
        # 解析html
        soup = bs4.BeautifulSoup(html, 'html.parser')

        # 查找首页所有a链接，匹配想要的URL格式（v.xxx内容）
        pattern = r'https://v.virscan.org/'  # URL格式
        vLinks = soup.find_all('a', href=re.compile(pattern))
        self.parent.progressBar2.setMaximum(len(vLinks))
        process = 1
        for vlink in vLinks:
            self.processBar2_update.emit(process)
            time.sleep(1)
            url3 = urllib.parse.quote(vlink['href'])
            url3 = url3.replace('https%3A', 'https:')

            if vlink.has_attr('alt'):
                vn = vlink['alt']
            else:
                vn = ''
            if vn == '':
                vn = url3.split('/')[-1][0:-5]
                vn = urllib.parse.unquote(vn)
            print(url3)
            self.GetVirusReport(url3)
            process += 1
        self.processBar2_update.emit(0)

    def GetVirusReport(self, url):
        reponse = urllib.request.Request(url)
        html = urllib.request.urlopen(reponse).read().decode("utf-8", errors='ignore')
        # 解析html
        soup = bs4.BeautifulSoup(html, 'html.parser')

        basepageurl = urllib.parse.unquote(url[:-5]) + '/'

        # 获取详解界面
        pattern = 'https://v.virscan.org/'
        VInfoLinks = soup.find_all('a', href=re.compile(pattern))
        # 这里是找到页面最大值，然后for循环访问
        maxpagenum = 1
        for link in VInfoLinks:
            url4 = link['href']
            numstr = url4.split('/')[-1][0:-5]
            try:
                if maxpagenum < int(numstr):
                    maxpagenum = int(numstr)

            except:
                continue
        for i in range(1, maxpagenum + 1):
            time.sleep(1)
            url5 = urllib.parse.quote(basepageurl + str(i) + '.html')
            url5 = url5.replace('https%3A', 'https:')
            self.GetVirusPage(url5)

    def GetVirusPage(self, url):
        # print('--------getAndroidVirusPage-->'+myurl)
        reponse = urllib.request.Request(url)
        html = urllib.request.urlopen(reponse).read().decode("utf-8", errors='ignore')
        # 解析html
        soup = bs4.BeautifulSoup(html, 'html.parser')
        # 拿到md5值
        pattern = r'https://md5.virscan.org/\w+'  # URL格式
        md5Links = soup.find_all('a', href=re.compile(pattern))
        for link in md5Links:
            url6 = link['href']
            md5str = url6.split('/')[-1][0:-5]
            print("get file md5 :" + md5str)
            self.textEdit_output_update.emit("get file md5 :" + md5str)
            if (os.path.exists('VirusInfomation.log')):
                file = open('VirusInfomation.log', 'a')
            else:
                file = open('AntiVirus\\VirusInfomation.log', 'a')
            file.write(md5str + '\n')
            file.close()


if (__name__ == '__main__'):
    app = QApplication(sys.argv)
    getvirusui = GetVirusUi()
    getvirusui.show()
    app.exec_()

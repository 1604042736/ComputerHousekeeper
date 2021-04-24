import sys
import os
import requests
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

try:
    from __pyqt__.Downloader import *
except:
    from Downloader.__pyqt__.Downloader import *


class Downloader(QWidget, Ui_Downloader):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_choose.clicked.connect(self.choosefile)
        self.pushButton_start.clicked.connect(self.sartdownload)

        if (os.path.exists('.computerhousekeeper\\img\\downloader.jpg')):
            self.setWindowIcon(QIcon('.computerhousekeeper\\img\\downloader.jpg'))
        else:
            self.setWindowIcon(QIcon('..\\.computerhousekeeper\\img\\downloader.jpg'))

    def sartdownload(self):
        item = QListWidgetItem()
        item.setSizeHint(QSize(32, 64))
        widget = DownloadItemWidget(self.lineEdit_url.text(),
                                    self.lineEdit_path.text() + '/' + self.lineEdit_url.text().split('/')[-1])
        widget.resize(32, 64)
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, widget)

    def choosefile(self):
        dir_choose = QFileDialog.getExistingDirectory(self, "选取文件夹", os.getcwd())
        if (dir_choose != ''):
            self.lineEdit_path.setText(dir_choose)

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        self.listWidget.resize(self.width(), self.height() - self.lineEdit_path.height() - self.lineEdit_url.height())


class DownloadItemWidget(QWidget):
    def __init__(self, url, path):
        super().__init__()

        self.label_message = QLabel(self)
        self.label_message.setText(f'{url} 下载到 {path}')
        self.label_message.resize(self.width(), 32)
        self.label_message.move(0, 0)

        self.progressBar = QProgressBar(self)
        self.progressBar.setMaximum(0)
        self.progressBar.move(0, 32)
        self.progressBar.resize(self.width(), 32)

        self.url = url
        self.path = path
        self.download()

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        self.label_message.resize(self.width(), self.label_message.height())
        self.progressBar.resize(self.width(), self.progressBar.height())

    def updata_process(self, process):
        self.progressBar.setValue(process)

    def download(self):
        self.progressBar.setMaximum(100)
        self.downloadthread = Download(self.url, self.path)
        self.downloadthread.process_updata.connect(self.updata_process)
        self.downloadthread.start()


class Download(QThread):
    process_updata = pyqtSignal(int)

    def __init__(self, url, path):
        super().__init__()

        self.url, self.path = url, path
        self.fileobj = open(self.path, 'wb')

    def run(self):
        try:
            rsp = requests.get(self.url, stream=True)
            offset = 0
            for chunk in rsp.iter_content(chunk_size=10240):
                if not chunk:
                    break
                self.fileobj.seek(offset)  # 设置指针位置
                self.fileobj.write(chunk)  # 写入文件
                offset = offset + len(chunk)
                proess = offset / int(rsp.headers['Content-Length']) * 100
                self.process_updata.emit(int(proess))
            self.fileobj.close()
        except Exception as e:
            print(e)


if (__name__ == '__main__'):
    app = QApplication(sys.argv)
    downloader = Downloader()
    downloader.show()
    app.exec_()

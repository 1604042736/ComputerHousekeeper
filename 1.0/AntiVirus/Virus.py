import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from pathlib import *

import os

try:
    from __pyqt__.Virus import *
    from GetVirus import *
    from GetMd5 import *
except:
    from AntiVirus.__pyqt__.Virus import *
    from AntiVirus.GetVirus import *
    from AntiVirus.GetMd5 import *


class Virus(QWidget, Ui_Virus):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.anti = Anti(self)
        self.anti.processBar_update.connect(self.update_processBar)
        self.pushButton_start.clicked.connect(self.on_pushButton_start_clicked)
        self.pushButton_choose.clicked.connect(self.choosefile)

        if (os.path.exists('.computerhousekeeper\\img\\virus.jpg')):
            self.setWindowIcon(QIcon('.computerhousekeeper\\img\\virus.jpg'))
        else:
            self.setWindowIcon(QIcon('..\\.computerhousekeeper\\img\\virus.jpg'))

    def on_pushButton_start_clicked(self):
        self.pushButton_start.setEnabled(False)
        self.anti.start()

    def update_processBar(self, process):
        self.progressBar.setValue(process)

    def choosefile(self):
        dir_choose = QFileDialog.getExistingDirectory(self, "选取文件夹", os.getcwd())
        if (dir_choose != ''):
            self.lineEdit_way.setText(dir_choose)

    def resizeEvent(self, a0: QtGui.QResizeEvent):
        self.label_filepath.resize(self.width() - self.pushButton_start.width(), self.label_filepath.height())
        self.progressBar.resize(self.width() - self.pushButton_start.width(), self.progressBar.height())
        self.listWidget_program.resize(self.width(), self.height() - self.pushButton_start.height())
        self.lineEdit_way.resize(self.width() - self.pushButton_choose.width(), self.lineEdit_way.height())
        self.pushButton_choose.move(self.width() - self.pushButton_choose.width(), self.pushButton_choose.y())


class Anti(QThread):
    processBar_update = pyqtSignal(int)

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.progress = 0
        self.filenumber = 0

    def run(self):
        self.parent.listWidget_program.clear()
        self.parent.label_filepath.setText('正在获取病毒信息')
        # GetVirus().Get()
        self.virusinfo = []
        try:
            with open('VirusInfomation.log')as file:
                for line in file.readlines():
                    self.virusinfo.append(line[:-1])
        except FileNotFoundError:
            with open('AntiVirus\\VirusInfomation.log')as file:
                for line in file.readlines():
                    self.virusinfo.append(line[:-1])
        print(self.virusinfo)
        self.parent.label_filepath.setText('正在获取文件数量')
        self.anti(self.parent.lineEdit_way.text())
        self.progress = 0
        self.processBar_update.emit(0)
        self.parent.pushButton_start.setEnabled(True)
        self.parent.label_filepath.setText('')

    def anti(self, path):
        p = Path(self.parent.lineEdit_way.text())
        filenumber = list(p.glob('**/*.exe'))
        print(filenumber)
        self.parent.progressBar.setMaximum(len(filenumber))
        for filepath in filenumber:
            try:
                self.parent.label_filepath.setText('正在扫描' + str(filepath))
                md5 = GetFileMd5(str(filepath))
                if (md5 in self.virusinfo):
                    self.parent.listWidget_program.addItem(str(filepath))
                self.processBar_update.emit(self.progress)
                self.progress += 1
            except Exception as e:
                print(e)


if (__name__ == '__main__'):
    app = QApplication(sys.argv)
    virus = Virus()
    virus.show()
    app.exec_()

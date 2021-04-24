import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os
from pathlib import *

try:
    from __pyqt__.GarbageCleaning import *
except:
    from GarbageCleaning.__pyqt__.GarbageCleaning import *


class GarbageCleaning(QWidget, Ui_GarbageCleaning):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.clean = Clean(self)
        self.pushButton_choose.clicked.connect(self.choosefile)
        self.pushButton_start.clicked.connect(self.startclean)
        self.pushButton_del.clicked.connect(self.cleaning)

        if (os.path.exists('.computerhousekeeper\\img\\garbagecleaning.jpg')):
            self.setWindowIcon(QIcon('.computerhousekeeper\\img\\garbagecleaning.jpg'))
        else:
            self.setWindowIcon(QIcon('..\\.computerhousekeeper\\img\\garbagecleaning.jpg'))

    def cleaning(self):
        for item in range(self.listWidget_result.count()):
            try:
                print(self.listWidget_result.item(item).text())
                os.remove(self.listWidget_result.item(item).text())
            except Exception as e:
                print(e)

    def choosefile(self):
        dir_choose = QFileDialog.getExistingDirectory(self, "选取文件夹", os.getcwd())
        if (dir_choose != ''):
            self.lineEdit_path.setText(dir_choose)

    def startclean(self):
        self.pushButton_start.setEnabled(False)
        self.clean.start()

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        self.pushButton_del.move(self.width() - self.pushButton_del.width(), self.pushButton_del.y())
        self.pushButton_start.move(self.width() - self.pushButton_del.width() - self.pushButton_start.width(),
                                   self.pushButton_start.y())
        self.pushButton_choose.move(
            self.width() - self.pushButton_del.width() - self.pushButton_start.width() - self.pushButton_choose.width(),
            self.pushButton_choose.y())
        self.lineEdit_path.resize(
            self.width() - self.pushButton_del.width() - self.pushButton_start.width() - self.pushButton_choose.width(),
            self.lineEdit_path.height())
        self.listWidget_result.resize(self.width(), self.height() - self.lineEdit_path.height())


class Clean(QThread):
    filetype = ['tmp', '_mp', 'log', 'gid', 'chk', 'old', 'bak']

    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def run(self):
        self.parent.listWidget_result.clear()
        self.search(self.parent.lineEdit_path.text())
        self.parent.pushButton_start.setEnabled(True)

    def search(self, path):
        try:
            for filename in os.listdir(path):
                filepath = os.path.join(path, filename)
                print(filepath)
                if (os.path.isdir(filepath)):
                    self.search(filepath)
                elif (filename.split('.')[-1] in self.filetype):
                    self.parent.listWidget_result.addItem(filepath)
        except Exception as e:
            print(e)


if (__name__ == '__main__'):
    app = QApplication(sys.argv)
    cleaning = GarbageCleaning()
    cleaning.show()
    app.exec_()

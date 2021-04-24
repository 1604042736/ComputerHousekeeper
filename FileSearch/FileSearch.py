import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os

try:
    from __pyqt__.FileSearch import *
except:
    from FileSearch.__pyqt__.FileSearch import *


class FileSearch(QWidget, Ui_FileSearch):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.searchfile = SearchFile(self)
        self.pushButton_start.clicked.connect(self.startsearchfile)
        self.pushButton_choose.clicked.connect(self.choosefile)
        self.listWidget_result.customContextMenuRequested.connect(self.listWidget_result_showrightmenu)

        if (os.path.exists('.computerhousekeeper\\img\\filesearch.jpg')):
            self.setWindowIcon(QIcon('.computerhousekeeper\\img\\filesearch.jpg'))
        else:
            self.setWindowIcon(QIcon('..\\.computerhousekeeper\\img\\filesearch.jpg'))

    def startsearchfile(self):
        self.pushButton_start.setEnabled(False)
        self.searchfile.start()

    def choosefile(self):
        dir_choose = QFileDialog.getExistingDirectory(self, "选取文件夹", os.getcwd())
        if (dir_choose != ''):
            self.lineEdit_path.setText(dir_choose)

    def listWidget_result_showrightmenu(self):
        menu = QMenu(self.listWidget_result)
        action = menu.addAction("打开文件夹")
        action.triggered.connect(self.openfoder)
        menu.exec_(QCursor.pos())

    def openfoder(self):
        print(os.path.dirname(self.listWidget_result.currentItem().text()))
        os.startfile(os.path.dirname(self.listWidget_result.currentItem().text()))

    def resizeEvent(self, QResizeEvent):
        self.lineEdit_path.resize(int(self.width() / 2), self.lineEdit_path.height())
        self.pushButton_choose.move(self.width() - self.lineEdit_path.width(), self.pushButton_choose.y())
        self.pushButton_start.move(self.width() - self.pushButton_start.width(), self.pushButton_start.y())
        self.lineEdit_key.resize(
            self.width() - self.lineEdit_path.width() - self.pushButton_start.width() - self.pushButton_choose.width(),
            self.lineEdit_key.height())
        self.lineEdit_key.move(self.lineEdit_path.width() + self.pushButton_choose.width(), self.lineEdit_key.y())
        self.listWidget_result.resize(self.width(), self.height() - self.lineEdit_path.height())


class SearchFile(QThread):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def run(self):
        self.parent.listWidget_result.clear()
        self.keyword = self.parent.lineEdit_key.text()
        self.search(self.parent.lineEdit_path.text())
        self.parent.pushButton_start.setEnabled(True)

    def search(self, path):
        try:
            for filename in os.listdir(path):
                filepath = os.path.join(path, filename)
                print(filepath)
                if (self.keyword in filename):
                    self.parent.listWidget_result.addItem(filepath)
                if (os.path.isdir(filepath)):
                    self.search(filepath)
        except Exception as e:
            print(e)


if (__name__ == '__main__'):
    app = QApplication(sys.argv)
    filesearch = FileSearch()
    filesearch.show()
    app.exec_()

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import winreg  as wr
import os

try:
    from __pyqt__.StartItem import *
except:
    from TaskManager.__pyqt__.StartItem import *


class StartItem(QWidget, Ui_StartItem):
    NAME, PATH = range(2)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.model = QStandardItemModel(0, 2, self)
        self.model.setHeaderData(self.NAME, Qt.Horizontal, "name")
        self.model.setHeaderData(self.PATH, Qt.Horizontal, "path")
        self.treeView.setModel(self.model)

        self.update_treeView()

        if (os.path.exists('.computerhousekeeper\\img\\startitem.jpg')):
            self.setWindowIcon(QIcon('.computerhousekeeper\\img\\startitem.jpg'))
        else:
            self.setWindowIcon(QIcon('..\\.computerhousekeeper\\img\\startitem.jpg'))

    def resizeEvent(self, QResizeEvent):
        self.treeView.resize(self.width(), self.height())

    def update_treeView(self):
        self.model = QStandardItemModel(0, 2, self)
        self.model.setHeaderData(self.NAME, Qt.Horizontal, "name")
        self.model.setHeaderData(self.PATH, Qt.Horizontal, "path")
        self.treeView.setModel(self.model)

        autorun = self.getAutoRun()
        print(autorun)
        for key in autorun:
            self.model.insertRow(0)
            self.model.setData(self.model.index(0, self.NAME), key)
            self.model.setData(self.model.index(0, self.PATH), autorun[key])

    def getAutoRun(self):
        root1 = wr.ConnectRegistry(None, wr.HKEY_LOCAL_MACHINE)  # 获取LocalMachine Key
        root2 = wr.ConnectRegistry(None, wr.HKEY_CURRENT_USER)
        result = {}
        try:
            targ = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
            print("****reading from ", targ, "****")
            key1 = wr.OpenKey(root1, targ)  # 打开localmachine的autorun列表
            key2 = wr.OpenKey(root2, targ)  # 打开currentuser的autorun列表
            cnt = 0
            try:
                for i in range(1024):
                    try:
                        n, v, t = wr.EnumValue(key1, i)  # 迭代localmachine
                        result[n] = v
                        cnt += 1
                    except EnvironmentError:
                        break
                for i in range(1024):
                    try:
                        n, v, t = wr.EnumValue(key2, i)  # 迭代currentuser
                        result[n] = v
                        cnt += 1
                    except EnvironmentError:
                        break
            finally:
                wr.CloseKey(key1)
                wr.CloseKey(key2)
        finally:
            wr.CloseKey(root1)
            wr.CloseKey(root2)
        return result


if (__name__ == '__main__'):
    app = QApplication(sys.argv)
    startitem = StartItem()
    startitem.show()
    app.exec_()

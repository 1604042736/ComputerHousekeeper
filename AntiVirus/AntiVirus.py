import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os

try:
    from __pyqt__.AntiVirus import *
    from Virus import *
    from GetVirus import *
except:
    from AntiVirus.__pyqt__.AntiVirus import *
    from AntiVirus.Virus import *
    from AntiVirus.GetVirus import *


class AntiVirus(QWidget, Ui_AntiVirus):
    def __init__(self):
        self.sepwin = []
        super().__init__()
        self.setupUi(self)

        self.tabWidget.addTab(Virus(), "扫描")
        self.tabWidget.addTab(GetVirusUi(), '更新病毒库')

        self.tabWidget.customContextMenuRequested.connect(self.tabWidget_showrightmenu)

        if (os.path.exists('.computerhousekeeper\\img\\antivirus.jpg')):
            self.setWindowIcon(QIcon('.computerhousekeeper\\img\\antivirus.jpg'))
        else:
            self.setWindowIcon(QIcon('..\\.computerhousekeeper\\img\\antivirus.jpg'))

    def tabWidget_showrightmenu(self):
        menu = QMenu(self.tabWidget)
        action = menu.addAction('分离')
        action.triggered.connect(self.sep)
        menu.exec_(QCursor.pos())

    def sep(self):
        widget = [Virus, GetVirusUi]
        self.sepwin.append(widget[self.tabWidget.currentIndex()]())
        self.sepwin[-1].show()

    def resizeEvent(self, QResizeEvent):
        self.tabWidget.resize(self.width(), self.height())


if (__name__ == '__main__'):
    app = QApplication(sys.argv)
    antivirus = AntiVirus()
    antivirus.show()
    app.exec_()

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

try:
    from __pyqt__.TaskManager import *
    from Performance import *
    from Process import *
    from StartItem import *
except:
    from TaskManager.__pyqt__.TaskManager import *
    from TaskManager.Performance import *
    from TaskManager.Process import *
    from TaskManager.StartItem import *


class TaskManager(QWidget, Ui_TaskManager):
    def __init__(self):
        self.sepwin = []
        super().__init__()
        self.setupUi(self)

        self.tabWidget.addTab(Process(), "进程")
        self.tabWidget.addTab(Performance(), "性能")
        self.tabWidget.addTab(StartItem(), "启动项")
        self.tabWidget.customContextMenuRequested.connect(self.tabWidget_showrightmenu)

        if (os.path.exists('.computerhousekeeper\\img\\taskmanager.jpg')):
            self.setWindowIcon(QIcon('.computerhousekeeper\\img\\taskmanager.jpg'))
        else:
            self.setWindowIcon(QIcon('..\\.computerhousekeeper\\img\\taskmanager.jpg'))

    def tabWidget_showrightmenu(self):
        menu = QMenu(self.tabWidget)
        action = menu.addAction('分离')
        action.triggered.connect(self.sep)
        menu.exec_(QCursor.pos())

    def sep(self):
        widget = [Process, Performance, StartItem]
        self.sepwin.append(widget[self.tabWidget.currentIndex()]())
        self.sepwin[-1].show()

    def resizeEvent(self, a0: QtGui.QResizeEvent):
        self.tabWidget.resize(self.width(), self.height())


if (__name__ == '__main__'):
    app = QApplication(sys.argv)
    taskmanager = TaskManager()
    taskmanager.show()
    app.exec_()

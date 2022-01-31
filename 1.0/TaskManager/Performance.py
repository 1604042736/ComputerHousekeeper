import sys

sys.path.append("..\\")

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

try:
    from __pyqt__.Performance import *
    from CpuPercent import *
    from Memory import *
    from WLAN import *
except:
    from TaskManager.__pyqt__.Performance import *
    from TaskManager.CpuPercent import *
    from TaskManager.Memory import *
    from TaskManager.WLAN import *


class Performance(QWidget, Ui_Performance):
    def __init__(self):
        self.sepwin = []
        super().__init__()
        self.setupUi(self)

        self.listWidget_name.itemClicked.connect(self.on_listWidget_itemClicked)
        self.listWidget_name.customContextMenuRequested.connect(self.listWidget_showrightmenu)

        self.qsl = QStackedLayout(self.frame_content)
        self.qsl.addWidget(CpuPercent())
        self.qsl.addWidget(Memory())
        self.qsl.addWidget(WLAN())

        if (os.path.exists('.computerhousekeeper\\img\\performance.jpg')):
            self.setWindowIcon(QIcon('.computerhousekeeper\\img\\performance.jpg'))
        else:
            self.setWindowIcon(QIcon('..\\.computerhousekeeper\\img\\performance.jpg'))

    def on_listWidget_itemClicked(self):
        self.qsl.setCurrentIndex(self.listWidget_name.currentRow())

    def listWidget_showrightmenu(self):
        menu = QMenu(self.listWidget_name)
        action = menu.addAction('分离')
        action.triggered.connect(self.sep)
        menu.exec_(QCursor.pos())

    def sep(self):
        widget = [CpuPercent, Memory, WLAN]
        self.sepwin.append(widget[self.listWidget_name.currentRow()]())
        self.sepwin[-1].show()

    def resizeEvent(self, a0: QtGui.QResizeEvent):
        self.listWidget_name.resize(self.listWidget_name.width(), self.height())
        self.frame_content.resize(self.width() - self.listWidget_name.width(), self.height())


if (__name__ == '__main__'):
    app = QApplication(sys.argv)
    performance = Performance()
    performance.show()
    app.exec_()

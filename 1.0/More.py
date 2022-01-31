import sys
import logging
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from __pyqt__.More import *
from About import *


class More(QWidget, Ui_More):
    def __init__(self):
        self.sepwin = []
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('.computerhousekeeper\\img\\more.jpg'))

        self.about = About()

        self.qsl = QStackedLayout(self.frame_content)
        self.qsl.addWidget(self.about)

        self.pushButton_about.clicked.connect(self.show_panel)
        self.pushButton_about.customContextMenuRequested.connect(self.pushButton_about_showrightmenu)

        logging.info(f'初始化{type(self).__name__}窗口')

    def show_panel(self):
        button_objectname = {
            'pushButton_about': 0,
        }
        self.qsl.setCurrentIndex(button_objectname[self.sender().objectName()])

        logging.info(f'切换{type(self).__name__}界面')

    def pushButton_about_showrightmenu(self):
        menu = QMenu(self.pushButton_about)
        action = menu.addAction("分离")
        action.triggered.connect(self.sep)
        menu.exec_(QCursor.pos())

        logging.info(f'{type(self).__name__}.{self.sender().objectName()}按钮按下')

    def sep(self):
        win = [About]
        self.sepwin.append(win[self.qsl.currentIndex()]())
        self.sepwin[-1].show()

        logging.info(f'{type(self).__name__}分离窗口')

    def resizeEvent(self, a0: QtGui.QResizeEvent):
        self.frame_name.resize(self.frame_name.width(), self.height())
        self.frame_content.resize(self.width() - self.frame_name.width(), self.height())
        logging.info(f'{type(self).__name__}窗口大小改变')


if (__name__ == '__main__'):
    logging.basicConfig(level=logging.NOTSET,
                        filename='.computerhousekeeper\\debug.log',
                        filemode='w',
                        format='%(levelno)s %(levelname)s %(pathname)s %(filename)s %(funcName)s %(lineno)d %(asctime)s %(thread)d %(threadName)s %(process)d %(message)s')

    app = QApplication(sys.argv)
    more = More()
    more.show()
    logging.info('显示More窗口')
    app.exec_()

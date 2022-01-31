import sys
import logging
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from markdown import *

from __pyqt__.About import *


class About(QWidget, Ui_About):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('.computerhousekeeper\\img\\about.png'))
        print(markdown(open('README.md', encoding='utf-8').read()))
        self.textEdit.setHtml(markdown(open('README.md', encoding='utf-8').read()))

        logging.info(f'初始化{type(self).__name__}窗口')

    def resizeEvent(self, a0: QtGui.QResizeEvent):
        self.textEdit.resize(self.width(), self.height())


if (__name__ == '__main__'):
    logging.basicConfig(level=logging.NOTSET,
                        filename='.computerhousekeeper\\debug.log',
                        filemode='w',
                        format='%(levelno)s %(levelname)s %(pathname)s %(filename)s %(funcName)s %(lineno)d %(asctime)s %(thread)d %(threadName)s %(process)d %(message)s')

    app = QApplication(sys.argv)
    about = About()
    about.show()
    logging.info('显示About窗口')
    app.exec_()

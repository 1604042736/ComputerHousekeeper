import sys
import logging
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from __pyqt__.Task import *
from TaskManager.TaskManager import *
from AntiVirus.AntiVirus import *
from FileSearch.FileSearch import *
from GarbageCleaning.GarbageCleaning import *
from Downloader.Downloader import *
from Software.Software import *


class Task(QWidget, Ui_Task):
    def __init__(self):
        self.sepwin = []
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('.computerhousekeeper\\img\\task.jpg'))

        self.listWidget_name.itemClicked.connect(self.show_tool)
        self.listWidget_name.customContextMenuRequested.connect(self.listWidget_name_showrightmenu)

        self.qsl = QStackedLayout(self.frame_content)

        logging.info(f'初始化{type(self).__name__}窗口')

    def show_tool(self):
        self.qsl.setCurrentIndex(self.listWidget_name.currentRow())
        logging.info(f'显示{type(self).__name__}工具')

    def listWidget_name_showrightmenu(self):
        menu = QMenu(self.listWidget_name)
        action = menu.addAction("分离")
        action.triggered.connect(self.sep)
        action = menu.addAction("删除")
        action.triggered.connect(self.delete)
        menu.exec_(QCursor.pos())

        logging.info(f'{type(self).__name__}.{self.sender().objectName()}右键菜单')

    def sep(self):
        toolname = {'AntiVirus': AntiVirus,
                    'TaskManager': TaskManager,
                    'FileSearch': FileSearch,
                    'GarbageCleaning': GarbageCleaning,
                    'Software': Software,
                    'Downloader': Downloader}
        self.sepwin.append(toolname[self.listWidget_name.currentItem().text()]())
        self.sepwin[-1].show()
        logging.info(f'{type(self).__name__}分离窗口')

    def delete(self):
        self.qsl.removeWidget(self.qsl.currentWidget())
        self.listWidget_name.takeItem(self.listWidget_name.currentRow())
        logging.info(f'{type(self).__name__}删除')

    def resizeEvent(self, a0: QtGui.QResizeEvent):
        self.listWidget_name.resize(self.listWidget_name.width(), self.height())
        self.frame_content.resize(self.width() - self.listWidget_name.width(), self.height())
        logging.info(f'{type(self).__name__}大小改变')


if (__name__ == '__main__'):
    logging.basicConfig(level=logging.NOTSET,
                        filename='.computerhousekeeper\\debug.log',
                        filemode='w',
                        format='%(levelno)s %(levelname)s %(pathname)s %(filename)s %(funcName)s %(lineno)d %(asctime)s %(thread)d %(threadName)s %(process)d %(message)s')

    app = QApplication(sys.argv)
    task = Task()
    task.show()
    logging.info('显示Task窗口')
    app.exec_()

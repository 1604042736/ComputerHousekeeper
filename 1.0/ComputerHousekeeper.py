import sys
import logging
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from __pyqt__.ComputerHousekeeper import *
from Tool import *
from Task import *
from More import *
from TaskManager.TaskManager import *
from AntiVirus.AntiVirus import *
from FileSearch.FileSearch import *
from GarbageCleaning.GarbageCleaning import *
from Downloader.Downloader import *
from Software.Software import *


class ComputerHousekeeper(QMainWindow, Ui_ComputerHousekeeper):
    def __init__(self):
        self.sepwin = []
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('.computerhousekeeper\\img\\ComputerHousekeeper.jpg'))

        self.task = Task()
        self.tool = Tool()
        self.more = More()

        self.qsl = QStackedLayout(self.frame_ui)
        self.qsl.addWidget(self.task)
        self.qsl.addWidget(self.tool)
        self.qsl.addWidget(self.more)

        self.pushButton_task.clicked.connect(self.show_panel)
        self.pushButton_task.customContextMenuRequested.connect(self.pushButton_task_showrightmenu)
        self.pushButton_tool.clicked.connect(self.show_panel)
        self.pushButton_tool.customContextMenuRequested.connect(self.pushButton_tool_showrightmenu)
        self.pushButton_more.clicked.connect(self.show_panel)
        self.pushButton_more.customContextMenuRequested.connect(self.pushButton_more_showrightmenu)
        self.tool.listWidget_tool.doubleClicked.connect(self.start_tool)
        self.tool.listWidget_tool.doubleClicked.disconnect(self.tool.start_tool)

        self.pushButton_task.setIcon(QIcon('.computerhousekeeper\\img\\task.jpg'))
        self.pushButton_tool.setIcon(QIcon('.computerhousekeeper\\img\\tool.jpg'))
        self.pushButton_more.setIcon(QIcon('.computerhousekeeper\\img\\more.jpg'))

        logging.info(f'初始化{type(self).__name__}窗口')

    def show_panel(self):
        button_objectname = {
            'pushButton_task': 0,
            'pushButton_tool': 1,
            'pushButton_more': 2
        }
        self.qsl.setCurrentIndex(button_objectname[self.sender().objectName()])
        logging.info(f'切换{type(self).__name__}界面')

    def start_tool(self):
        toolname = [AntiVirus,
                    Downloader,
                    FileSearch,
                    GarbageCleaning,
                    Software,
                    TaskManager]
        self.task.listWidget_name.addItem(toolname[self.tool.listWidget_tool.currentRow()].__name__)
        self.task.qsl.addWidget(toolname[self.tool.listWidget_tool.currentRow()]())
        self.qsl.setCurrentIndex(0)
        logging.info(f'{type(self).__name__}打开工具')

    def pushButton_more_showrightmenu(self):
        menu = QMenu(self.pushButton_more)
        action = menu.addAction("分离")
        action.triggered.connect(self.sep)
        menu.exec_(QCursor.pos())
        logging.info(f'{type(self).__name__}.{self.sender().objectName()}按钮按下')

    def pushButton_task_showrightmenu(self):
        menu = QMenu(self.pushButton_task)
        action = menu.addAction("分离")
        action.triggered.connect(self.sep)
        menu.exec_(QCursor.pos())
        logging.info(f'{type(self).__name__}.{self.sender().objectName()}按钮按下')

    def pushButton_tool_showrightmenu(self):
        menu = QMenu(self.pushButton_tool)
        action = menu.addAction("分离")
        action.triggered.connect(self.sep)
        menu.exec_(QCursor.pos())
        logging.info(f'{type(self).__name__}.{self.sender().objectName()}按钮按下')

    def sep(self):
        win = [Task, Tool, More]
        tools = {'AntiVirus': AntiVirus,
                 'TaskManager': TaskManager,
                 'FileSearch': FileSearch,
                 'GarbageCleaning': GarbageCleaning,
                 'Software': Software,
                 'Downloader': Downloader}

        if (self.qsl.currentIndex() == 0):
            task = win[0]()
            for i in range(self.task.listWidget_name.count()):
                task.listWidget_name.addItem(self.task.listWidget_name.item(i).text())
                task.qsl.addWidget(tools[self.task.listWidget_name.item(i).text()]())
            self.sepwin.append(task)
        else:
            self.sepwin.append(win[self.qsl.currentIndex()]())
        self.sepwin[-1].show()
        logging.info(f'{type(self).__name__}分离窗口')

    def resizeEvent(self, a0: QtGui.QResizeEvent):
        self.frame_panel.resize(self.frame_panel.width(), self.height())
        self.frame_ui.resize(self.width() - self.frame_panel.width(), self.height())
        logging.info(f'{type(self).__name__}大小改变')


if (__name__ == '__main__'):
    logging.basicConfig(level=logging.NOTSET,
                        filename='.computerhousekeeper\\debug.log',
                        filemode='w',
                        format='%(levelno)s %(levelname)s %(pathname)s %(filename)s %(funcName)s %(lineno)d %(asctime)s %(thread)d %(threadName)s %(process)d %(message)s')
    app = QApplication(sys.argv)
    computerHousekeeper = ComputerHousekeeper()
    computerHousekeeper.show()
    logging.info('显示ComputerHousekeeper窗口')
    app.exec_()

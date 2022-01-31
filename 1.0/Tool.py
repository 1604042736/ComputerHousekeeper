import sys
import logging
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from __pyqt__.Tool import *
from TaskManager.TaskManager import *
from AntiVirus.AntiVirus import *
from FileSearch.FileSearch import *
from GarbageCleaning.GarbageCleaning import *
from Downloader.Downloader import *
from Software.Software import *


class Tool(QWidget, Ui_Tool):
    tools = {'AntiVirus': '.computerhousekeeper\\img\\antivirus.jpg',
             'Downloader': '.computerhousekeeper\\img\\downloader.jpg',
             'FileSearch': '.computerhousekeeper\\img\\filesearch.jpg',
             'GarbageCleaning': '.computerhousekeeper\\img\\garbagecleaning.jpg',
             'Software': '.computerhousekeeper\\img\\software.jpg',
             'TaskManager': '.computerhousekeeper\\img\\taskmanager.jpg'}

    def __init__(self):
        self.sepwin = []
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('.computerhousekeeper\\img\\tool.jpg'))
        self.listWidget_tool.doubleClicked.connect(self.start_tool)
        self.listWidget_tool.customContextMenuRequested.connect(self.listWIdget_tool_showrightmenu)
        self.listWidget_tool_updata()

        logging.info(f'初始化{type(self).__name__}窗口')

    def listWIdget_tool_showrightmenu(self):
        menu = QMenu(self.listWidget_tool)
        action = menu.addAction('单独打开')
        action.triggered.connect(self.start_tool)
        menu.exec_(QCursor.pos())

        logging.info(f'{type(self).__name__}.{self.sender().objectName()}右键菜单')

    def listWidget_tool_updata(self):
        self.listWidget_tool.clear()
        for key in self.tools:
            item = QListWidgetItem()
            item.setSizeHint(QSize(32, 64))
            widget = ToolItemWidget(self.tools[key], key)
            widget.resize(32, 64)
            self.listWidget_tool.addItem(item)
            self.listWidget_tool.setItemWidget(item, widget)

        logging.info(f'{type(self).__name__}.listWidget_tool更新')

    def resizeEvent(self, a0: QtGui.QResizeEvent):
        self.listWidget_tool.resize(self.width(), self.height())
        logging.info(f'{type(self).__name__}大小改变')

    def start_tool(self):
        toolname = [AntiVirus,
                    Downloader,
                    FileSearch,
                    GarbageCleaning,
                    Software,
                    TaskManager]
        self.sepwin.append(toolname[self.listWidget_tool.currentRow()]())
        self.sepwin[-1].show()
        logging.info(f'{type(self).__name__}打开工具')


class ToolItemWidget(QWidget):
    def __init__(self, img, text):
        super().__init__()
        self.label_img = QLabel(self)
        self.label_img.setPixmap(QPixmap(img))
        self.label_img.setGeometry(0, 0, 64, 64)
        self.label_img.setScaledContents(True)

        self.label_text = QLabel(self)
        self.label_text.setText(text)
        self.label_text.setGeometry(64, 0, 128, 64)
        logging.info(f'初始化{type(self).__name__}')


if (__name__ == '__main__'):
    logging.basicConfig(level=logging.NOTSET,
                        filename='.computerhousekeeper\\debug.log',
                        filemode='w',
                        format='%(levelno)s %(levelname)s %(pathname)s %(filename)s %(funcName)s %(lineno)d %(asctime)s %(thread)d %(threadName)s %(process)d %(message)s')

    app = QApplication(sys.argv)
    tool = Tool()
    tool.show()
    logging.info('显示Tool窗口')
    app.exec_()

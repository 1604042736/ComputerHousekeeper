import sys

sys.path.append("..\\")

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import pyqtgraph as pg
import psutil
import traceback
import threading
import time
import os

try:
    from __pyqt__.Memory import *
except:
    from TaskManager.__pyqt__.Memory import *


class Memory(QWidget, Ui_Memory):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.plot_plt = pg.PlotWidget(self)
        self.plot_plt.showGrid(x=True, y=True)
        self.plot_plt.move(0, 0)
        self.plot_plt.resize(self.width(), self.height())
        self.plot_plt.setBackground('w')

        self.data_list = []
        self.showmemortinfo = ShowMemoryInfo(self)
        self.showmemortinfo.plot_update.connect(self.updata_plot)
        self.showmemortinfo.start()

        if (os.path.exists('.computerhousekeeper\\img\\memory.jpg')):
            self.setWindowIcon(QIcon('.computerhousekeeper\\img\\memory.jpg'))
        else:
            self.setWindowIcon(QIcon('..\\.computerhousekeeper\\img\\memory.jpg'))

    def updata_plot(self):
        self.plot_plt.plot().setData(self.data_list, pen='g')

    def resizeEvent(self, a0: QtGui.QResizeEvent):
        self.plot_plt.resize(self.width(), self.height())


class ShowMemoryInfo(QThread):
    plot_update = pyqtSignal()

    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def run(self):
        while (True):
            self.get_memory_info()
            time.sleep(1)

    def get_memory_info(self):
        try:
            mem = psutil.virtual_memory()
            self.parent.data_list.append(float(mem.used / 1024 / 1024 / 1024))
            print(float(mem.used / 1024 / 1024 / 1024))
            self.plot_update.emit()
        except Exception as e:
            print(traceback.print_exc())


if (__name__ == '__main__'):
    app = QApplication(sys.argv)
    memory = Memory()
    memory.show()
    app.exec_()

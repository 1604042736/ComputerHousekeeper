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
    from __pyqt__.CpuPercent import *
except:
    from TaskManager.__pyqt__.CpuPercent import *


class CpuPercent(QWidget, Ui_CpuPercent):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.plot_plt = pg.PlotWidget(self)
        self.plot_plt.showGrid(x=True, y=True)
        self.plot_plt.move(0, 0)
        self.plot_plt.resize(self.width(), self.height())
        self.plot_plt.setBackground('w')

        self.data_list = []
        self.showcpuinfo = ShowCPUInfo(self)
        self.showcpuinfo.plot_update.connect(self.updata_plot)
        self.showcpuinfo.start()

        if (os.path.exists('.computerhousekeeper\\img\\cpupercent.jpg')):
            self.setWindowIcon(QIcon('.computerhousekeeper\\img\\cpupercent.jpg'))
        else:
            self.setWindowIcon(QIcon('..\\.computerhousekeeper\\img\\cpupercent.jpg'))

    def updata_plot(self):
        self.plot_plt.plot().setData(self.data_list, pen='g')

    def resizeEvent(self, a0: QtGui.QResizeEvent):
        self.plot_plt.resize(self.width(), self.height())


class ShowCPUInfo(QThread):
    plot_update = pyqtSignal()

    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def run(self):
        while (True):
            self.get_cpu_info()
            # time.sleep(1)

    def get_cpu_info(self):
        try:
            cpu = "%0.2f" % psutil.cpu_percent(interval=1)
            self.parent.data_list.append(float(cpu))
            print(float(cpu))
            self.plot_update.emit()
        except Exception as e:
            print(traceback.print_exc())


if (__name__ == '__main__'):
    app = QApplication(sys.argv)
    cpupercent = CpuPercent()
    cpupercent.show()
    app.exec_()

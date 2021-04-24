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
    from __pyqt__.WLAN import *
except:
    from TaskManager.__pyqt__.WLAN import *


class WLAN(QWidget, Ui_WLAN):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.plot_plt = pg.PlotWidget(self)
        self.plot_plt.showGrid(x=True, y=True)
        self.plot_plt.move(0, 0)
        self.plot_plt.resize(self.width(), self.height())
        self.plot_plt.setBackground('w')

        self.data_list = []
        self.showwlaninfo = ShowWLANInfo(self)
        self.showwlaninfo.plot_update.connect(self.updata_plot)
        self.showwlaninfo.start()

        if (os.path.exists('.computerhousekeeper\\img\\WLAN.jpg')):
            self.setWindowIcon(QIcon('.computerhousekeeper\\img\\WLAN.jpg'))
        else:
            self.setWindowIcon(QIcon('..\\.computerhousekeeper\\img\\WLAN.jpg'))

    def updata_plot(self):
        self.plot_plt.plot().setData(self.data_list, pen='g')

    def resizeEvent(self, a0: QtGui.QResizeEvent):
        self.plot_plt.resize(self.width(), self.height())


class ShowWLANInfo(QThread):
    plot_update = pyqtSignal()

    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def run(self):
        while (True):
            self.get_wlan_info()
            time.sleep(1)

    def get_wlan_info(self):
        try:
            nets = self.__check_speeds()
            snap_prev = self.__snapshoot()
            snap_now = self.__snapshoot()
            net_name, speed = list(nets.items())[-1]
            recv_prev = snap_prev[net_name]
            recv_now = snap_now[net_name]
            rate = (recv_now - recv_prev) / (speed * 1024 * 1024 / 8.)
            print('name:%s,rate:%.2f%%' % (net_name, rate * 100))
            self.parent.data_list.append(rate * 100)
            self.plot_update.emit()
        except Exception as e:
            print(traceback.print_exc())

    def __snapshoot(self):
        rs = {}
        for net_name, stats in psutil.net_io_counters(pernic=True).items():
            rs[net_name] = stats.bytes_recv
        return rs

    def __check_speeds(self):
        rs = {}
        for net_name, stats in psutil.net_if_stats().items():
            if type(stats) is tuple or not stats.isup:
                continue
            rs[net_name] = stats.speed
        return rs


if (__name__ == '__main__'):
    app = QApplication(sys.argv)
    wlan = WLAN()
    wlan.show()
    app.exec_()

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import time
import psutil
import datetime
import os

try:
    from __pyqt__.Process import *
except:
    from TaskManager.__pyqt__.Process import *


class Process(QWidget, Ui_Process):
    PID, NAME, RUNTIME, CPUTIME, MEMUSAGE, IOCNTER, CONNECTIONS, THRDCNT = range(8)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.model = QStandardItemModel(0, 8, self)
        self.model.setHeaderData(self.PID, Qt.Horizontal, "pid")
        self.model.setHeaderData(self.NAME, Qt.Horizontal, "name")
        self.model.setHeaderData(self.RUNTIME, Qt.Horizontal, "runtime")
        self.model.setHeaderData(self.CPUTIME, Qt.Horizontal, "cputime")
        self.model.setHeaderData(self.MEMUSAGE, Qt.Horizontal, "memusage")
        self.model.setHeaderData(self.IOCNTER, Qt.Horizontal, "iocnter")
        self.model.setHeaderData(self.CONNECTIONS, Qt.Horizontal, "connections")
        self.model.setHeaderData(self.THRDCNT, Qt.Horizontal, "thrdcnt")

        self.treeView.setModel(self.model)

        self.pushButton_refresh.clicked.connect(self.get_process_info)

        if (os.path.exists('.computerhousekeeper\\img\\process.jpg')):
            self.setWindowIcon(QIcon('.computerhousekeeper\\img\\process.jpg'))
        else:
            self.setWindowIcon(QIcon('..\\.computerhousekeeper\\img\\process.jpg'))

    def get_process_info(self):
        self.model = QStandardItemModel(0, 8, self)
        self.model.setHeaderData(self.PID, Qt.Horizontal, "pid")
        self.model.setHeaderData(self.NAME, Qt.Horizontal, "name")
        self.model.setHeaderData(self.RUNTIME, Qt.Horizontal, "runtime")
        self.model.setHeaderData(self.CPUTIME, Qt.Horizontal, "cputime")
        self.model.setHeaderData(self.MEMUSAGE, Qt.Horizontal, "memusage")
        self.model.setHeaderData(self.IOCNTER, Qt.Horizontal, "iocnter")
        self.model.setHeaderData(self.CONNECTIONS, Qt.Horizontal, "connections")
        self.model.setHeaderData(self.THRDCNT, Qt.Horizontal, "thrdcnt")
        self.treeView.setModel(self.model)
        for proc in psutil.process_iter():
            procinfo = get_proc_running_info(proc.pid)
            self.model.insertRow(0)
            self.model.setData(self.model.index(0, self.PID), procinfo['pid'])
            self.model.setData(self.model.index(0, self.NAME), procinfo['name'])
            self.model.setData(self.model.index(0, self.RUNTIME), procinfo['run_time'])
            self.model.setData(self.model.index(0, self.CPUTIME), procinfo['cpu_time'])
            self.model.setData(self.model.index(0, self.MEMUSAGE), procinfo['mem_usage'])
            self.model.setData(self.model.index(0, self.IOCNTER), procinfo['io_cnter'])
            self.model.setData(self.model.index(0, self.CONNECTIONS), procinfo['connections'])
            self.model.setData(self.model.index(0, self.THRDCNT), procinfo['thrd_cnt'])

    def resizeEvent(self, a0: QtGui.QResizeEvent):
        self.treeView.resize(self.width(), self.height() - self.pushButton_refresh.height())
        self.pushButton_refresh.move(self.width() - self.pushButton_refresh.width(),
                                     self.height() - self.pushButton_refresh.height())
        self.pushButton_stop.move(self.width() - self.pushButton_refresh.width() - self.pushButton_stop.width(),
                                  self.height() - self.pushButton_stop.height())


class ShowProcess(QThread):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def run(self):
        while (True):
            self.get_process_info()
            time.sleep(1)

    def get_process_info(self):
        self.parent.model.clear()
        for proc in psutil.process_iter():
            self.parent.model.invisibleRootItem().appendRow(QStandardItem(proc.name()))


def get_proc_running_info(pid):
    proc_info = {}
    proc_info['pid'] = pid

    proc = psutil.Process(pid)
    proc_info['name'] = proc.name()
    # proc_info['path'] = proc.exe()
    # proc_info['work_dir'] = proc.cwd()
    proc_info['run_time'] = datetime.datetime.fromtimestamp(proc.create_time()).strftime("%Y-%m-%d %H:%M:%S")
    proc_info['cpu_time'] = str(proc.cpu_times())
    proc_info['mem_usage'] = str(proc.memory_info())
    proc_info['io_cnter'] = str(proc.io_counters())
    proc_info['connections'] = str(proc.connections())
    proc_info['thrd_cnt'] = proc.num_threads()

    return proc_info


if (__name__ == '__main__'):
    app = QApplication(sys.argv)
    process = Process()
    process.show()
    app.exec_()

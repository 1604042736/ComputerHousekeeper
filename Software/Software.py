import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import winreg

try:
    from __pyqt__.Software import *
except:
    from Software.__pyqt__.Software import *


class Software(QWidget, Ui_Software):
    paths = [
        'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall',
        'SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall',
    ]

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.listWidget_updata()

        if (os.path.exists('.computerhousekeeper\\img\\software.jpg')):
            self.setWindowIcon(QIcon('.computerhousekeeper\\img\\software.jpg'))
        else:
            self.setWindowIcon(QIcon('..\\.computerhousekeeper\\img\\software.jpg'))

    def listWidget_updata(self):
        self.listWidget.clear()

        for curPath in self.paths:
            try:
                mainKey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, curPath)
                try:
                    i = 0
                    while (1):
                        name = winreg.EnumKey(mainKey, i)
                        try:
                            item = QListWidgetItem()
                            item.setSizeHint(QSize(32, 64))
                            widget = SoftwareItem(f'{curPath}\\{name}')
                            widget.resize(32, 64)
                            self.listWidget.addItem(item)
                            self.listWidget.setItemWidget(item, widget)
                        except Exception as e:
                            print(e)
                        i += 1
                except Exception as e:
                    print(e)
            except Exception as e:
                print(e)
            finally:
                winreg.CloseKey(mainKey)

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        self.listWidget.resize(self.width(), self.height())


class SoftwareItem(QWidget):
    def __init__(self, regpath):
        super().__init__()

        self.setStyleSheet("QPushButton\n"
                           "{\n"
                           "    border:0px solid rgb(16,124,16);\n"
                           "    background-color:white\n"
                           "}\n"
                           "QPushButton:hover\n"
                           "{\n"
                           "    border:2px solid rgb(16,124,16);\n"
                           "    border-color:green\n"
                           "}\n"
                           "QPushButton:pressed\n"
                           "{\n"
                           "    background-color:rgb(195, 195, 195)\n"
                           "}")

        self.regpath = regpath

        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, self.regpath)

            self.name = winreg.QueryValueEx(key, "DisplayName")[0]
            self.label_name = QLabel(self)
            self.label_name.setText(self.name)
            self.label_name.setGeometry(0, 0, 500, 64)

            self.uninstallstring = winreg.QueryValueEx(key, "UninstallString")[0]
            print(self.uninstallstring)

            self.pushButton_uninstall = QPushButton(self)
            self.pushButton_uninstall.setText('卸载')
            self.pushButton_uninstall.resize(64, 32)
            self.pushButton_uninstall.move(self.width() - self.pushButton_uninstall.width(), 0)
            self.pushButton_uninstall.clicked.connect(self.uninstall)
        except Exception as e:
            raise Exception
        finally:
            winreg.CloseKey(key)

    def uninstall(self):
        print(f'"{self.uninstallstring}"')
        os.popen(f'"{self.uninstallstring}"')

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        try:
            self.label_name.resize(int(self.width() / 2), self.label_name.height())
            self.pushButton_uninstall.move(self.width() - self.pushButton_uninstall.width(),
                                           self.pushButton_uninstall.y())
        except Exception as e:
            print(e)


if (__name__ == '__main__'):
    app = QApplication(sys.argv)
    software = Software()
    software.show()
    app.exec_()

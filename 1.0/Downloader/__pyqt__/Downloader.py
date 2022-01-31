# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Downloader.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Downloader(object):
    def setupUi(self, Downloader):
        Downloader.setObjectName("Downloader")
        Downloader.resize(1000, 618)
        Downloader.setStyleSheet("QWidget#Downloader\n"
                                 "{\n"
                                 "    background-color:white\n"
                                 "}")
        self.lineEdit_url = QtWidgets.QLineEdit(Downloader)
        self.lineEdit_url.setGeometry(QtCore.QRect(0, 0, 512, 32))
        self.lineEdit_url.setObjectName("lineEdit_url")
        self.lineEdit_path = QtWidgets.QLineEdit(Downloader)
        self.lineEdit_path.setGeometry(QtCore.QRect(0, 32, 512, 32))
        self.lineEdit_path.setObjectName("lineEdit_path")
        self.pushButton_start = QtWidgets.QPushButton(Downloader)
        self.pushButton_start.setGeometry(QtCore.QRect(512, 0, 64, 32))
        self.pushButton_start.setStyleSheet("QPushButton#pushButton_start\n"
                                            "{\n"
                                            "    border:0px solid rgb(16,124,16);\n"
                                            "    background-color:white\n"
                                            "}\n"
                                            "QPushButton#pushButton_start:hover\n"
                                            "{\n"
                                            "    border:2px solid rgb(16,124,16);\n"
                                            "    border-color:green\n"
                                            "}\n"
                                            "QPushButton#pushButton_start:pressed\n"
                                            "{\n"
                                            "    background-color:rgb(195, 195, 195)\n"
                                            "}")
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_choose = QtWidgets.QPushButton(Downloader)
        self.pushButton_choose.setGeometry(QtCore.QRect(512, 32, 64, 32))
        self.pushButton_choose.setStyleSheet("QPushButton#pushButton_choose\n"
                                             "{\n"
                                             "    border:0px solid rgb(16,124,16);\n"
                                             "    background-color:white\n"
                                             "}\n"
                                             "QPushButton#pushButton_choose:hover\n"
                                             "{\n"
                                             "    border:2px solid rgb(16,124,16);\n"
                                             "    border-color:green\n"
                                             "}\n"
                                             "QPushButton#pushButton_choose:pressed\n"
                                             "{\n"
                                             "    background-color:rgb(195, 195, 195)\n"
                                             "}")
        self.pushButton_choose.setObjectName("pushButton_choose")
        self.listWidget = QtWidgets.QListWidget(Downloader)
        self.listWidget.setGeometry(QtCore.QRect(0, 64, 1000, 554))
        self.listWidget.setStyleSheet("QListWidget#listWidget\n"
                                      "{\n"
                                      "    border:none\n"
                                      "}")
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(Downloader)
        QtCore.QMetaObject.connectSlotsByName(Downloader)

    def retranslateUi(self, Downloader):
        _translate = QtCore.QCoreApplication.translate
        Downloader.setWindowTitle(_translate("Downloader", "Downloader"))
        self.lineEdit_url.setPlaceholderText(_translate("Downloader", "请输入下载网址"))
        self.lineEdit_path.setPlaceholderText(_translate("Downloader", "请输入下载路径"))
        self.pushButton_start.setText(_translate("Downloader", "开始"))
        self.pushButton_choose.setText(_translate("Downloader", "选择"))

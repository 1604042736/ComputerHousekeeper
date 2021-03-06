# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FileSearch.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FileSearch(object):
    def setupUi(self, FileSearch):
        FileSearch.setObjectName("FileSearch")
        FileSearch.resize(1000, 618)
        FileSearch.setStyleSheet("QWidget#FileSearch\n"
                                 "{\n"
                                 "    background-color:white\n"
                                 "}")
        self.lineEdit_path = QtWidgets.QLineEdit(FileSearch)
        self.lineEdit_path.setGeometry(QtCore.QRect(0, 0, 500, 32))
        self.lineEdit_path.setObjectName("lineEdit_path")
        self.pushButton_choose = QtWidgets.QPushButton(FileSearch)
        self.pushButton_choose.setGeometry(QtCore.QRect(500, 0, 64, 32))
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
        self.lineEdit_key = QtWidgets.QLineEdit(FileSearch)
        self.lineEdit_key.setGeometry(QtCore.QRect(564, 0, 372, 32))
        self.lineEdit_key.setObjectName("lineEdit_key")
        self.pushButton_start = QtWidgets.QPushButton(FileSearch)
        self.pushButton_start.setGeometry(QtCore.QRect(936, 0, 64, 32))
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
        self.listWidget_result = QtWidgets.QListWidget(FileSearch)
        self.listWidget_result.setGeometry(QtCore.QRect(0, 32, 1000, 586))
        self.listWidget_result.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.listWidget_result.setStyleSheet("QListWidget#listWidget_result\n"
                                             "{\n"
                                             "    border:none\n"
                                             "}")
        self.listWidget_result.setObjectName("listWidget_result")

        self.retranslateUi(FileSearch)
        QtCore.QMetaObject.connectSlotsByName(FileSearch)

    def retranslateUi(self, FileSearch):
        _translate = QtCore.QCoreApplication.translate
        FileSearch.setWindowTitle(_translate("FileSearch", "FileSearch"))
        self.lineEdit_path.setPlaceholderText(_translate("FileSearch", "?????????????????????"))
        self.pushButton_choose.setText(_translate("FileSearch", "??????"))
        self.lineEdit_key.setPlaceholderText(_translate("FileSearch", "??????????????????"))
        self.pushButton_start.setText(_translate("FileSearch", "??????"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Software.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Software(object):
    def setupUi(self, Software):
        Software.setObjectName("Software")
        Software.resize(1000, 618)
        Software.setStyleSheet("QWidget#Software\n"
                               "{\n"
                               "    background-color:white\n"
                               "}")
        self.listWidget = QtWidgets.QListWidget(Software)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 1000, 618))
        self.listWidget.setStyleSheet("QListWidget#listWidget\n"
                                      "{\n"
                                      "    border:none\n"
                                      "}")
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(Software)
        QtCore.QMetaObject.connectSlotsByName(Software)

    def retranslateUi(self, Software):
        _translate = QtCore.QCoreApplication.translate
        Software.setWindowTitle(_translate("Software", "Software"))

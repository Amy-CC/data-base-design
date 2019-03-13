# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_flight.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_deleteflight(object):
    def setupUi(self, deleteflight):
        deleteflight.setObjectName("deleteflight")
        deleteflight.resize(354, 239)
        self.label = QtWidgets.QLabel(deleteflight)
        self.label.setGeometry(QtCore.QRect(110, 50, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.userid = QtWidgets.QLineEdit(deleteflight)
        self.userid.setGeometry(QtCore.QRect(60, 100, 231, 31))
        self.userid.setObjectName("userid")
        self.delok = QtWidgets.QPushButton(deleteflight)
        self.delok.setGeometry(QtCore.QRect(130, 180, 75, 23))
        self.delok.setObjectName("delok")

        self.retranslateUi(deleteflight)
        QtCore.QMetaObject.connectSlotsByName(deleteflight)

    def retranslateUi(self, deleteflight):
        _translate = QtCore.QCoreApplication.translate
        deleteflight.setWindowTitle(_translate("deleteflight", "删除"))
        self.label.setText(_translate("deleteflight", "请输入航班号"))
        self.delok.setText(_translate("deleteflight", "OK"))


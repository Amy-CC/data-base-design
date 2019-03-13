# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_orders.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_deleteorders(object):
    def setupUi(self, deleteorders):
        deleteorders.setObjectName("deleteorders")
        deleteorders.resize(354, 239)
        self.label = QtWidgets.QLabel(deleteorders)
        self.label.setGeometry(QtCore.QRect(110, 50, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.userid = QtWidgets.QLineEdit(deleteorders)
        self.userid.setGeometry(QtCore.QRect(60, 100, 231, 31))
        self.userid.setObjectName("userid")
        self.delok = QtWidgets.QPushButton(deleteorders)
        self.delok.setGeometry(QtCore.QRect(130, 180, 75, 23))
        self.delok.setObjectName("delok")

        self.retranslateUi(deleteorders)
        QtCore.QMetaObject.connectSlotsByName(deleteorders)

    def retranslateUi(self, deleteorders):
        _translate = QtCore.QCoreApplication.translate
        deleteorders.setWindowTitle(_translate("deleteorders", "删除"))
        self.label.setText(_translate("deleteorders", "请输入订单号"))
        self.delok.setText(_translate("deleteorders", "OK"))


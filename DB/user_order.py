# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_order.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_userorder(object):
    def setupUi(self, userorder):
        userorder.setObjectName("userorder")
        userorder.resize(832, 433)
        self.tableView = QtWidgets.QTableView(userorder)
        self.tableView.setGeometry(QtCore.QRect(20, 30, 791, 341))
        self.tableView.setObjectName("tableView")
        self.pushButton = QtWidgets.QPushButton(userorder)
        self.pushButton.setGeometry(QtCore.QRect(380, 390, 111, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(userorder)
        QtCore.QMetaObject.connectSlotsByName(userorder)

    def retranslateUi(self, userorder):
        _translate = QtCore.QCoreApplication.translate
        userorder.setWindowTitle(_translate("userorder", "订单"))
        self.pushButton.setText(_translate("userorder", "OK"))


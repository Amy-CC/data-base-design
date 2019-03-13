# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_buy_flight.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_userbuyflight(object):
    def setupUi(self, userbuyflight):
        userbuyflight.setObjectName("userbuyflight")
        userbuyflight.resize(830, 439)
        self.tableView = QtWidgets.QTableView(userbuyflight)
        self.tableView.setGeometry(QtCore.QRect(20, 20, 791, 361))
        self.tableView.setObjectName("tableView")
        self.cancel = QtWidgets.QPushButton(userbuyflight)
        self.cancel.setGeometry(QtCore.QRect(520, 390, 111, 31))
        self.cancel.setObjectName("cancel")
        self.book = QtWidgets.QPushButton(userbuyflight)
        self.book.setGeometry(QtCore.QRect(200, 390, 111, 31))
        self.book.setObjectName("book")

        self.retranslateUi(userbuyflight)
        QtCore.QMetaObject.connectSlotsByName(userbuyflight)

    def retranslateUi(self, userbuyflight):
        _translate = QtCore.QCoreApplication.translate
        userbuyflight.setWindowTitle(_translate("userbuyflight", "航班信息"))
        self.cancel.setText(_translate("userbuyflight", "退出"))
        self.book.setText(_translate("userbuyflight", "订票"))


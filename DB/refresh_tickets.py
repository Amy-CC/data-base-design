# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'refresh_tickets.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_refreshTickets(object):
    def setupUi(self, refreshTickets):
        refreshTickets.setObjectName("refreshTickets")
        refreshTickets.resize(504, 261)
        self.reok = QtWidgets.QPushButton(refreshTickets)
        self.reok.setGeometry(QtCore.QRect(190, 220, 75, 23))
        self.reok.setObjectName("reok")
        self.label_3 = QtWidgets.QLabel(refreshTickets)
        self.label_3.setGeometry(QtCore.QRect(50, 40, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.ticketprice = QtWidgets.QLineEdit(refreshTickets)
        self.ticketprice.setGeometry(QtCore.QRect(220, 40, 231, 31))
        self.ticketprice.setObjectName("ticketprice")
        self.label_7 = QtWidgets.QLabel(refreshTickets)
        self.label_7.setGeometry(QtCore.QRect(50, 90, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.discount = QtWidgets.QLineEdit(refreshTickets)
        self.discount.setGeometry(QtCore.QRect(220, 90, 231, 31))
        self.discount.setObjectName("discount")
        self.label_8 = QtWidgets.QLabel(refreshTickets)
        self.label_8.setGeometry(QtCore.QRect(50, 150, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.state = QtWidgets.QLineEdit(refreshTickets)
        self.state.setGeometry(QtCore.QRect(220, 150, 231, 31))
        self.state.setObjectName("state")
        self.label_9 = QtWidgets.QLabel(refreshTickets)
        self.label_9.setGeometry(QtCore.QRect(310, 120, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(refreshTickets)
        self.label_10.setGeometry(QtCore.QRect(260, 180, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.retranslateUi(refreshTickets)
        QtCore.QMetaObject.connectSlotsByName(refreshTickets)

    def retranslateUi(self, refreshTickets):
        _translate = QtCore.QCoreApplication.translate
        refreshTickets.setWindowTitle(_translate("refreshTickets", "更新"))
        self.reok.setText(_translate("refreshTickets", "OK"))
        self.label_3.setText(_translate("refreshTickets", "请输入票价"))
        self.label_7.setText(_translate("refreshTickets", "请输入折扣"))
        self.label_8.setText(_translate("refreshTickets", "当前预售状态"))
        self.label_9.setText(_translate("refreshTickets", "形如0.1"))
        self.label_10.setText(_translate("refreshTickets", "已出售，未出售，不出售"))


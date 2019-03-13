# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mana_tickets.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mana_ticket(object):
    def setupUi(self, mana_ticket):
        mana_ticket.setObjectName("mana_ticket")
        mana_ticket.resize(631, 412)
        self.userview = QtWidgets.QTableView(mana_ticket)
        self.userview.setGeometry(QtCore.QRect(30, 30, 571, 321))
        self.userview.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.userview.setObjectName("userview")
        self.return_2 = QtWidgets.QPushButton(mana_ticket)
        self.return_2.setGeometry(QtCore.QRect(360, 370, 75, 23))
        self.return_2.setObjectName("return_2")
        self.refresh = QtWidgets.QPushButton(mana_ticket)
        self.refresh.setGeometry(QtCore.QRect(160, 370, 75, 23))
        self.refresh.setObjectName("refresh")

        self.retranslateUi(mana_ticket)
        QtCore.QMetaObject.connectSlotsByName(mana_ticket)

    def retranslateUi(self, mana_ticket):
        _translate = QtCore.QCoreApplication.translate
        mana_ticket.setWindowTitle(_translate("mana_ticket", "机票管理"))
        self.return_2.setText(_translate("mana_ticket", "退出"))
        self.refresh.setText(_translate("mana_ticket", "更新"))


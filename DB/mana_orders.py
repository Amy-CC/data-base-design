# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mana_orders.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mana_order(object):
    def setupUi(self, mana_order):
        mana_order.setObjectName("mana_order")
        mana_order.resize(634, 412)
        self.userview = QtWidgets.QTableView(mana_order)
        self.userview.setGeometry(QtCore.QRect(30, 30, 571, 321))
        self.userview.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.userview.setObjectName("userview")
        self.add = QtWidgets.QPushButton(mana_order)
        self.add.setGeometry(QtCore.QRect(110, 370, 75, 23))
        self.add.setObjectName("add")
        self.delete_2 = QtWidgets.QPushButton(mana_order)
        self.delete_2.setGeometry(QtCore.QRect(230, 370, 75, 23))
        self.delete_2.setObjectName("delete_2")
        self.return_2 = QtWidgets.QPushButton(mana_order)
        self.return_2.setGeometry(QtCore.QRect(450, 370, 75, 23))
        self.return_2.setObjectName("return_2")
        self.refresh = QtWidgets.QPushButton(mana_order)
        self.refresh.setGeometry(QtCore.QRect(340, 370, 75, 23))
        self.refresh.setObjectName("refresh")

        self.retranslateUi(mana_order)
        QtCore.QMetaObject.connectSlotsByName(mana_order)

    def retranslateUi(self, mana_order):
        _translate = QtCore.QCoreApplication.translate
        mana_order.setWindowTitle(_translate("mana_order", "订单管理"))
        self.add.setText(_translate("mana_order", "添加"))
        self.delete_2.setText(_translate("mana_order", "删除"))
        self.return_2.setText(_translate("mana_order", "退出"))
        self.refresh.setText(_translate("mana_order", "更新"))


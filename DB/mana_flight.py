# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mana_flight.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mana_flight(object):
    def setupUi(self, mana_flight):
        mana_flight.setObjectName("mana_flight")
        mana_flight.resize(634, 406)
        self.userview = QtWidgets.QTableView(mana_flight)
        self.userview.setGeometry(QtCore.QRect(30, 30, 571, 321))
        self.userview.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.userview.setObjectName("userview")
        self.add = QtWidgets.QPushButton(mana_flight)
        self.add.setGeometry(QtCore.QRect(100, 370, 75, 23))
        self.add.setObjectName("add")
        self.delete_2 = QtWidgets.QPushButton(mana_flight)
        self.delete_2.setGeometry(QtCore.QRect(250, 370, 75, 23))
        self.delete_2.setObjectName("delete_2")
        self.return_2 = QtWidgets.QPushButton(mana_flight)
        self.return_2.setGeometry(QtCore.QRect(500, 370, 75, 23))
        self.return_2.setObjectName("return_2")
        self.refresh = QtWidgets.QPushButton(mana_flight)
        self.refresh.setGeometry(QtCore.QRect(370, 370, 75, 23))
        self.refresh.setObjectName("refresh")

        self.retranslateUi(mana_flight)
        QtCore.QMetaObject.connectSlotsByName(mana_flight)

    def retranslateUi(self, mana_flight):
        _translate = QtCore.QCoreApplication.translate
        mana_flight.setWindowTitle(_translate("mana_flight", "航班管理"))
        self.add.setText(_translate("mana_flight", "添加"))
        self.delete_2.setText(_translate("mana_flight", "删除"))
        self.return_2.setText(_translate("mana_flight", "退出"))
        self.refresh.setText(_translate("mana_flight", "更新"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manauser.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mana_user(object):
    def setupUi(self, mana_user):
        mana_user.setObjectName("mana_user")
        mana_user.resize(629, 416)
        self.label = QtWidgets.QLabel(mana_user)
        self.label.setGeometry(QtCore.QRect(350, 60, 54, 12))
        self.label.setText("")
        self.label.setObjectName("label")
        self.userview = QtWidgets.QTableView(mana_user)
        self.userview.setGeometry(QtCore.QRect(30, 30, 571, 321))
        self.userview.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.userview.setObjectName("userview")
        self.add = QtWidgets.QPushButton(mana_user)
        self.add.setGeometry(QtCore.QRect(110, 370, 75, 23))
        self.add.setObjectName("add")
        self.delete_2 = QtWidgets.QPushButton(mana_user)
        self.delete_2.setGeometry(QtCore.QRect(230, 370, 75, 23))
        self.delete_2.setObjectName("delete_2")
        self.return_2 = QtWidgets.QPushButton(mana_user)
        self.return_2.setGeometry(QtCore.QRect(490, 370, 75, 23))
        self.return_2.setObjectName("return_2")
        self.refresh = QtWidgets.QPushButton(mana_user)
        self.refresh.setGeometry(QtCore.QRect(360, 370, 75, 23))
        self.refresh.setObjectName("refresh")

        self.retranslateUi(mana_user)
        QtCore.QMetaObject.connectSlotsByName(mana_user)

    def retranslateUi(self, mana_user):
        _translate = QtCore.QCoreApplication.translate
        mana_user.setWindowTitle(_translate("mana_user", "用户管理"))
        self.add.setText(_translate("mana_user", "添加"))
        self.delete_2.setText(_translate("mana_user", "删除"))
        self.return_2.setText(_translate("mana_user", "退出"))
        self.refresh.setText(_translate("mana_user", "更新"))


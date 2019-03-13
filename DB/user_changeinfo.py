# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_changeinfo.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_userchangeinfo(object):
    def setupUi(self, userchangeinfo):
        userchangeinfo.setObjectName("userchangeinfo")
        userchangeinfo.resize(832, 435)
        self.tableView = QtWidgets.QTableView(userchangeinfo)
        self.tableView.setGeometry(QtCore.QRect(20, 30, 791, 341))
        self.tableView.setObjectName("tableView")
        self.cancel = QtWidgets.QPushButton(userchangeinfo)
        self.cancel.setGeometry(QtCore.QRect(560, 390, 111, 31))
        self.cancel.setObjectName("cancel")
        self.refresh = QtWidgets.QPushButton(userchangeinfo)
        self.refresh.setGeometry(QtCore.QRect(160, 390, 111, 31))
        self.refresh.setObjectName("refresh")

        self.retranslateUi(userchangeinfo)
        QtCore.QMetaObject.connectSlotsByName(userchangeinfo)

    def retranslateUi(self, userchangeinfo):
        _translate = QtCore.QCoreApplication.translate
        userchangeinfo.setWindowTitle(_translate("userchangeinfo", "修改用户信息"))
        self.cancel.setText(_translate("userchangeinfo", "退出"))
        self.refresh.setText(_translate("userchangeinfo", "更新"))


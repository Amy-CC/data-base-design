# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_users.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_deleteusers(object):
    def setupUi(self, deleteusers):
        deleteusers.setObjectName("deleteusers")
        deleteusers.resize(354, 239)
        self.label = QtWidgets.QLabel(deleteusers)
        self.label.setGeometry(QtCore.QRect(100, 50, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.userid = QtWidgets.QLineEdit(deleteusers)
        self.userid.setGeometry(QtCore.QRect(60, 100, 231, 31))
        self.userid.setObjectName("userid")
        self.delok = QtWidgets.QPushButton(deleteusers)
        self.delok.setGeometry(QtCore.QRect(130, 180, 75, 23))
        self.delok.setObjectName("delok")

        self.retranslateUi(deleteusers)
        QtCore.QMetaObject.connectSlotsByName(deleteusers)

    def retranslateUi(self, deleteusers):
        _translate = QtCore.QCoreApplication.translate
        deleteusers.setWindowTitle(_translate("deleteusers", "删除"))
        self.label.setText(_translate("deleteusers", "请输入客户编号"))
        self.delok.setText(_translate("deleteusers", "OK"))


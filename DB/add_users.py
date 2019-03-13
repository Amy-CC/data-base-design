# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_users.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_addusers(object):
    def setupUi(self, addusers):
        addusers.setObjectName("addusers")
        addusers.resize(354, 239)
        self.label = QtWidgets.QLabel(addusers)
        self.label.setGeometry(QtCore.QRect(50, 50, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(addusers)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.userid = QtWidgets.QLineEdit(addusers)
        self.userid.setGeometry(QtCore.QRect(130, 49, 131, 31))
        self.userid.setObjectName("userid")
        self.userpassword = QtWidgets.QLineEdit(addusers)
        self.userpassword.setGeometry(QtCore.QRect(130, 110, 131, 31))
        self.userpassword.setObjectName("userpassword")
        self.adOk = QtWidgets.QPushButton(addusers)
        self.adOk.setGeometry(QtCore.QRect(130, 180, 75, 23))
        self.adOk.setObjectName("adOk")

        self.retranslateUi(addusers)
        QtCore.QMetaObject.connectSlotsByName(addusers)

    def retranslateUi(self, addusers):
        _translate = QtCore.QCoreApplication.translate
        addusers.setWindowTitle(_translate("addusers", "添加"))
        self.label.setText(_translate("addusers", "账号"))
        self.label_2.setText(_translate("addusers", "密码"))
        self.adOk.setText(_translate("addusers", "OK"))


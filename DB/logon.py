# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logon.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_logon(object):
    def setupUi(self, logon):
        logon.setObjectName("logon")
        logon.resize(354, 239)
        self.label = QtWidgets.QLabel(logon)
        self.label.setGeometry(QtCore.QRect(50, 50, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(logon)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.userid = QtWidgets.QLineEdit(logon)
        self.userid.setGeometry(QtCore.QRect(130, 49, 131, 31))
        self.userid.setObjectName("userid")
        self.userpassword = QtWidgets.QLineEdit(logon)
        self.userpassword.setGeometry(QtCore.QRect(130, 110, 131, 31))
        self.userpassword.setObjectName("userpassword")
        self.pushButton = QtWidgets.QPushButton(logon)
        self.pushButton.setGeometry(QtCore.QRect(130, 180, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(logon)
        QtCore.QMetaObject.connectSlotsByName(logon)

    def retranslateUi(self, logon):
        _translate = QtCore.QCoreApplication.translate
        logon.setWindowTitle(_translate("logon", "登录"))
        self.label.setText(_translate("logon", "账号"))
        self.label_2.setText(_translate("logon", "密码"))
        self.pushButton.setText(_translate("logon", "OK"))


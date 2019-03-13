# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_regist(object):
    def setupUi(self, regist):
        regist.setObjectName("regist")
        regist.resize(354, 239)
        self.label = QtWidgets.QLabel(regist)
        self.label.setGeometry(QtCore.QRect(50, 50, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(regist)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.userid = QtWidgets.QLineEdit(regist)
        self.userid.setGeometry(QtCore.QRect(130, 49, 131, 31))
        self.userid.setObjectName("userid")
        self.userpassword = QtWidgets.QLineEdit(regist)
        self.userpassword.setGeometry(QtCore.QRect(130, 110, 131, 31))
        self.userpassword.setObjectName("userpassword")
        self.pushButton = QtWidgets.QPushButton(regist)
        self.pushButton.setGeometry(QtCore.QRect(130, 180, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(regist)
        QtCore.QMetaObject.connectSlotsByName(regist)

    def retranslateUi(self, regist):
        _translate = QtCore.QCoreApplication.translate
        regist.setWindowTitle(_translate("regist", "注册"))
        self.label.setText(_translate("regist", "账号"))
        self.label_2.setText(_translate("regist", "密码"))
        self.pushButton.setText(_translate("regist", "OK"))


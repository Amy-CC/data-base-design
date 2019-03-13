# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_ticket_choose.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_user_ticket_choose(object):
    def setupUi(self, user_ticket_choose):
        user_ticket_choose.setObjectName("user_ticket_choose")
        user_ticket_choose.resize(567, 236)
        self.label = QtWidgets.QLabel(user_ticket_choose)
        self.label.setGeometry(QtCore.QRect(50, 50, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(user_ticket_choose)
        self.label_2.setGeometry(QtCore.QRect(50, 120, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(user_ticket_choose)
        self.pushButton.setGeometry(QtCore.QRect(220, 190, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.go = QtWidgets.QLineEdit(user_ticket_choose)
        self.go.setGeometry(QtCore.QRect(250, 60, 201, 31))
        self.go.setObjectName("go")
        self.purpose = QtWidgets.QLineEdit(user_ticket_choose)
        self.purpose.setGeometry(QtCore.QRect(250, 120, 201, 31))
        self.purpose.setObjectName("purpose")

        self.retranslateUi(user_ticket_choose)
        QtCore.QMetaObject.connectSlotsByName(user_ticket_choose)

    def retranslateUi(self, user_ticket_choose):
        _translate = QtCore.QCoreApplication.translate
        user_ticket_choose.setWindowTitle(_translate("user_ticket_choose", "选择订购的航班"))
        self.label.setText(_translate("user_ticket_choose", "请输入出发地点"))
        self.label_2.setText(_translate("user_ticket_choose", "请输入目的地"))
        self.pushButton.setText(_translate("user_ticket_choose", "OK"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_return.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_return_3(object):
    def setupUi(self, return_3):
        return_3.setObjectName("return_3")
        return_3.resize(508, 300)
        self.label = QtWidgets.QLabel(return_3)
        self.label.setGeometry(QtCore.QRect(80, 30, 361, 111))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.return_2 = QtWidgets.QLineEdit(return_3)
        self.return_2.setGeometry(QtCore.QRect(50, 130, 411, 51))
        self.return_2.setObjectName("return_2")
        self.pushButton = QtWidgets.QPushButton(return_3)
        self.pushButton.setGeometry(QtCore.QRect(190, 220, 111, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(return_3)
        QtCore.QMetaObject.connectSlotsByName(return_3)

    def retranslateUi(self, return_3):
        _translate = QtCore.QCoreApplication.translate
        return_3.setWindowTitle(_translate("return_3", "Form"))
        self.label.setText(_translate("return_3", "请输入需要退订的票号"))
        self.pushButton.setText(_translate("return_3", "OK"))


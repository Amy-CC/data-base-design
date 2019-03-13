# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_book.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(459, 306)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 40, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.flightid = QtWidgets.QLineEdit(Form)
        self.flightid.setGeometry(QtCore.QRect(190, 40, 231, 31))
        self.flightid.setObjectName("flightid")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(40, 100, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.fnum = QtWidgets.QLineEdit(Form)
        self.fnum.setGeometry(QtCore.QRect(190, 100, 231, 31))
        self.fnum.setObjectName("fnum")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(40, 150, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.enum_2 = QtWidgets.QLineEdit(Form)
        self.enum_2.setGeometry(QtCore.QRect(190, 150, 231, 31))
        self.enum_2.setObjectName("enum_2")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(40, 200, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.Bnum = QtWidgets.QLineEdit(Form)
        self.Bnum.setGeometry(QtCore.QRect(190, 200, 231, 31))
        self.Bnum.setObjectName("Bnum")
        self.reok = QtWidgets.QPushButton(Form)
        self.reok.setGeometry(QtCore.QRect(190, 260, 75, 23))
        self.reok.setObjectName("reok")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "请输入航班号"))
        self.label_10.setText(_translate("Form", "头等舱机票数"))
        self.label_11.setText(_translate("Form", "经济舱机票数"))
        self.label_12.setText(_translate("Form", "商务舱机票数"))
        self.reok.setText(_translate("Form", "OK"))


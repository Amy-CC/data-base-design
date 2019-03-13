# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mana_ticket_choose.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mana_ticket_choose(object):
    def setupUi(self, mana_ticket_choose):
        mana_ticket_choose.setObjectName("mana_ticket_choose")
        mana_ticket_choose.resize(475, 282)
        self.label = QtWidgets.QLabel(mana_ticket_choose)
        self.label.setGeometry(QtCore.QRect(130, 0, 221, 111))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(mana_ticket_choose)
        self.lineEdit.setGeometry(QtCore.QRect(60, 110, 361, 61))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(mana_ticket_choose)
        self.pushButton.setGeometry(QtCore.QRect(190, 220, 101, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(mana_ticket_choose)
        QtCore.QMetaObject.connectSlotsByName(mana_ticket_choose)

    def retranslateUi(self, mana_ticket_choose):
        _translate = QtCore.QCoreApplication.translate
        mana_ticket_choose.setWindowTitle(_translate("mana_ticket_choose", "筛选"))
        self.label.setText(_translate("mana_ticket_choose", "请输入航班号"))
        self.pushButton.setText(_translate("mana_ticket_choose", "确认"))


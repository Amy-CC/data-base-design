# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'managemenu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_manawindow(object):
    def setupUi(self, manawindow):
        manawindow.setObjectName("manawindow")
        manawindow.resize(830, 337)
        self.centralwidget = QtWidgets.QWidget(manawindow)
        self.centralwidget.setObjectName("centralwidget")
        self.flight = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.flight.setGeometry(QtCore.QRect(600, 70, 185, 41))
        self.flight.setObjectName("flight")
        self.manamenu = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.manamenu.setGeometry(QtCore.QRect(600, 20, 185, 41))
        self.manamenu.setObjectName("manamenu")
        self.ticket = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.ticket.setGeometry(QtCore.QRect(600, 130, 185, 41))
        self.ticket.setObjectName("ticket")
        self.order = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.order.setGeometry(QtCore.QRect(600, 190, 185, 41))
        self.order.setObjectName("order")
        self.user_4 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.user_4.setGeometry(QtCore.QRect(600, 250, 185, 41))
        self.user_4.setObjectName("user_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 90, 441, 111))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        manawindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(manawindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 830, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        manawindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(manawindow)
        self.statusbar.setObjectName("statusbar")
        manawindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(manawindow)
        QtCore.QMetaObject.connectSlotsByName(manawindow)

    def retranslateUi(self, manawindow):
        _translate = QtCore.QCoreApplication.translate
        manawindow.setWindowTitle(_translate("manawindow", "欢迎你，管理员"))
        self.flight.setText(_translate("manawindow", "航班管理"))
        self.manamenu.setText(_translate("manawindow", "用户管理"))
        self.ticket.setText(_translate("manawindow", "机票管理"))
        self.order.setText(_translate("manawindow", "订单管理"))
        self.user_4.setText(_translate("manawindow", "退出"))
        self.label.setText(_translate("manawindow", "欢迎使用航空票务管理系统"))
        self.menu.setTitle(_translate("manawindow", "菜单"))


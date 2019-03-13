# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainmenu(object):
    def setupUi(self, mainmenu):
        mainmenu.setObjectName("mainmenu")
        mainmenu.resize(828, 348)
        self.centralwidget = QtWidgets.QWidget(mainmenu)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 50, 441, 111))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 210, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.register_2 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.register_2.setGeometry(QtCore.QRect(630, 60, 185, 41))
        self.register_2.setObjectName("register_2")
        self.logon = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.logon.setGeometry(QtCore.QRect(630, 150, 185, 41))
        self.logon.setObjectName("logon")
        self.manalogon = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.manalogon.setGeometry(QtCore.QRect(630, 240, 185, 41))
        self.manalogon.setObjectName("manalogon")
        mainmenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainmenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 828, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        mainmenu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainmenu)
        self.statusbar.setObjectName("statusbar")
        mainmenu.setStatusBar(self.statusbar)
        self.actionexit = QtWidgets.QAction(mainmenu)
        self.actionexit.setObjectName("actionexit")
        self.menu.addAction(self.actionexit)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(mainmenu)
        QtCore.QMetaObject.connectSlotsByName(mainmenu)

    def retranslateUi(self, mainmenu):
        _translate = QtCore.QCoreApplication.translate
        mainmenu.setWindowTitle(_translate("mainmenu", "主菜单"))
        self.label.setText(_translate("mainmenu", "欢迎使用航空票务管理系统"))
        self.label_2.setText(_translate("mainmenu", "初次使用请注册"))
        self.register_2.setText(_translate("mainmenu", "用户注册"))
        self.logon.setText(_translate("mainmenu", "用户登录"))
        self.manalogon.setText(_translate("mainmenu", "管理员登录"))
        self.menu.setTitle(_translate("mainmenu", "菜单"))
        self.actionexit.setText(_translate("mainmenu", "exit"))


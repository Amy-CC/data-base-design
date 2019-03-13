# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_usermenu(object):
    def setupUi(self, usermenu):
        usermenu.setObjectName("usermenu")
        usermenu.resize(830, 348)
        self.centralwidget = QtWidgets.QWidget(usermenu)
        self.centralwidget.setObjectName("centralwidget")
        self.order = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.order.setGeometry(QtCore.QRect(580, 60, 185, 41))
        self.order.setObjectName("order")
        self.checkorder = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.checkorder.setGeometry(QtCore.QRect(580, 110, 185, 41))
        self.checkorder.setObjectName("checkorder")
        self.changeinfo = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.changeinfo.setGeometry(QtCore.QRect(580, 10, 185, 41))
        self.changeinfo.setObjectName("changeinfo")
        self.checkflight = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.checkflight.setGeometry(QtCore.QRect(580, 160, 185, 41))
        self.checkflight.setObjectName("checkflight")
        self.cancelorder = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.cancelorder.setGeometry(QtCore.QRect(580, 210, 185, 41))
        self.cancelorder.setObjectName("cancelorder")
        self.exit = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(580, 260, 185, 41))
        self.exit.setObjectName("exit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 80, 441, 111))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 190, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        usermenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(usermenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 830, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        usermenu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(usermenu)
        self.statusbar.setObjectName("statusbar")
        usermenu.setStatusBar(self.statusbar)
        self.actionexit = QtWidgets.QAction(usermenu)
        self.actionexit.setObjectName("actionexit")
        self.menu.addAction(self.actionexit)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(usermenu)
        QtCore.QMetaObject.connectSlotsByName(usermenu)

    def retranslateUi(self, usermenu):
        _translate = QtCore.QCoreApplication.translate
        usermenu.setWindowTitle(_translate("usermenu", "欢迎使用票务管理系统"))
        self.order.setText(_translate("usermenu", "订购机票"))
        self.checkorder.setText(_translate("usermenu", "查看订单"))
        self.changeinfo.setText(_translate("usermenu", "修改用户信息"))
        self.checkflight.setText(_translate("usermenu", "查询航班"))
        self.cancelorder.setText(_translate("usermenu", "退订机票"))
        self.exit.setText(_translate("usermenu", "退出"))
        self.label.setText(_translate("usermenu", "欢迎使用航空票务管理系统"))
        self.label_2.setText(_translate("usermenu", "使用功能前请完善用户信息"))
        self.menu.setTitle(_translate("usermenu", "菜单"))
        self.actionexit.setText(_translate("usermenu", "exit"))


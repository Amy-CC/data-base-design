# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_flight.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_userflight(object):
    def setupUi(self, userflight):
        userflight.setObjectName("userflight")
        userflight.resize(830, 439)
        self.tableView = QtWidgets.QTableView(userflight)
        self.tableView.setGeometry(QtCore.QRect(20, 20, 791, 361))
        self.tableView.setObjectName("tableView")
        self.pushButton_2 = QtWidgets.QPushButton(userflight)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 400, 111, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(userflight)
        QtCore.QMetaObject.connectSlotsByName(userflight)

    def retranslateUi(self, userflight):
        _translate = QtCore.QCoreApplication.translate
        userflight.setWindowTitle(_translate("userflight", "航班信息"))
        self.pushButton_2.setText(_translate("userflight", "OK"))


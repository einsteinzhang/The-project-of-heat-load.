# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qiang13.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow44(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(440, 180, 331, 231))
        self.groupBox.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 8pt \"楷体\";")
        self.groupBox.setObjectName("groupBox")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(40, 110, 221, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.fffq_13 = QtWidgets.QPushButton(self.groupBox)
        self.fffq_13.setGeometry(QtCore.QRect(210, 190, 75, 23))
        self.fffq_13.setObjectName("fff")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(40, 90, 321, 341))
        self.graphicsView.setStyleSheet("border-image: url(:/wuding1/8.png);")
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "保温层δ的厚度(mm)"))
        self.comboBox.setItemText(0, _translate("MainWindow", "75"))
        self.comboBox.setItemText(1, _translate("MainWindow", "65"))
        self.comboBox.setItemText(2, _translate("MainWindow", "55"))
        self.comboBox.setItemText(3, _translate("MainWindow", "40"))
        self.comboBox.setItemText(4, _translate("MainWindow", "30"))
        self.comboBox.setItemText(5, _translate("MainWindow", "25"))
        self.fffq_13.setText(_translate("MainWindow", "完成"))

import wuding_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow44()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


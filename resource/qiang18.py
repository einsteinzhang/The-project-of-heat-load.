# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qiang18.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow49(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(270, 180, 251, 181))
        self.graphicsView.setStyleSheet("border-image: url(:/wuding1/13.png);")
        self.graphicsView.setObjectName("graphicsView")
        self.bububu_3 = QtWidgets.QPushButton(self.centralwidget)
        self.bububu_3.setGeometry(QtCore.QRect(270, 470, 251, 51))
        self.bububu_3.setStyleSheet("color: rgb(242, 52, 255);\n"
"font: 8pt \"楷体\";")
        self.bububu_3.setObjectName("bububu")
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
        self.bububu_3.setText(_translate("MainWindow", "确定"))

import wuding_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow49()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chengshi_1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow9(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.xiajishuju = QtWidgets.QTextEdit(self.centralwidget)
        self.xiajishuju.setGeometry(QtCore.QRect(210, 110, 351, 91))
        self.xiajishuju.setStyleSheet("font: 9pt \"楷体\";\n"
"color: rgb(26, 10, 255);")
        self.xiajishuju.setObjectName("xiajishuju")
        self.xiajishuju_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.xiajishuju_2.setGeometry(QtCore.QRect(210, 250, 351, 91))
        self.xiajishuju_2.setStyleSheet("font: 9pt \"楷体\";\n"
"color: rgb(26, 10, 255);")
        self.xiajishuju_2.setObjectName("xiajishuju_2")
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow9()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


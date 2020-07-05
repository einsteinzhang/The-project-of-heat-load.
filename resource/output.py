# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'output.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.jieguo1 = QtWidgets.QTextEdit(self.centralwidget)
        self.jieguo1.setGeometry(QtCore.QRect(90, 80, 421, 51))
        self.jieguo1.setStyleSheet("font: 9pt \"楷体\";")
        self.jieguo1.setObjectName("jieguo1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 331, 71))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 17pt \"楷体\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(620, 77, 131, 71))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(620, 150, 131, 81))
        self.pushButton_2.setObjectName("pushButton_2")
        self.jieguo2 = QtWidgets.QTextEdit(self.centralwidget)
        self.jieguo2.setGeometry(QtCore.QRect(90, 140, 421, 51))
        self.jieguo2.setObjectName("jieguo2")
        self.jieguo3 = QtWidgets.QTextEdit(self.centralwidget)
        self.jieguo3.setGeometry(QtCore.QRect(90, 200, 421, 51))
        self.jieguo3.setObjectName("jieguo3")
        self.jieguo4 = QtWidgets.QTextEdit(self.centralwidget)
        self.jieguo4.setGeometry(QtCore.QRect(90, 260, 421, 51))
        self.jieguo4.setObjectName("jieguo4")
        self.jieguo5 = QtWidgets.QTextEdit(self.centralwidget)
        self.jieguo5.setGeometry(QtCore.QRect(90, 320, 421, 51))
        self.jieguo5.setObjectName("jieguo5")
        self.jieguo6 = QtWidgets.QTextEdit(self.centralwidget)
        self.jieguo6.setGeometry(QtCore.QRect(90, 440, 421, 51))
        self.jieguo6.setObjectName("jieguo6")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(620, 230, 131, 81))
        self.pushButton_3.setObjectName("pushButton_3")
        self.jieguo6_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.jieguo6_2.setGeometry(QtCore.QRect(90, 380, 421, 51))
        self.jieguo6_2.setObjectName("jieguo6_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuSave = QtWidgets.QMenu(self.menubar)
        self.menuSave.setObjectName("menuSave")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionexcel = QtWidgets.QAction(MainWindow)
        self.actionexcel.setObjectName("actionexcel")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionhelp = QtWidgets.QAction(MainWindow)
        self.actionhelp.setObjectName("actionhelp")
        self.menuSave.addAction(self.actionexcel)
        self.menuSave.addAction(self.actionClose)
        self.menu.addAction(self.actionhelp)
        self.menubar.addAction(self.menuSave.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "夏季冷负荷计算结果："))
        self.pushButton.setText(_translate("MainWindow", "计算结果显示"))
        self.pushButton_2.setText(_translate("MainWindow", "数据清空"))
        self.pushButton_3.setText(_translate("MainWindow", "显示图像"))
        self.menuSave.setTitle(_translate("MainWindow", "文件"))
        self.menu.setTitle(_translate("MainWindow", "帮助"))
        self.actionexcel.setText(_translate("MainWindow", "Save"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionhelp.setText(_translate("MainWindow", "help"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

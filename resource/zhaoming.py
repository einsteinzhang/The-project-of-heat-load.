# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zhaoming.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow5(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.queding_deng = QtWidgets.QPushButton(self.centralwidget)
        self.queding_deng.setGeometry(QtCore.QRect(350, 300, 111, 71))
        self.queding_deng.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 180, 271, 20))
        self.label.setStyleSheet("font: 6pt \"楷体\";")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(520, 180, 100, 20))
        self.lineEdit.setMinimumSize(QtCore.QSize(100, 20))
        self.lineEdit.setMaximumSize(QtCore.QSize(100, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(200, 230, 500, 40))
        self.comboBox.setMinimumSize(QtCore.QSize(500, 40))
        self.comboBox.setMaximumSize(QtCore.QSize(500, 40))
        self.comboBox.setStyleSheet("font: 7pt \"楷体\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
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
        self.queding_deng.setText(_translate("MainWindow", "确定"))
        self.label.setText(_translate("MainWindow", "照明设备安装功率N（W）："))
        self.comboBox.setItemText(0, _translate("MainWindow", "明装白炽灯"))
        self.comboBox.setItemText(1, _translate("MainWindow", "荧光灯（整流器在空调房间内部）"))
        self.comboBox.setItemText(2, _translate("MainWindow", "荧光灯（整流器在吊顶内，且灯罩有小孔）"))
        self.comboBox.setItemText(3, _translate("MainWindow", "荧光灯（整流器在吊顶内，且灯罩无小孔）"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow5()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


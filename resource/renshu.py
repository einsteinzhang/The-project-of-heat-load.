# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'renshu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow4(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.queding_r = QtWidgets.QPushButton(self.centralwidget)
        self.queding_r.setGeometry(QtCore.QRect(360, 450, 121, 41))
        self.queding_r.setObjectName("queding_r")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 110, 221, 20))
        self.label.setStyleSheet("font: 8pt \"楷体\";")
        self.label.setObjectName("label")
        self.renshu_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.renshu_1.setGeometry(QtCore.QRect(380, 110, 351, 20))
        self.renshu_1.setObjectName("renshu_1")
        self.changsuo_com = QtWidgets.QComboBox(self.centralwidget)
        self.changsuo_com.setGeometry(QtCore.QRect(380, 210, 351, 22))
        self.changsuo_com.setStyleSheet("font: 8pt \"Arial\";\n"
"font: 8pt \"楷体\";")
        self.changsuo_com.setObjectName("changsuo_com")
        self.changsuo_com.addItem("")
        self.changsuo_com.addItem("")
        self.changsuo_com.addItem("")
        self.changsuo_com.addItem("")
        self.changsuo_com.addItem("")
        self.changsuo_com.addItem("")
        self.changsuo_com.addItem("")
        self.changsuo_com.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 220, 141, 16))
        self.label_2.setStyleSheet("font: 8pt \"楷体\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 330, 111, 20))
        self.label_3.setStyleSheet("font: 8pt \"楷体\";")
        self.label_3.setObjectName("label_3")
        self.laoqiang_com = QtWidgets.QComboBox(self.centralwidget)
        self.laoqiang_com.setGeometry(QtCore.QRect(380, 330, 351, 22))
        self.laoqiang_com.setStyleSheet("font: 8pt \"楷体\";")
        self.laoqiang_com.setObjectName("laoqiang_com")
        self.laoqiang_com.addItem("")
        self.laoqiang_com.addItem("")
        self.laoqiang_com.addItem("")
        self.laoqiang_com.addItem("")
        self.laoqiang_com.addItem("")
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
        self.queding_r.setText(_translate("MainWindow", "确定"))
        self.label.setText(_translate("MainWindow", "房间的人数："))
        self.changsuo_com.setItemText(0, _translate("MainWindow", "影剧院"))
        self.changsuo_com.setItemText(1, _translate("MainWindow", "旅店"))
        self.changsuo_com.setItemText(2, _translate("MainWindow", "铸造车间"))
        self.changsuo_com.setItemText(3, _translate("MainWindow", "图书馆阅览室"))
        self.changsuo_com.setItemText(4, _translate("MainWindow", "炼钢车间"))
        self.changsuo_com.setItemText(5, _translate("MainWindow", "百货商场（售货）"))
        self.changsuo_com.setItemText(6, _translate("MainWindow", "体育馆"))
        self.changsuo_com.setItemText(7, _translate("MainWindow", "纺织厂"))
        self.label_2.setText(_translate("MainWindow", "工作场所的选择："))
        self.label_3.setText(_translate("MainWindow", "人员劳动强度的选择："))
        self.laoqiang_com.setItemText(0, _translate("MainWindow", "静坐"))
        self.laoqiang_com.setItemText(1, _translate("MainWindow", "极轻等劳动"))
        self.laoqiang_com.setItemText(2, _translate("MainWindow", "轻等劳动"))
        self.laoqiang_com.setItemText(3, _translate("MainWindow", "中等劳动"))
        self.laoqiang_com.setItemText(4, _translate("MainWindow", "重度劳动"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow4()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chuangkou.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow7(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.queding_chuangk = QtWidgets.QPushButton(self.centralwidget)
        self.queding_chuangk.setGeometry(QtCore.QRect(570, 460, 111, 91))
        self.queding_chuangk.setStyleSheet("\n"
"QPushButton{\n"
"color:white;\n"
"font: 8pt \"楷体\";\n"
"border-radius:8px;\n"
"background-color:rgb(33, 174, 250);\n"
"spacing:20px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(72,203,250);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(85,85,255);\n"
"}")
        self.queding_chuangk.setObjectName("queding_chuangk")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 250, 441, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(45)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(250, 0))
        self.label_5.setMaximumSize(QtCore.QSize(250, 16777215))
        self.label_5.setStyleSheet("font: 9pt \"楷体\";\n"
"color: rgb(255, 26, 255);")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.chuangw = QtWidgets.QComboBox(self.layoutWidget)
        self.chuangw.setObjectName("chuangw")
        self.chuangw.addItem("")
        self.chuangw.addItem("")
        self.chuangw.addItem("")
        self.chuangw.addItem("")
        self.chuangw.addItem("")
        self.chuangw.addItem("")
        self.chuangw.addItem("")
        self.chuangw.addItem("")
        self.chuangw.addItem("")
        self.chuangw.addItem("")
        self.chuangw.addItem("")
        self.chuangw.addItem("")
        self.chuangw.addItem("")
        self.chuangw.addItem("")
        self.chuangw.addItem("")
        self.chuangw.addItem("")
        self.horizontalLayout_5.addWidget(self.chuangw)
        self.queding_ds = QtWidgets.QPushButton(self.centralwidget)
        self.queding_ds.setGeometry(QtCore.QRect(540, 40, 151, 41))
        self.queding_ds.setStyleSheet("\n"
"QPushButton{\n"
"color:white;\n"
"font: 8pt \"楷体\";\n"
"border-radius:8px;\n"
"background-color:rgb(33, 174, 250);\n"
"spacing:20px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(72,203,250);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(85,85,255);\n"
"}")
        self.queding_ds.setObjectName("queding_ds")
        self.queding_ck = QtWidgets.QPushButton(self.centralwidget)
        self.queding_ck.setGeometry(QtCore.QRect(540, 160, 151, 41))
        self.queding_ck.setStyleSheet("\n"
"QPushButton{\n"
"color:white;\n"
"font: 8pt \"楷体\";\n"
"border-radius:8px;\n"
"background-color:rgb(33, 174, 250);\n"
"spacing:20px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(72,203,250);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(85,85,255);\n"
"}")
        self.queding_ck.setObjectName("queding_ck")
        self.queding_cw = QtWidgets.QPushButton(self.centralwidget)
        self.queding_cw.setGeometry(QtCore.QRect(540, 270, 151, 41))
        self.queding_cw.setStyleSheet("\n"
"QPushButton{\n"
"color:white;\n"
"font: 8pt \"楷体\";\n"
"border-radius:8px;\n"
"background-color:rgb(33, 174, 250);\n"
"spacing:20px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(72,203,250);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(85,85,255);\n"
"}")
        self.queding_cw.setObjectName("queding_cw")
        self.queding_cn = QtWidgets.QPushButton(self.centralwidget)
        self.queding_cn.setGeometry(QtCore.QRect(540, 380, 151, 41))
        self.queding_cn.setStyleSheet("\n"
"QPushButton{\n"
"color:white;\n"
"font: 8pt \"楷体\";\n"
"border-radius:8px;\n"
"background-color:rgb(33, 174, 250);\n"
"spacing:20px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(72,203,250);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(85,85,255);\n"
"}")
        self.queding_cn.setObjectName("queding_cn")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 140, 441, 81))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(60)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setStyleSheet("font: 9pt \"楷体\";\n"
"color: rgb(255, 26, 255);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.chuangk_com = QtWidgets.QComboBox(self.widget)
        self.chuangk_com.setObjectName("chuangk_com")
        self.chuangk_com.addItem("")
        self.chuangk_com.addItem("")
        self.chuangk_com.addItem("")
        self.chuangk_com.addItem("")
        self.horizontalLayout_2.addWidget(self.chuangk_com)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(20, 360, 441, 81))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(45)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setMinimumSize(QtCore.QSize(250, 0))
        self.label_3.setMaximumSize(QtCore.QSize(250, 16777215))
        self.label_3.setStyleSheet("font: 9pt \"楷体\";\n"
"color: rgb(255, 26, 255);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.chuangn = QtWidgets.QComboBox(self.widget1)
        self.chuangn.setObjectName("chuangn")
        self.chuangn.addItem("")
        self.chuangn.addItem("")
        self.chuangn.addItem("")
        self.chuangn.addItem("")
        self.chuangn.addItem("")
        self.chuangn.addItem("")
        self.chuangn.addItem("")
        self.chuangn.addItem("")
        self.chuangn.addItem("")
        self.chuangn.addItem("")
        self.horizontalLayout_3.addWidget(self.chuangn)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(20, 10, 441, 101))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout.setSpacing(60)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget2)
        self.label.setStyleSheet("font: 9pt \"楷体\";\n"
"color: rgb(255, 26, 255);")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.dsbl_com = QtWidgets.QComboBox(self.widget2)
        self.dsbl_com.setObjectName("dsbl_com")
        self.dsbl_com.addItem("")
        self.dsbl_com.addItem("")
        self.horizontalLayout.addWidget(self.dsbl_com)
        self.widget3 = QtWidgets.QWidget(self.centralwidget)
        self.widget3.setGeometry(QtCore.QRect(20, 460, 441, 91))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_4.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.widget3)
        self.label_4.setStyleSheet("font: 9pt \"楷体\";\n"
"color: rgb(255, 26, 255);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.chuangmian = QtWidgets.QLineEdit(self.widget3)
        self.chuangmian.setObjectName("chuangmian")
        self.horizontalLayout_4.addWidget(self.chuangmian)
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
        self.queding_chuangk.setText(_translate("MainWindow", "确定"))
        self.label_5.setText(_translate("MainWindow", "窗外表面换热系数，W/（m^2*℃）："))
        self.chuangw.setItemText(0, _translate("MainWindow", "11.6"))
        self.chuangw.setItemText(1, _translate("MainWindow", "12.8"))
        self.chuangw.setItemText(2, _translate("MainWindow", "14.0"))
        self.chuangw.setItemText(3, _translate("MainWindow", "15.1"))
        self.chuangw.setItemText(4, _translate("MainWindow", "16.3"))
        self.chuangw.setItemText(5, _translate("MainWindow", "17.5"))
        self.chuangw.setItemText(6, _translate("MainWindow", "18.6"))
        self.chuangw.setItemText(7, _translate("MainWindow", "19.8"))
        self.chuangw.setItemText(8, _translate("MainWindow", "20.9"))
        self.chuangw.setItemText(9, _translate("MainWindow", "22.1"))
        self.chuangw.setItemText(10, _translate("MainWindow", "23.3"))
        self.chuangw.setItemText(11, _translate("MainWindow", "24.4"))
        self.chuangw.setItemText(12, _translate("MainWindow", "25.6"))
        self.chuangw.setItemText(13, _translate("MainWindow", "26.7"))
        self.chuangw.setItemText(14, _translate("MainWindow", "27.9"))
        self.chuangw.setItemText(15, _translate("MainWindow", "29.1"))
        self.queding_ds.setText(_translate("MainWindow", "填写完毕"))
        self.queding_ck.setText(_translate("MainWindow", "填写完毕"))
        self.queding_cw.setText(_translate("MainWindow", "填写完毕"))
        self.queding_cn.setText(_translate("MainWindow", "填写完毕"))
        self.label_2.setText(_translate("MainWindow", "窗框类型："))
        self.chuangk_com.setItemText(0, _translate("MainWindow", "全部金属"))
        self.chuangk_com.setItemText(1, _translate("MainWindow", "木窗框（80%玻璃）"))
        self.chuangk_com.setItemText(2, _translate("MainWindow", "木窗框（60%玻璃）"))
        self.chuangk_com.setItemText(3, _translate("MainWindow", "金属窗框（80%玻璃）"))
        self.label_3.setText(_translate("MainWindow", "窗内表面换热系数，W/（m^2*℃）："))
        self.chuangn.setItemText(0, _translate("MainWindow", "5.8"))
        self.chuangn.setItemText(1, _translate("MainWindow", "6.4"))
        self.chuangn.setItemText(2, _translate("MainWindow", "7.0"))
        self.chuangn.setItemText(3, _translate("MainWindow", "7.6"))
        self.chuangn.setItemText(4, _translate("MainWindow", "8.2"))
        self.chuangn.setItemText(5, _translate("MainWindow", "8.7"))
        self.chuangn.setItemText(6, _translate("MainWindow", "9.4"))
        self.chuangn.setItemText(7, _translate("MainWindow", "9.9"))
        self.chuangn.setItemText(8, _translate("MainWindow", "10.5"))
        self.chuangn.setItemText(9, _translate("MainWindow", "11.1"))
        self.label.setText(_translate("MainWindow", "单/双玻璃窗："))
        self.dsbl_com.setItemText(0, _translate("MainWindow", "单层窗玻璃"))
        self.dsbl_com.setItemText(1, _translate("MainWindow", "双层窗玻璃"))
        self.label_4.setText(_translate("MainWindow", "窗口面积（m^2）:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow7()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


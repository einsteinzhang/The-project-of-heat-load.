# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fangjian.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow3(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 700)
        MainWindow.setMinimumSize(QtCore.QSize(900, 700))
        MainWindow.setMaximumSize(QtCore.QSize(900, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(70, 220, 741, 131))
        self.groupBox.setStyleSheet("font: 12pt \"楷体\";\n"
"color: rgb(225, 53, 255);")
        self.groupBox.setObjectName("groupBox")
        self.qiangmian = QtWidgets.QComboBox(self.groupBox)
        self.qiangmian.setGeometry(QtCore.QRect(140, 30, 501, 31))
        self.qiangmian.setObjectName("qiangmian")
        self.qiangmian.addItem("")
        self.qiangmian.addItem("")
        self.qiangmian.addItem("")
        self.qiangmian.addItem("")
        self.qiangmian.addItem("")
        self.qiangmian.addItem("")
        self.qiangmian.addItem("")
        self.qiangmian.addItem("")
        self.qiangmian.addItem("")
        self.qiangmian.addItem("")
        self.qiangmian.addItem("")
        self.qiangmian.addItem("")
        self.qinagwaibianmian = QtWidgets.QPushButton(self.groupBox)
        self.qinagwaibianmian.setEnabled(False)
        self.qinagwaibianmian.setGeometry(QtCore.QRect(90, 80, 581, 41))
        self.qinagwaibianmian.setStyleSheet("QPushButton{\n"
"color:white;\n"
"font: 16pt \"楷体\";\n"
"border-radius:8px;\n"
"background-color:rgb(33, 174, 250);\n"
"spacing:20px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(72,203,250);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(85,85,255);\n"
"}\n"
"QPushButton:checked{\n"
"background-color: rgb(11, 15, 255);\n"
"}\n"
"QPushButton:disabled{\n"
"\n"
"    background-color: rgb(165, 165, 165);\n"
"    color: rgb(11, 11, 11);\n"
"}")
        self.qinagwaibianmian.setCheckable(True)
        self.qinagwaibianmian.setObjectName("qinagwaibianmian")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(70, 360, 741, 131))
        self.groupBox_2.setStyleSheet("font: 12pt \"楷体\";\n"
"color: rgb(225, 53, 255);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.qiangmian_2 = QtWidgets.QComboBox(self.groupBox_2)
        self.qiangmian_2.setGeometry(QtCore.QRect(140, 30, 501, 31))
        self.qiangmian_2.setObjectName("qiangmian_2")
        self.qiangmian_2.addItem("")
        self.qiangmian_2.addItem("")
        self.qiangmian_2.addItem("")
        self.qiangmian_2.addItem("")
        self.qiangmian_2.addItem("")
        self.qiangmian_2.addItem("")
        self.qiangmian_2.addItem("")
        self.qiangmian_2.addItem("")
        self.wudingwaibm = QtWidgets.QPushButton(self.groupBox_2)
        self.wudingwaibm.setEnabled(False)
        self.wudingwaibm.setGeometry(QtCore.QRect(80, 80, 601, 41))
        self.wudingwaibm.setStyleSheet("QPushButton{\n"
"color:white;\n"
"font: 16pt \"楷体\";\n"
"border-radius:8px;\n"
"background-color:rgb(33, 174, 250);\n"
"spacing:20px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(72,203,250);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(85,85,255);\n"
"}\n"
"QPushButton:disabled{\n"
"\n"
"    background-color: rgb(165, 165, 165);\n"
"    color: rgb(11, 11, 11);\n"
"}\n"
"QPushButton:checked{\n"
"background-color: rgb(11, 15, 255);\n"
"}")
        self.wudingwaibm.setCheckable(True)
        self.wudingwaibm.setObjectName("wudingwaibm")
        self.mian_dong = QtWidgets.QLineEdit(self.centralwidget)
        self.mian_dong.setGeometry(QtCore.QRect(320, 10, 471, 20))
        self.mian_dong.setObjectName("mian_dong")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 261, 20))
        self.label.setStyleSheet("font: 12pt \"楷体\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 40, 261, 20))
        self.label_2.setStyleSheet("font: 12pt \"楷体\";")
        self.label_2.setObjectName("label_2")
        self.mian_xi = QtWidgets.QLineEdit(self.centralwidget)
        self.mian_xi.setGeometry(QtCore.QRect(320, 40, 471, 20))
        self.mian_xi.setObjectName("mian_xi")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 100, 291, 21))
        self.label_3.setStyleSheet("font: 12pt \"楷体\";")
        self.label_3.setObjectName("label_3")
        self.mian_bei = QtWidgets.QLineEdit(self.centralwidget)
        self.mian_bei.setGeometry(QtCore.QRect(320, 100, 471, 20))
        self.mian_bei.setObjectName("mian_bei")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 70, 291, 21))
        self.label_4.setStyleSheet("font: 12pt \"楷体\";")
        self.label_4.setObjectName("label_4")
        self.mian_nan = QtWidgets.QLineEdit(self.centralwidget)
        self.mian_nan.setGeometry(QtCore.QRect(320, 70, 471, 20))
        self.mian_nan.setObjectName("mian_nan")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 130, 291, 21))
        self.label_5.setStyleSheet("font: 12pt \"楷体\";")
        self.label_5.setObjectName("label_5")
        self.mian_wu = QtWidgets.QLineEdit(self.centralwidget)
        self.mian_wu.setGeometry(QtCore.QRect(320, 130, 471, 20))
        self.mian_wu.setObjectName("mian_wu")
        self.qiangtimianji = QtWidgets.QPushButton(self.centralwidget)
        self.qiangtimianji.setEnabled(False)
        self.qiangtimianji.setGeometry(QtCore.QRect(40, 160, 811, 51))
        self.qiangtimianji.setStyleSheet("QPushButton{\n"
"color:white;\n"
"font: 16pt \"楷体\";\n"
"border-radius:8px;\n"
"background-color:rgb(33, 174, 250);\n"
"spacing:20px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(72,203,250);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(85,85,255);\n"
"}\n"
"QPushButton:checked{\n"
"background-color: rgb(11, 15, 255);\n"
"}\n"
"QPushButton:disabled{\n"
"\n"
"    background-color: rgb(165, 165, 165);\n"
"    color: rgb(11, 11, 11);\n"
"}")
        self.qiangtimianji.setCheckable(True)
        self.qiangtimianji.setObjectName("qiangtimianji")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(70, 500, 741, 131))
        self.groupBox_3.setStyleSheet("color:rgb(218, 29, 255);\n"
"font: 12pt \"楷体\";")
        self.groupBox_3.setObjectName("groupBox_3")
        self.tainanle = QtWidgets.QPushButton(self.groupBox_3)
        self.tainanle.setEnabled(False)
        self.tainanle.setGeometry(QtCore.QRect(140, 30, 501, 41))
        self.tainanle.setStyleSheet("QPushButton{\n"
"\n"
"font: 16pt \"楷体\";\n"
"border-radius:8px;\n"
"background-color:rgb(33, 174, 250);\n"
"spacing:20px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(72,203,250);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(85,85,255);\n"
"}\n"
"QPushButton:checked{\n"
"background-color: rgb(11, 15, 255);\n"
"}\n"
"QPushButton:disabled{\n"
"\n"
"    background-color: rgb(165, 165, 165);\n"
"    color: rgb(11, 11, 11);\n"
"}")
        self.tainanle.setCheckable(True)
        self.tainanle.setObjectName("tainanle")
        self.zuihzonglea = QtWidgets.QPushButton(self.groupBox_3)
        self.zuihzonglea.setEnabled(False)
        self.zuihzonglea.setGeometry(QtCore.QRect(80, 80, 601, 41))
        self.zuihzonglea.setStyleSheet("QPushButton{\n"
"color:white;\n"
"font: 16pt \"楷体\";\n"
"border-radius:8px;\n"
"background-color:rgb(33, 174, 250);\n"
"spacing:20px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(72,203,250);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(85,85,255);\n"
"}\n"
"QPushButton:disabled{\n"
"\n"
"    background-color: rgb(165, 165, 165);\n"
"    color: rgb(11, 11, 11);\n"
"}")
        self.zuihzonglea.setObjectName("zuihzonglea")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 26))
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
        self.groupBox.setTitle(_translate("MainWindow", "墙面结构外表面"))
        self.qiangmian.setItemText(0, _translate("MainWindow", "无"))
        self.qiangmian.setItemText(1, _translate("MainWindow", "金属：白铁屋面(灰黑色)"))
        self.qiangmian.setItemText(2, _translate("MainWindow", "金属：抛光铝反射板(浅色)"))
        self.qiangmian.setItemText(3, _translate("MainWindow", "粉刷：拉毛水泥墙面(灰/米黄色)"))
        self.qiangmian.setItemText(4, _translate("MainWindow", "粉刷：石灰粉刷(白色)"))
        self.qiangmian.setItemText(5, _translate("MainWindow", "粉刷：陶石子墙面(浅灰色)"))
        self.qiangmian.setItemText(6, _translate("MainWindow", "粉刷：水泥粉刷墙面(浅蓝色)"))
        self.qiangmian.setItemText(7, _translate("MainWindow", "粉刷：砂石粉刷墙(深色)"))
        self.qiangmian.setItemText(8, _translate("MainWindow", "粉刷：浅色饰面砖(浅黄、浅绿色)"))
        self.qiangmian.setItemText(9, _translate("MainWindow", "红砖墙(红色)旧"))
        self.qiangmian.setItemText(10, _translate("MainWindow", "硅酸盐砖墙(青灰色)不光滑"))
        self.qiangmian.setItemText(11, _translate("MainWindow", "混凝土块墙(灰色)"))
        self.qinagwaibianmian.setText(_translate("MainWindow", "确认"))
        self.groupBox_2.setTitle(_translate("MainWindow", "屋面结构外表面"))
        self.qiangmian_2.setItemText(0, _translate("MainWindow", "无"))
        self.qiangmian_2.setItemText(1, _translate("MainWindow", "红瓦屋面(红色)旧"))
        self.qiangmian_2.setItemText(2, _translate("MainWindow", "红褐色瓦屋面(红褐色)旧"))
        self.qiangmian_2.setItemText(3, _translate("MainWindow", "灰瓦屋面(浅灰色)旧"))
        self.qiangmian_2.setItemText(4, _translate("MainWindow", "石板瓦(银灰色)旧"))
        self.qiangmian_2.setItemText(5, _translate("MainWindow", "水泥屋面(青灰色)旧"))
        self.qiangmian_2.setItemText(6, _translate("MainWindow", "浅色油毛毡(浅黑色)粗糙，新"))
        self.qiangmian_2.setItemText(7, _translate("MainWindow", "黑色油毛毡(深黑色)粗糙，新"))
        self.wudingwaibm.setText(_translate("MainWindow", "确认"))
        self.label.setText(_translate("MainWindow", "东墙体面积(m^2)(没有写0):"))
        self.label_2.setText(_translate("MainWindow", "西墙体面积(m^2)(没有写0):"))
        self.label_3.setText(_translate("MainWindow", "北墙体面积(m^2)(没有写0):"))
        self.label_4.setText(_translate("MainWindow", "南墙体面积(m^2)(没有写0):"))
        self.label_5.setText(_translate("MainWindow", "屋顶面积(m^2)(没有写0):"))
        self.qiangtimianji.setText(_translate("MainWindow", "面积输入完毕"))
        self.groupBox_3.setTitle(_translate("MainWindow", "外墙和屋顶结构"))
        self.tainanle.setText(_translate("MainWindow", "外墙和屋顶结构图例"))
        self.zuihzonglea.setText(_translate("MainWindow", "完成"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow3()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'renshu_xin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form45(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setMinimumSize(QtCore.QSize(800, 600))
        Form.setMaximumSize(QtCore.QSize(800, 600))
        Form.setStyleSheet("QWidget#Form {\n"
"    border-image: url(:/ll/renshu.png);\n"
"}")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 350, 291, 41))
        self.label_3.setStyleSheet("font: 18pt \"楷体\";\n"
"color:rgb(9, 24, 2);")
        self.label_3.setObjectName("label_3")
        self.laoqiang_com = QtWidgets.QComboBox(Form)
        self.laoqiang_com.setGeometry(QtCore.QRect(350, 360, 351, 31))
        self.laoqiang_com.setStyleSheet("font: 16pt \"楷体\";")
        self.laoqiang_com.setObjectName("laoqiang_com")
        self.laoqiang_com.addItem("")
        self.laoqiang_com.addItem("")
        self.laoqiang_com.addItem("")
        self.laoqiang_com.addItem("")
        self.laoqiang_com.addItem("")
        self.changsuo_com = QtWidgets.QComboBox(Form)
        self.changsuo_com.setGeometry(QtCore.QRect(340, 230, 351, 41))
        self.changsuo_com.setStyleSheet("font: 16pt \"楷体\";")
        self.changsuo_com.setObjectName("changsuo_com")
        self.changsuo_com.addItem("")
        self.changsuo_com.addItem("")
        self.changsuo_com.addItem("")
        self.changsuo_com.addItem("")
        self.changsuo_com.addItem("")
        self.changsuo_com.addItem("")
        self.changsuo_com.addItem("")
        self.changsuo_com.addItem("")
        self.queding_r = QtWidgets.QPushButton(Form)
        self.queding_r.setGeometry(QtCore.QRect(330, 480, 121, 41))
        self.queding_r.setStyleSheet("QPushButton{\n"
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
        self.queding_r.setObjectName("queding_r")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 230, 271, 31))
        self.label_2.setStyleSheet("font: 18pt \"楷体\";\n"
"color:rgb(9, 24, 2);")
        self.label_2.setObjectName("label_2")
        self.renshu_1 = QtWidgets.QLineEdit(Form)
        self.renshu_1.setGeometry(QtCore.QRect(350, 140, 351, 20))
        self.renshu_1.setStyleSheet("background-color: transparent;\n"
"color: rgb(10, 55, 255);\n"
"border:none;\n"
"font: 18pt \"楷体\";\n"
"border-bottom:1px solid lightgreen;")
        self.renshu_1.setObjectName("renshu_1")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 120, 221, 51))
        self.label.setStyleSheet("font: 18pt \"楷体\";\n"
"color:rgb(9, 24, 2);")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "人员劳动强度的选择："))
        self.laoqiang_com.setItemText(0, _translate("Form", "静坐"))
        self.laoqiang_com.setItemText(1, _translate("Form", "极轻等劳动"))
        self.laoqiang_com.setItemText(2, _translate("Form", "轻等劳动"))
        self.laoqiang_com.setItemText(3, _translate("Form", "中等劳动"))
        self.laoqiang_com.setItemText(4, _translate("Form", "重度劳动"))
        self.changsuo_com.setItemText(0, _translate("Form", "影剧院"))
        self.changsuo_com.setItemText(1, _translate("Form", "旅店"))
        self.changsuo_com.setItemText(2, _translate("Form", "铸造车间"))
        self.changsuo_com.setItemText(3, _translate("Form", "图书馆阅览室"))
        self.changsuo_com.setItemText(4, _translate("Form", "炼钢车间"))
        self.changsuo_com.setItemText(5, _translate("Form", "百货商场（售货）"))
        self.changsuo_com.setItemText(6, _translate("Form", "体育馆"))
        self.changsuo_com.setItemText(7, _translate("Form", "纺织厂"))
        self.queding_r.setText(_translate("Form", "确定"))
        self.label_2.setText(_translate("Form", "工作场所的选择："))
        self.label.setText(_translate("Form", "房间的人数："))
import wuding_rc
import xin_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form45()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

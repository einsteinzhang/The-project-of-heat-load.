# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zhaoming_xin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form5(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setMinimumSize(QtCore.QSize(800, 600))
        Form.setMaximumSize(QtCore.QSize(800, 600))
        Form.setStyleSheet("QWidget#Form {\n"
"    border-image: url(:/ll/dengguang.png);\n"
"}")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(490, 170, 100, 40))
        self.lineEdit.setMinimumSize(QtCore.QSize(100, 40))
        self.lineEdit.setMaximumSize(QtCore.QSize(100, 40))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 169, 371, 41))
        self.label.setStyleSheet("font: 18pt \"楷体\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(330, 350, 111, 71))
        self.pushButton.setStyleSheet("QPushButton{\n"
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
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(50, 250, 700, 40))
        self.comboBox.setMinimumSize(QtCore.QSize(700, 40))
        self.comboBox.setMaximumSize(QtCore.QSize(700, 40))
        self.comboBox.setStyleSheet("font: 16pt \"楷体\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(120, 119, 371, 41))
        self.label_2.setStyleSheet("font: 18pt \"楷体\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(490, 120, 100, 40))
        self.lineEdit_2.setMinimumSize(QtCore.QSize(100, 40))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(100, 40))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "照明设备安装功率N（KW）："))
        self.pushButton.setText(_translate("Form", "确定"))
        self.comboBox.setItemText(0, _translate("Form", "明装白炽灯"))
        self.comboBox.setItemText(1, _translate("Form", "荧光灯（整流器在空调房间内部）"))
        self.comboBox.setItemText(2, _translate("Form", "荧光灯（整流器在吊顶内，且灯罩有小孔）"))
        self.comboBox.setItemText(3, _translate("Form", "荧光灯（整流器在吊顶内，且灯罩无小孔）"))
        self.label_2.setText(_translate("Form", "照明设备的个数："))
import xin_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form5()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

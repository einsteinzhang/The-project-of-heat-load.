# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chuangrishe.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form88(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(794, 616)
        Form.setStyleSheet("QWidget#Form{\n"
"    \n"
"    border-image: url(:/rishe/rishe.png);\n"
"}")
        self.chaung_gui = QtWidgets.QPushButton(Form)
        self.chaung_gui.setEnabled(False)
        self.chaung_gui.setGeometry(QtCore.QRect(680, 340, 75, 23))
        self.chaung_gui.setStyleSheet("QPushButton{\n"
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
        self.chaung_gui.setObjectName("chaung_gui")
        self.wancheng = QtWidgets.QPushButton(Form)
        self.wancheng.setEnabled(False)
        self.wancheng.setGeometry(QtCore.QRect(150, 522, 491, 51))
        self.wancheng.setStyleSheet("QPushButton{\n"
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
        self.wancheng.setObjectName("wancheng")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(90, 310, 591, 71))
        self.groupBox.setStyleSheet("font: 10pt \"楷体\" Bold-75;\n"
"color: rgb(255, 56, 7);")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(70, 40, 141, 31))
        self.label.setStyleSheet("font: 10pt \"楷体\";")
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(220, 40, 351, 22))
        self.comboBox.setStyleSheet("font: 10pt \"楷体\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(160, 230, 471, 51))
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
"QPushButton:checked{\n"
"background-color: rgb(11, 15, 255);\n"
"}\n"
"QPushButton:disabled{\n"
"\n"
"    background-color: rgb(165, 165, 165);\n"
"    color: rgb(11, 11, 11);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.chuang_bo = QtWidgets.QPushButton(Form)
        self.chuang_bo.setEnabled(False)
        self.chuang_bo.setGeometry(QtCore.QRect(680, 410, 75, 23))
        self.chuang_bo.setStyleSheet("QPushButton{\n"
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
        self.chuang_bo.setObjectName("chuang_bo")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(380, 40, 271, 191))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.bei = QtWidgets.QLineEdit(self.layoutWidget)
        self.bei.setMinimumSize(QtCore.QSize(0, 20))
        self.bei.setMaximumSize(QtCore.QSize(16777215, 20))
        self.bei.setObjectName("bei")
        self.verticalLayout_2.addWidget(self.bei)
        self.xi = QtWidgets.QLineEdit(self.layoutWidget)
        self.xi.setMinimumSize(QtCore.QSize(0, 20))
        self.xi.setMaximumSize(QtCore.QSize(16777215, 20))
        self.xi.setObjectName("xi")
        self.verticalLayout_2.addWidget(self.xi)
        self.dong = QtWidgets.QLineEdit(self.layoutWidget)
        self.dong.setMinimumSize(QtCore.QSize(0, 20))
        self.dong.setMaximumSize(QtCore.QSize(16777215, 20))
        self.dong.setObjectName("dong")
        self.verticalLayout_2.addWidget(self.dong)
        self.nan = QtWidgets.QLineEdit(self.layoutWidget)
        self.nan.setMinimumSize(QtCore.QSize(0, 20))
        self.nan.setMaximumSize(QtCore.QSize(16777215, 20))
        self.nan.setObjectName("nan")
        self.verticalLayout_2.addWidget(self.nan)
        self.shuiping = QtWidgets.QLineEdit(self.layoutWidget)
        self.shuiping.setMinimumSize(QtCore.QSize(0, 20))
        self.shuiping.setMaximumSize(QtCore.QSize(16777215, 20))
        self.shuiping.setObjectName("shuiping")
        self.verticalLayout_2.addWidget(self.shuiping)
        self.layoutWidget_2 = QtWidgets.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(130, 40, 251, 191))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_5.setStyleSheet("font: 10pt \"楷体\";\n"
"color: rgb(215, 15, 255);")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_7.setStyleSheet("font: 10pt \"楷体\";\n"
"color: rgb(215, 15, 255);")
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_8.setStyleSheet("font: 10pt \"楷体\";\n"
"color: rgb(215, 15, 255);")
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_6.setStyleSheet("font: 10pt \"楷体\";\n"
"color: rgb(215, 15, 255);")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_10.setStyleSheet("font: 10pt \"楷体\";\n"
"color: rgb(215, 15, 255);")
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(90, 380, 591, 71))
        self.groupBox_2.setStyleSheet("font: 10pt \"楷体\" Bold-75;\n"
"color: rgb(255, 56, 7);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(70, 30, 141, 31))
        self.label_2.setStyleSheet("font: 10pt \"楷体\";")
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_2.setGeometry(QtCore.QRect(220, 40, 351, 22))
        self.comboBox_2.setStyleSheet("font: 10pt \"楷体\";")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(90, 450, 591, 71))
        self.groupBox_3.setStyleSheet("font: 10pt \"楷体\" Bold-75;\n"
"color: rgb(255, 56, 7);")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(70, 30, 141, 31))
        self.label_3.setStyleSheet("font: 10pt \"楷体\";")
        self.label_3.setObjectName("label_3")
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_3.setGeometry(QtCore.QRect(220, 40, 351, 22))
        self.comboBox_3.setStyleSheet("font: 10pt \"楷体\";")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.chuang_zhe = QtWidgets.QPushButton(Form)
        self.chuang_zhe.setEnabled(False)
        self.chuang_zhe.setGeometry(QtCore.QRect(680, 480, 75, 23))
        self.chuang_zhe.setStyleSheet("QPushButton{\n"
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
        self.chuang_zhe.setObjectName("chuang_zhe")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.chaung_gui.setText(_translate("Form", "确定"))
        self.wancheng.setText(_translate("Form", "完成"))
        self.groupBox.setTitle(_translate("Form", "窗有效面积系数值："))
        self.label.setText(_translate("Form", "窗柜类型："))
        self.comboBox.setItemText(0, _translate("Form", "/"))
        self.comboBox.setItemText(1, _translate("Form", "单层钢窗"))
        self.comboBox.setItemText(2, _translate("Form", "单层木窗"))
        self.comboBox.setItemText(3, _translate("Form", "双层钢窗"))
        self.comboBox.setItemText(4, _translate("Form", "双层木窗"))
        self.pushButton.setText(_translate("Form", "面积输入完毕"))
        self.chuang_bo.setText(_translate("Form", "确定"))
        self.label_5.setText(_translate("Form", "窗朝向北面积(m^2)："))
        self.label_7.setText(_translate("Form", "窗朝向西面积(m^2)："))
        self.label_8.setText(_translate("Form", "窗朝向东面积(m^2)："))
        self.label_6.setText(_translate("Form", "窗朝向南面积(m^2)："))
        self.label_10.setText(_translate("Form", "水平(m^2)："))
        self.groupBox_2.setTitle(_translate("Form", "窗玻璃的遮挡系数值："))
        self.label_2.setText(_translate("Form", "玻璃类型："))
        self.comboBox_2.setItemText(0, _translate("Form", "/"))
        self.comboBox_2.setItemText(1, _translate("Form", "标准玻璃"))
        self.comboBox_2.setItemText(2, _translate("Form", "5mm厚普通玻璃"))
        self.comboBox_2.setItemText(3, _translate("Form", "6mm厚普通玻璃"))
        self.comboBox_2.setItemText(4, _translate("Form", "3mm厚吸热玻璃"))
        self.comboBox_2.setItemText(5, _translate("Form", "5mm厚吸热玻璃"))
        self.comboBox_2.setItemText(6, _translate("Form", "6mm厚吸热玻璃"))
        self.comboBox_2.setItemText(7, _translate("Form", "双层3mm厚普通玻璃"))
        self.comboBox_2.setItemText(8, _translate("Form", "双层5mm厚普通玻璃"))
        self.comboBox_2.setItemText(9, _translate("Form", "双层6mm厚普通玻璃"))
        self.groupBox_3.setTitle(_translate("Form", "窗内遮阳设施的遮阳系数："))
        self.label_3.setText(_translate("Form", "窗内遮阳类型："))
        self.comboBox_3.setItemText(0, _translate("Form", "/"))
        self.comboBox_3.setItemText(1, _translate("Form", "无遮阳设备"))
        self.comboBox_3.setItemText(2, _translate("Form", "白布帘（浅色）"))
        self.comboBox_3.setItemText(3, _translate("Form", "浅蓝色布帘（中间色）"))
        self.comboBox_3.setItemText(4, _translate("Form", "深黄、紫红、深绿色布帘（深色）"))
        self.comboBox_3.setItemText(5, _translate("Form", "活动百叶帘（中间色）"))
        self.chuang_zhe.setText(_translate("Form", "确定"))
import rishe_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form88()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chuangkou_xin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form7(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(792, 614)
        Form.setStyleSheet("QWidget#Form{\n"
"border-image: url(:/chuang/chuanghu.png);\n"
"\n"
"}\n"
"")
        self.queding_ck = QtWidgets.QPushButton(Form)
        self.queding_ck.setEnabled(False)
        self.queding_ck.setGeometry(QtCore.QRect(580, 180, 151, 41))
        self.queding_ck.setStyleSheet("QPushButton{\n"
"color:white;\n"
"font: 16pt \"楷体\";\n"
"border-radius:8px;\n"
"background-color:rgb(33, 174, 250);\n"
"spacing:20px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(72,203,250);\n"
"}\n"
"QPushButton:checked{\n"
"background-color: rgb(11, 15, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(85,85,255);\n"
"}\n"
"QPushButton:disabled{\n"
"\n"
"    background-color: rgb(165, 165, 165);\n"
"    color: rgb(11, 11, 11);\n"
"}")
        self.queding_ck.setCheckable(True)
        self.queding_ck.setObjectName("queding_ck")
        self.layoutWidget_2 = QtWidgets.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(60, 480, 441, 91))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_4.setStyleSheet("font: 14pt \"楷体\";\n"
"color: rgb(255, 44, 16);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.chuangmian = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.chuangmian.setStyleSheet("font: 18pt \"楷体\";")
        self.chuangmian.setObjectName("chuangmian")
        self.horizontalLayout_4.addWidget(self.chuangmian)
        self.queding_ds = QtWidgets.QPushButton(Form)
        self.queding_ds.setEnabled(False)
        self.queding_ds.setGeometry(QtCore.QRect(580, 60, 151, 41))
        self.queding_ds.setStyleSheet("QPushButton{\n"
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
        self.queding_ds.setCheckable(True)
        self.queding_ds.setObjectName("queding_ds")
        self.queding_cn = QtWidgets.QPushButton(Form)
        self.queding_cn.setEnabled(False)
        self.queding_cn.setGeometry(QtCore.QRect(580, 400, 151, 41))
        self.queding_cn.setStyleSheet("QPushButton{\n"
"color:white;\n"
"font: 16pt \"楷体\";\n"
"border-radius:8px;\n"
"background-color:rgb(33, 174, 250);\n"
"spacing:20px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(72,203,250);\n"
"}\n"
"QPushButton:checked{\n"
"background-color: rgb(11, 15, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(85,85,255);\n"
"}\n"
"QPushButton:disabled{\n"
"\n"
"    background-color: rgb(165, 165, 165);\n"
"    color: rgb(11, 11, 11);\n"
"}")
        self.queding_cn.setCheckable(True)
        self.queding_cn.setObjectName("queding_cn")
        self.layoutWidget_4 = QtWidgets.QWidget(Form)
        self.layoutWidget_4.setGeometry(QtCore.QRect(60, 160, 491, 81))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_2.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(60)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_2.setStyleSheet("font: 14pt \"楷体\";\n"
"color: rgb(255, 44, 16);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.chuangk_com = QtWidgets.QComboBox(self.layoutWidget_4)
        self.chuangk_com.setStyleSheet("font: 12pt \"楷体\";")
        self.chuangk_com.setObjectName("chuangk_com")
        self.chuangk_com.addItem("")
        self.chuangk_com.addItem("")
        self.chuangk_com.addItem("")
        self.chuangk_com.addItem("")
        self.chuangk_com.addItem("")
        self.horizontalLayout_2.addWidget(self.chuangk_com)
        self.layoutWidget_5 = QtWidgets.QWidget(Form)
        self.layoutWidget_5.setGeometry(QtCore.QRect(60, 30, 491, 101))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout.setSpacing(60)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget_5)
        self.label.setStyleSheet("font: 14pt \"楷体\";\n"
"color: rgb(255, 44, 16);")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.dsbl_com = QtWidgets.QComboBox(self.layoutWidget_5)
        self.dsbl_com.setStyleSheet("font: 12pt \"楷体\";")
        self.dsbl_com.setObjectName("dsbl_com")
        self.dsbl_com.addItem("")
        self.dsbl_com.addItem("")
        self.dsbl_com.addItem("")
        self.horizontalLayout.addWidget(self.dsbl_com)
        self.queding_cw = QtWidgets.QPushButton(Form)
        self.queding_cw.setEnabled(False)
        self.queding_cw.setGeometry(QtCore.QRect(580, 290, 151, 41))
        self.queding_cw.setStyleSheet("QPushButton{\n"
"color:white;\n"
"font: 16pt \"楷体\";\n"
"border-radius:8px;\n"
"background-color:rgb(33, 174, 250);\n"
"spacing:20px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(72,203,250);\n"
"}\n"
"QPushButton:checked{\n"
"background-color: rgb(11, 15, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgb(85,85,255);\n"
"}\n"
"QPushButton:disabled{\n"
"\n"
"    background-color: rgb(165, 165, 165);\n"
"    color: rgb(11, 11, 11);\n"
"}")
        self.queding_cw.setCheckable(True)
        self.queding_cw.setObjectName("queding_cw")
        self.queding_chuangk = QtWidgets.QPushButton(Form)
        self.queding_chuangk.setEnabled(False)
        self.queding_chuangk.setGeometry(QtCore.QRect(510, 510, 151, 61))
        self.queding_chuangk.setStyleSheet("QPushButton{\n"
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
        self.queding_chuangk.setObjectName("queding_chuangk")
        self.chuangn = QtWidgets.QComboBox(Form)
        self.chuangn.setGeometry(QtCore.QRect(450, 410, 111, 21))
        self.chuangn.setStyleSheet("font: 12pt \"楷体\";")
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
        self.chuangn.addItem("")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(70, 410, 384, 23))
        self.label_3.setMinimumSize(QtCore.QSize(300, 0))
        self.label_3.setMaximumSize(QtCore.QSize(400, 16777215))
        self.label_3.setStyleSheet("font: 14pt \"楷体\";\n"
"color: rgb(255, 44, 16);")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(70, 271, 400, 81))
        self.label_5.setMinimumSize(QtCore.QSize(400, 0))
        self.label_5.setMaximumSize(QtCore.QSize(400, 16777215))
        self.label_5.setStyleSheet("font: 14pt \"楷体\";\n"
"color: rgb(255, 44, 16);")
        self.label_5.setObjectName("label_5")
        self.chuangw = QtWidgets.QComboBox(Form)
        self.chuangw.setGeometry(QtCore.QRect(452, 300, 111, 21))
        self.chuangw.setStyleSheet("font: 12pt \"楷体\";")
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
        self.chuangw.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.queding_ck.setText(_translate("Form", "填写完毕"))
        self.label_4.setText(_translate("Form", "窗口面积（m^2）:"))
        self.queding_ds.setText(_translate("Form", "填写完毕"))
        self.queding_cn.setText(_translate("Form", "填写完毕"))
        self.label_2.setText(_translate("Form", "窗框类型："))
        self.chuangk_com.setItemText(0, _translate("Form", "无"))
        self.chuangk_com.setItemText(1, _translate("Form", "全部金属"))
        self.chuangk_com.setItemText(2, _translate("Form", "木窗框（80%玻璃）"))
        self.chuangk_com.setItemText(3, _translate("Form", "木窗框（60%玻璃）"))
        self.chuangk_com.setItemText(4, _translate("Form", "金属窗框（80%玻璃）"))
        self.label.setText(_translate("Form", "单/双玻璃窗："))
        self.dsbl_com.setItemText(0, _translate("Form", "无"))
        self.dsbl_com.setItemText(1, _translate("Form", "单层窗玻璃"))
        self.dsbl_com.setItemText(2, _translate("Form", "双层窗玻璃"))
        self.queding_cw.setText(_translate("Form", "填写完毕"))
        self.queding_chuangk.setText(_translate("Form", "确定"))
        self.chuangn.setItemText(0, _translate("Form", "无"))
        self.chuangn.setItemText(1, _translate("Form", "5.8"))
        self.chuangn.setItemText(2, _translate("Form", "6.4"))
        self.chuangn.setItemText(3, _translate("Form", "7.0"))
        self.chuangn.setItemText(4, _translate("Form", "7.6"))
        self.chuangn.setItemText(5, _translate("Form", "8.2"))
        self.chuangn.setItemText(6, _translate("Form", "8.7"))
        self.chuangn.setItemText(7, _translate("Form", "9.4"))
        self.chuangn.setItemText(8, _translate("Form", "9.9"))
        self.chuangn.setItemText(9, _translate("Form", "10.5"))
        self.chuangn.setItemText(10, _translate("Form", "11.1"))
        self.label_3.setText(_translate("Form", "窗内表面换热系数，W/（m^2*℃）："))
        self.label_5.setText(_translate("Form", "窗外表面换热系数，W/（m^2*℃）："))
        self.chuangw.setItemText(0, _translate("Form", "无"))
        self.chuangw.setItemText(1, _translate("Form", "11.6"))
        self.chuangw.setItemText(2, _translate("Form", "12.8"))
        self.chuangw.setItemText(3, _translate("Form", "14.0"))
        self.chuangw.setItemText(4, _translate("Form", "15.1"))
        self.chuangw.setItemText(5, _translate("Form", "16.3"))
        self.chuangw.setItemText(6, _translate("Form", "17.5"))
        self.chuangw.setItemText(7, _translate("Form", "18.6"))
        self.chuangw.setItemText(8, _translate("Form", "19.8"))
        self.chuangw.setItemText(9, _translate("Form", "20.9"))
        self.chuangw.setItemText(10, _translate("Form", "22.1"))
        self.chuangw.setItemText(11, _translate("Form", "23.3"))
        self.chuangw.setItemText(12, _translate("Form", "24.4"))
        self.chuangw.setItemText(13, _translate("Form", "25.6"))
        self.chuangw.setItemText(14, _translate("Form", "26.7"))
        self.chuangw.setItemText(15, _translate("Form", "27.9"))
        self.chuangw.setItemText(16, _translate("Form", "29.1"))
import chuanghu_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form7()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

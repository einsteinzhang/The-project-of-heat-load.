# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'input_xin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1300, 850)
        Form.setMinimumSize(QtCore.QSize(1300, 850))
        Form.setMaximumSize(QtCore.QSize(1300, 850))
        Form.setStyleSheet("QWidget#Form{\n"
"border-image: url(:/tianjin/tianda.png);\n"
"}\n"
"")
        self.renshu = QtWidgets.QPushButton(Form)
        self.renshu.setEnabled(True)
        self.renshu.setGeometry(QtCore.QRect(40, 710, 200, 80))
        self.renshu.setMinimumSize(QtCore.QSize(200, 80))
        self.renshu.setMaximumSize(QtCore.QSize(100, 80))
        self.renshu.setStyleSheet("QPushButton{\n"
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
"}")
        self.renshu.setCheckable(True)
        self.renshu.setObjectName("renshu")
        self.bolichuang_1 = QtWidgets.QPushButton(Form)
        self.bolichuang_1.setEnabled(True)
        self.bolichuang_1.setGeometry(QtCore.QRect(60, 720, 200, 80))
        self.bolichuang_1.setMinimumSize(QtCore.QSize(200, 80))
        self.bolichuang_1.setMaximumSize(QtCore.QSize(100, 80))
        self.bolichuang_1.setStyleSheet("QPushButton{\n"
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
"}")
        self.bolichuang_1.setCheckable(True)
        self.bolichuang_1.setObjectName("bolichuang_1")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(310, 310, 471, 41))
        self.label_2.setStyleSheet("font: 20pt \"楷体\";\n"
"color:rgb(255, 81, 12);")
        self.label_2.setObjectName("label_2")
        self.queren_xiawen = QtWidgets.QPushButton(Form)
        self.queren_xiawen.setEnabled(False)
        self.queren_xiawen.setGeometry(QtCore.QRect(420, 390, 521, 61))
        self.queren_xiawen.setStyleSheet("QPushButton{\n"
"font: 16pt \"楷体\";\n"
"background-color: rgb(20, 232, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"\n"
"    background-color: rgb(47, 19, 190);\n"
"}\n"
"QPushButton:disabled{\n"
"\n"
"    background-color: rgb(165, 165, 165);\n"
"    color: rgb(11, 11, 11);\n"
"}")
        self.queren_xiawen.setObjectName("queren_xiawen")
        self.xia_wen = QtWidgets.QLineEdit(Form)
        self.xia_wen.setGeometry(QtCore.QRect(820, 250, 241, 20))
        self.xia_wen.setStyleSheet("background-color: transparent;\n"
"font: 16pt \"楷体\";\n"
"color: rgb(10, 55, 255);\n"
"border:none;\n"
"border-bottom:1px solid lightgreen;")
        self.xia_wen.setObjectName("xia_wen")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(310, 230, 421, 41))
        self.label_3.setStyleSheet("font: 20pt \"楷体\";\n"
"color:rgb(255, 81, 12);")
        self.label_3.setObjectName("label_3")
        self.zhaoming = QtWidgets.QPushButton(Form)
        self.zhaoming.setEnabled(True)
        self.zhaoming.setGeometry(QtCore.QRect(60, 710, 200, 80))
        self.zhaoming.setMinimumSize(QtCore.QSize(200, 80))
        self.zhaoming.setMaximumSize(QtCore.QSize(100, 80))
        self.zhaoming.setStyleSheet("QPushButton{\n"
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
"}")
        self.zhaoming.setCheckable(True)
        self.zhaoming.setObjectName("zhaoming")
        self.bolichuang = QtWidgets.QPushButton(Form)
        self.bolichuang.setEnabled(True)
        self.bolichuang.setGeometry(QtCore.QRect(60, 700, 200, 80))
        self.bolichuang.setMinimumSize(QtCore.QSize(200, 80))
        self.bolichuang.setMaximumSize(QtCore.QSize(100, 80))
        self.bolichuang.setStyleSheet("QPushButton{\n"
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
"}")
        self.bolichuang.setCheckable(True)
        self.bolichuang.setObjectName("bolichuang")
        self.dong_wen = QtWidgets.QLineEdit(Form)
        self.dong_wen.setGeometry(QtCore.QRect(820, 330, 241, 20))
        self.dong_wen.setStyleSheet("background-color: transparent;\n"
"font: 16pt \"楷体\";\n"
"color: rgb(10, 55, 255);\n"
"border:none;\n"
"border-bottom:1px solid lightgreen;")
        self.dong_wen.setObjectName("dong_wen")
        self.fangjian1 = QtWidgets.QPushButton(Form)
        self.fangjian1.setEnabled(True)
        self.fangjian1.setGeometry(QtCore.QRect(40, 710, 200, 80))
        self.fangjian1.setMinimumSize(QtCore.QSize(200, 80))
        self.fangjian1.setMaximumSize(QtCore.QSize(100, 80))
        self.fangjian1.setStyleSheet("QPushButton{\n"
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
"")
        self.fangjian1.setCheckable(True)
        self.fangjian1.setObjectName("fangjian1")
        self.queren = QtWidgets.QPushButton(Form)
        self.queren.setEnabled(False)
        self.queren.setGeometry(QtCore.QRect(590, 670, 181, 131))
        self.queren.setStyleSheet("QPushButton{\n"
"font: 16pt \"楷体\";\n"
"background-color: rgb(20, 232, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"\n"
"    background-color: rgb(47, 19, 190);\n"
"}\n"
"QPushButton:disabled{\n"
"\n"
"    background-color: rgb(165, 165, 165);\n"
"    color: rgb(11, 11, 11);\n"
"}")
        self.queren.setObjectName("queren")
        self.chengshi = QtWidgets.QPushButton(Form)
        self.chengshi.setEnabled(False)
        self.chengshi.setGeometry(QtCore.QRect(470, 30, 400, 150))
        self.chengshi.setMinimumSize(QtCore.QSize(400, 150))
        self.chengshi.setMaximumSize(QtCore.QSize(400, 150))
        self.chengshi.setStyleSheet("QPushButton{\n"
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
        self.chengshi.setCheckable(True)
        self.chengshi.setObjectName("chengshi")
        self.caidan = QtWidgets.QPushButton(Form)
        self.caidan.setEnabled(False)
        self.caidan.setGeometry(QtCore.QRect(30, 670, 250, 150))
        self.caidan.setMinimumSize(QtCore.QSize(250, 150))
        self.caidan.setMaximumSize(QtCore.QSize(250, 150))
        self.caidan.setStyleSheet("QPushButton{\n"
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
"}\n"
"")
        self.caidan.setCheckable(True)
        self.caidan.setChecked(False)
        self.caidan.setObjectName("caidan")
        self.shebei = QtWidgets.QPushButton(Form)
        self.shebei.setEnabled(True)
        self.shebei.setGeometry(QtCore.QRect(60, 710, 200, 80))
        self.shebei.setMinimumSize(QtCore.QSize(200, 80))
        self.shebei.setMaximumSize(QtCore.QSize(100, 80))
        self.shebei.setStyleSheet("QPushButton{\n"
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
"}")
        self.shebei.setCheckable(True)
        self.shebei.setObjectName("shebei")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(51, 51, 3, 583))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(115)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ll1 = QtWidgets.QLabel(self.layoutWidget)
        self.ll1.setMinimumSize(QtCore.QSize(1, 1))
        self.ll1.setMaximumSize(QtCore.QSize(1, 1))
        self.ll1.setText("")
        self.ll1.setObjectName("ll1")
        self.verticalLayout.addWidget(self.ll1)
        self.ll2 = QtWidgets.QLabel(self.layoutWidget)
        self.ll2.setMinimumSize(QtCore.QSize(1, 1))
        self.ll2.setMaximumSize(QtCore.QSize(1, 1))
        self.ll2.setText("")
        self.ll2.setObjectName("ll2")
        self.verticalLayout.addWidget(self.ll2)
        self.ll3 = QtWidgets.QLabel(self.layoutWidget)
        self.ll3.setMinimumSize(QtCore.QSize(1, 1))
        self.ll3.setMaximumSize(QtCore.QSize(1, 1))
        self.ll3.setText("")
        self.ll3.setObjectName("ll3")
        self.verticalLayout.addWidget(self.ll3)
        self.ll4 = QtWidgets.QLabel(self.layoutWidget)
        self.ll4.setMinimumSize(QtCore.QSize(1, 1))
        self.ll4.setMaximumSize(QtCore.QSize(1, 1))
        self.ll4.setText("")
        self.ll4.setObjectName("ll4")
        self.verticalLayout.addWidget(self.ll4)
        self.ll5 = QtWidgets.QLabel(self.layoutWidget)
        self.ll5.setMinimumSize(QtCore.QSize(1, 1))
        self.ll5.setMaximumSize(QtCore.QSize(1, 1))
        self.ll5.setText("")
        self.ll5.setObjectName("ll5")
        self.verticalLayout.addWidget(self.ll5)
        self.ll5_2 = QtWidgets.QLabel(self.layoutWidget)
        self.ll5_2.setMinimumSize(QtCore.QSize(1, 1))
        self.ll5_2.setMaximumSize(QtCore.QSize(1, 1))
        self.ll5_2.setText("")
        self.ll5_2.setObjectName("ll5_2")
        self.verticalLayout.addWidget(self.ll5_2)
        self.fangjian1.raise_()
        self.layoutWidget.raise_()
        self.renshu.raise_()
        self.bolichuang_1.raise_()
        self.label_2.raise_()
        self.queren_xiawen.raise_()
        self.xia_wen.raise_()
        self.label_3.raise_()
        self.zhaoming.raise_()
        self.bolichuang.raise_()
        self.dong_wen.raise_()
        self.queren.raise_()
        self.chengshi.raise_()
        self.shebei.raise_()
        self.caidan.raise_()

        self.retranslateUi(Form)
        self.caidan.clicked['bool'].connect(Form.slot1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.renshu.setText(_translate("Form", "房间人员"))
        self.bolichuang_1.setText(_translate("Form", "透过玻璃窗日射"))
        self.label_2.setText(_translate("Form", "请输入冬季室内温度（℃）："))
        self.queren_xiawen.setText(_translate("Form", "填写完毕"))
        self.label_3.setText(_translate("Form", "请输入夏季室内温度（℃）："))
        self.zhaoming.setText(_translate("Form", "照明设备"))
        self.bolichuang.setText(_translate("Form", "外玻璃窗传热"))
        self.fangjian1.setText(_translate("Form", "建筑物结构"))
        self.queren.setText(_translate("Form", "显示结果"))
        self.chengshi.setText(_translate("Form", "城市选择"))
        self.caidan.setText(_translate("Form", "菜单"))
        self.shebei.setText(_translate("Form", "设备"))
import tianda_rc
import wuding_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

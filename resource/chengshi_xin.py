# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chengshi_xin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form3(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setMinimumSize(QtCore.QSize(800, 600))
        Form.setMaximumSize(QtCore.QSize(800, 600))
        Form.setStyleSheet("QWidget#Form{\n"
"    border-image: url(:/wuding1/ditu.png);\n"
"}")
        self.queding_cheng = QtWidgets.QPushButton(Form)
        self.queding_cheng.setGeometry(QtCore.QRect(320, 80, 121, 31))
        self.queding_cheng.setObjectName("queding_cheng")
        self.chengshi = QtWidgets.QComboBox(Form)
        self.chengshi.setGeometry(QtCore.QRect(30, 20, 411, 51))
        self.chengshi.setObjectName("chengshi")
        self.chengshi.addItem("")
        self.chengshi.addItem("")
        self.chengshi.addItem("")
        self.chengshi.addItem("")
        self.chengshi.addItem("")
        self.chengshi.addItem("")
        self.chengshi.addItem("")
        self.chengshi.addItem("")
        self.chengshi.addItem("")
        self.chengshi.addItem("")
        self.chengshi.addItem("")
        self.chengshi.addItem("")
        self.chengshi.addItem("")
        self.chengshi.addItem("")
        self.chengshi.addItem("")
        self.chengshi.addItem("")
        self.chengshi.addItem("")
        self.chengshi.addItem("")
        self.chengshi.addItem("")
        self.chengshi.addItem("")
        self.chengshi.addItem("")
        self.chengshi.addItem("")
        self.chengshi.addItem("")
        self.chengshi.addItem("")
        self.chengshi.addItem("")
        self.chengshi.addItem("")
        self.chengshi.addItem("")
        self.chengshi.addItem("")
        self.chengshi.addItem("")
        self.chengshi.addItem("")
        self.chengshi.addItem("")
        self.chengshi.addItem("")
        self.chengshi.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.queding_cheng.setText(_translate("Form", "确定"))
        self.chengshi.setItemText(0, _translate("Form", "北京"))
        self.chengshi.setItemText(1, _translate("Form", "天津"))
        self.chengshi.setItemText(2, _translate("Form", "石家庄"))
        self.chengshi.setItemText(3, _translate("Form", "太原"))
        self.chengshi.setItemText(4, _translate("Form", "呼和浩特"))
        self.chengshi.setItemText(5, _translate("Form", "沈阳"))
        self.chengshi.setItemText(6, _translate("Form", "长春"))
        self.chengshi.setItemText(7, _translate("Form", "哈尔滨"))
        self.chengshi.setItemText(8, _translate("Form", "上海"))
        self.chengshi.setItemText(9, _translate("Form", "南京"))
        self.chengshi.setItemText(10, _translate("Form", "杭州"))
        self.chengshi.setItemText(11, _translate("Form", "合肥"))
        self.chengshi.setItemText(12, _translate("Form", "福州"))
        self.chengshi.setItemText(13, _translate("Form", "南昌"))
        self.chengshi.setItemText(14, _translate("Form", "济南"))
        self.chengshi.setItemText(15, _translate("Form", "郑州"))
        self.chengshi.setItemText(16, _translate("Form", "武汉"))
        self.chengshi.setItemText(17, _translate("Form", "长沙"))
        self.chengshi.setItemText(18, _translate("Form", "广州"))
        self.chengshi.setItemText(19, _translate("Form", "南宁"))
        self.chengshi.setItemText(20, _translate("Form", "成都"))
        self.chengshi.setItemText(21, _translate("Form", "贵阳"))
        self.chengshi.setItemText(22, _translate("Form", "昆明"))
        self.chengshi.setItemText(23, _translate("Form", "拉萨"))
        self.chengshi.setItemText(24, _translate("Form", "西安"))
        self.chengshi.setItemText(25, _translate("Form", "兰州"))
        self.chengshi.setItemText(26, _translate("Form", "西宁"))
        self.chengshi.setItemText(27, _translate("Form", "银川"))
        self.chengshi.setItemText(28, _translate("Form", "乌鲁木齐"))
        self.chengshi.setItemText(29, _translate("Form", "台北"))
        self.chengshi.setItemText(30, _translate("Form", "大连"))
        self.chengshi.setItemText(31, _translate("Form", "海口"))
        self.chengshi.setItemText(32, _translate("Form", "重庆"))




import wuding_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form3()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


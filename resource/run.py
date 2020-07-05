from PyQt5.Qt import *
from PyQt5.QtWidgets import *
from resource.input_xin import *
from resource.output import *
from resource.fangjian import *
from resource.renshu_xin import *
from resource.zhaoming_xin import *
from resource.chengshi_xin import *
from resource.chuangkou_xin import *
from resource.chuangrishe import *
from resource.chengshi_1 import *
from resource.tainanle import *
from resource.shebei import *
from resource.ou import *
from resource.wuding1 import *
from resource.wuding2 import *
from resource.wuding3 import *
from resource.wuding4 import *
from resource.wuding5 import *
from resource.wuding6 import *
from resource.wuding7 import *
from resource.wuding8 import *
from resource.wuding9 import *
from resource.wuding10 import *
from resource.wuding11 import *
from resource.wuding12 import *
from resource.wuding13 import *
from resource.wuding14 import *
from resource.wuding15 import *
from resource.wuding16 import *
from resource.wuding17 import *
from resource.wuding18 import *
from resource.wuding19 import *
from resource.wuding20 import *
from resource.wuding21 import *
from resource.qiang1 import *
from resource.qiang2 import *
from resource.qiang3 import *
from resource.qiang4 import *
from resource.qiang5 import *
from resource.qiang6 import *
from resource.qiang7 import *
from resource.qiang8 import *
from resource.qiang9 import *
from resource.qiang10 import *
from resource.qiang11 import *
from resource.qiang12 import *
from resource.qiang13 import *
from resource.qiang14 import *
from resource.qiang15 import *
from resource.qiang16 import *
from resource.qiang17 import *
from resource.qiang18 import *
from resource.qiang19 import *
from resource.qiang20 import *
from resource.qiang21 import *
from resource.qiang22 import *
from resource.qiang23 import *
from resource.qiang24 import *
from resource.qiang25 import *
import pyqtgraph as pg  ##绘图用
import xlwt  ##导出Excel





#input

class Ui_Form1(QWidget,Ui_Form):#input中的类名！

    def __init__(self):
        super().__init__()
        # super(Ui_Form1, self).__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground, True)

        self.setupUi(self)

        self.animation_targets = [self.fangjian1,self.renshu, self.zhaoming,self.bolichuang,self.bolichuang_1,self.shebei]  # 这里不是关于槽的名字，而是Designer右上角的按钮名字。
        # self.animation_targets_pos = [target.pos() for target in self.animation_targets]
        self.animation_labels = [self.ll1,self.ll2,self.ll3,self.ll4,self.ll5,self.ll5_2]#####这里用labels代替起了定位的作用！注意：label大小最小最好！不然点击会点成label。

        #信号与槽,按钮发出clicked信号，通过connect来将按钮的信号与函数连接
        self.queren.clicked.connect(self.ok_button)#connect后面连接（self.方法）
        self.queren_xiawen.clicked.connect(self.xiawen)
        # self.queren_dongwen.clicked.connect(self.dongwen)
        self.xia_wen.textChanged.connect(self.xiawen_1)
        self.dong_wen.textChanged.connect(self.xiawen_1)
        self.fangjian1.clicked.connect(self.fangjian_button)
        self.renshu.clicked.connect(self.renshu_button)#打开房间人数的界面
        self.zhaoming.clicked.connect(self.zhaoming_button)#确定照明设备界面
        self.chengshi.clicked.connect(self.chengshi_button)#确定城市界面
        self.bolichuang.clicked.connect(self.boli_button)#确定玻璃窗传热界面
        self.bolichuang_1.clicked.connect(self.chuaungri_button)#确定窗口日射得冷负荷
        self.shebei.clicked.connect(self.shebei_button)
        # self.fangjian1.clicked['bool'].connect(self.zuihoulea)
        # self.renshu.clicked['bool'].connect(self.zuihoulea)
        # self.zhaoming.clicked['bool'].connect(self.zuihoulea)
        # self.bolichuang.clicked['bool'].connect(self.zuihoulea)
        self.shebei.clicked['bool'].connect(self.zuihoulea)
        # self.chengshi.clicked['bool'].connect(self.zuihoulea)


    def slot1(self,checked):

        # animation_group = QSequentialAnimationGroup(self)
        # for idx, target in enumerate(self.animation_targets):
        #     animation = QPropertyAnimation()
        #     animation.setTargetObject(target)
        #     animation.setPropertyName(b'pos')
        #     # if not checked:
        #     animation.setStartValue(self.caidan.pos())
        #     # animation.setEndValue(self.animation_targets_pos[idx])
        #     animation.setEndValue(self.animation_labels[idx].pos())
        #     # else:
        #     #     animation.setEndValue(self.caidan.pos())
        #     #     animation.setStartValue(self.animation_targets_pos[idx])
        #     animation.setDuration(300)  # 控制展开收进的时间快慢。
        #     animation.setEasingCurve(QEasingCurve.OutBounce)  # 使窗口以弹出的形式出来。
        #     animation_group.addAnimation(animation)
        # if not checked:
        #     animation_group.setDirection(QAbstractAnimation.Forward)
        # else:
        #     animation_group.setDirection(QAbstractAnimation.Backward)  # 有了向前和向后，不需要上面的开始和结束时间。
        # animation_group.start(QAbstractAnimation.DeleteWhenStopped)
        if checked:
            QMessageBox.information(self, '提示：', u'请确保选择城市之后，再进行负荷参数设计！')
            animation_group = QSequentialAnimationGroup(self)
            for idx, target in enumerate(self.animation_targets):
                animation = QPropertyAnimation()
                animation.setTargetObject(target)
                animation.setPropertyName(b'pos')
                animation.setStartValue(self.caidan.pos())
                # animation.setEndValue(self.animation_targets_pos[idx])
                animation.setEndValue(self.animation_labels[idx].pos())
                animation.setDuration(300)  # 控制展开收进的时间快慢。
                animation.setEasingCurve(QEasingCurve.OutBounce)  # 使窗口以弹出的形式出来。
                animation_group.addAnimation(animation)

            animation_group.start(QAbstractAnimation.DeleteWhenStopped)
        else:
            animation_group = QSequentialAnimationGroup(self)
            for idx, target in enumerate(self.animation_targets):
                animation = QPropertyAnimation()
                animation.setTargetObject(target)
                animation.setPropertyName(b'pos')
                animation.setEndValue(self.caidan.pos())
                animation.setStartValue(self.animation_labels[idx].pos())
                animation.setDuration(300)  # 控制展开收进的时间快慢。
                animation.setEasingCurve(QEasingCurve.InOutBounce)  # 使窗口以弹出的形式出来。
                animation_group.addAnimation(animation)

            animation_group.start(QAbstractAnimation.DeleteWhenStopped)


    def ok_button(self):
        QMessageBox.information(self, '请注意：', u'请确保“菜单”按钮中六项负荷项均填写完成！')
        self.output_win = MyMainWindow2()
        self.output_win.show()
        self.output_win232 = MyMainWindow2777()
        self.output_win232.show()


    def xiawen_1(self):
        dongji_wendu = self.dong_wen.text()
        xiaji_wendu = self.xia_wen.text()
        if len(xiaji_wendu)>0 and len(dongji_wendu)>0:
            self.queren_xiawen.setEnabled(True)
            self.chengshi.setEnabled(True)
            self.caidan.setEnabled(True)
        else:
            self.queren_xiawen.setEnabled(False)
            self.chengshi.setEnabled(False)
            self.caidan.setEnabled(False)
    def xiawen(self):

        global dongji_shidu
        global xiaji_wendu
        global xiaji_shidu
        global xiawen
        global dongji_wendu1
        dongji_wendu = self.dong_wen.text()
        dongji_wendu1 = float(dongji_wendu)
        print(dongji_wendu1)
        xiaji_wendu = self.xia_wen.text()
        if 15 < int(xiaji_wendu) < 31 and 15 < int(dongji_wendu) < 31:
            my = QMessageBox.information(self,'提示：', u'输入成功！')
            print(my)
        else:
            my = QMessageBox.information(self,'请注意：', u'室内输入温度为16——30℃之间的整数')
            print(my)
    # def dongwen(self):
    #     global dongji_wendu1
    #     dongji_wendu = self.dong_wen.text()
    #     dongji_wendu1 = float(dongji_wendu)
    #     print(dongji_wendu1)
    #     if 15 < int(dongji_wendu) < 31:
    #         my24 = QMessageBox.information(self,'提示：', u'输入成功！')
    #         print(my24)
    #     else:
    #         my24 = QMessageBox.information(self,'请注意：', u'冬季室内输入温度为16——30℃之间的整数')
    #         print(my24)


    def fangjian_button(self,cs):

        # print(cs)
        # if cs:
        #     self.fagnjian_win = MyMainWindow3()
        #     self.fagnjian_win.show()
        # else:
        #     my = QMessageBox.information(self, '提示：', u'请先输入城市！')
        #     print(my)


        self.fagnjian_win = MyMainWindow3()
        self.fagnjian_win.show()
    def renshu_button(self):
        self.renshu_win = Ui_Form45()
        self.renshu_win.show()
    def zhaoming_button(self):
        self.zhaoming_win = Ui_Form5()
        self.zhaoming_win.show()
    def chengshi_button(self):
        self.chengshi_win = Ui_Form32()
        self.chengshi_win.show()
    def boli_button(self):
        self.chuangkou_win = MyMainWindow7()
        self.chuangkou_win.show()
    def chuaungri_button(self):
        self.chuangkou_win = MyMainWindow8()
        self.chuangkou_win.show()

    def zuihoulea(self,checked):
        if self.fangjian1.isChecked and self.chengshi.isChecked:
            self.queren.setEnabled(True)
        else:
            self.queren.setEnabled(False)

    def shebei_button(self):
        self.shebei_win = MyMainWindow5555()
        self.shebei_win.show()

#output

class MyMainWindow2(QMainWindow, Ui_MainWindow2):#output中的类名！

    def __init__(self, parent=None):
        super(MyMainWindow2, self).__init__(parent)
        self.setupUi(self)
        # 信号与槽,按钮发出clicked信号，通过connect来将按钮的信号与函数连接
        self.pushButton.clicked.connect(self.do_something)
        self.pushButton_2.clicked.connect(self.clear_button2)
        self.pushButton_3.clicked.connect(self.paint_button3)
        self.menuSave.triggered.connect(self.daochu)


    #你自己的算法
    def do_something(self):
        global Q_zuizhong
        Q_zuizhong = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        self.Q_renhuitu = [Q_ren]*24
        self.Q_dengguanghuitu = [Q_dengguang]*24
        self.Q_shebeihuitu = [Q_shebei]*24
        for i in range(len(Q_qiangorwu_qiang)):
            Q_zuizhong[i] =Q_qiangorwu_qiang[i]+Q_qiangorwu_wu[i]+Q_bolichuanre[i]+Q_rs[i]+self.Q_renhuitu[i]+self.Q_dengguanghuitu[i]+self.Q_shebeihuitu[i]
        self.Qzuizhong = max(Q_zuizhong)
        self.Qzuizhongqiangwu = max(Q_zuizhong1)
        self.Qzuizhongbolichuanre = max(Q_bolichuanre)
        self.Qzuizhongrs = max(Q_rs)


        # self.num1 = (float(dongji_wendu) + float(dongji_shidu) + float(input_renshu))*2
        # self.num2 = self.num1

        #在界面显示你的结果
        self.jieguo1.setPlainText("通过墙体/屋顶传热得冷负荷最大值："+str(self.Qzuizhongqiangwu))
        self.jieguo2.setPlainText("通过玻璃窗传热得冷负荷最大值："+str(self.Qzuizhongbolichuanre))
        self.jieguo3.setPlainText("透过玻璃窗日射得冷负荷最大值："+str(self.Qzuizhongrs))
        self.jieguo4.setPlainText("人体产生冷负荷最大值："+str(Q_ren))
        self.jieguo5.setPlainText("照明设备产生冷负荷最大值："+str(Q_dengguang))
        self.jieguo6_2.setPlainText("设备产生冷负荷最大值："+str(Q_shebei))
        self.jieguo6.setPlainText("最终冷负荷最大值："+str(self.Qzuizhong))

    def clear_button2(self):
        self.jieguo1.clear()
        self.jieguo2.clear()
        self.jieguo3.clear()
        self.jieguo4.clear()
        self.jieguo5.clear()
        self.jieguo6.clear()

    def paint_button3(self):
        global Q_ren
        global Q_dengguang
        global Q_bolichuanre
        global Q_rs
        global Q_zuizhong1
        self.Q_renhuitu = [Q_ren]*24
        self.Q_dengguanghuitu = [Q_dengguang]*24
        self.Q_shebeihuitu = [Q_shebei]*24

        plt = pg.plot(title='夏季冷负荷图表')
        plt.addLegend()


        c1 = plt.plot([0, 1,2, 3, 4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],self.Q_renhuitu, pen='r', name='人散热冷负荷/W')
        c2 = plt.plot([0, 1,2, 3, 4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],self.Q_dengguanghuitu, pen='g', name='灯光冷负荷/W')
        c3 = plt.plot([0, 1,2, 3, 4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],Q_bolichuanre, pen='b', name='通过玻璃窗传热形成冷负荷/W')
        c4 = plt.plot([0, 1,2, 3, 4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],Q_rs, pen='w', name='通过玻璃窗日射形成冷负荷/W')
        c5 = plt.plot([0, 1,2, 3, 4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],Q_zuizhong1, pen='y', name='墙体传热形成冷负荷/W')
        c5_2 = plt.plot([0, 1,2, 3, 4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],self.Q_shebeihuitu, pen='c', name='设备形成冷负荷/W')
        c5 = plt.plot([0, 1,2, 3, 4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],Q_zuizhong, pen='m', name='最终冷负荷/W')

    def daochu(self):
        my_file, bb = QFileDialog.getSaveFileName(self, r'文件另存为：', '/', '*.xls')
        print(my_file)
        book = xlwt.Workbook(encoding='utf-8', style_compression=0)
        sheet = book.add_sheet('mysheet', cell_overwrite_ok=True)
        sheet.write(0, 0, '时间/h')
        sheet.write(1, 0, '墙体传热形成冷负荷/W')
        sheet.write(2, 0, '人散热冷负荷/W')
        sheet.write(3, 0, '灯光冷负荷/W')
        sheet.write(4, 0, '通过玻璃窗日射形成冷负荷/W')
        sheet.write(5, 0, '通过玻璃窗传热形成冷负荷/W')
        sheet.write(6, 0, '设备形成冷负荷/W')
        sheet.write(7, 0, '最终冷负荷/W')
        for i in range(0,24):
            sheet.write(0,i+1,i)
            sheet.write(1,i+1,Q_zuizhong1[i])
            sheet.write(2,i+1,self.Q_renhuitu[i])
            sheet.write(3,i+1,self.Q_dengguanghuitu[i])
            sheet.write(4,i+1,Q_rs[i])
            sheet.write(5,i+1,Q_bolichuanre[i])
            sheet.write(6,i+1,self.Q_shebeihuitu[i])
            sheet.write(6,i+1,Q_zuizhong[i])

        book.save(my_file)

class MyMainWindow3(QMainWindow, Ui_MainWindow3):
    def __init__(self, parent=None):
        super(MyMainWindow3, self).__init__(parent)
        self.setupUi(self)
        self.qiangtimianji.clicked.connect(self.qiangtimianji_button)
        self.qinagwaibianmian.clicked.connect(self.qiangmian_button)
        self.wudingwaibm.clicked.connect(self.wuding_button)
        self.tainanle.clicked.connect(self.tainanle1)
        self.zuihzonglea.clicked.connect(self.zuizhong)
        self.mian_dong.textChanged.connect(self.hunao)
        self.mian_xi.textChanged.connect(self.hunao)
        self.mian_bei.textChanged.connect(self.hunao)
        self.mian_nan.textChanged.connect(self.hunao)
        self.mian_wu.textChanged.connect(self.hunao)
        self.qiangmian.currentTextChanged.connect(self.hunao_1)
        self.qiangmian_2.currentTextChanged.connect(self.hunao_2)


        list_20=["海口"]
        list_25=['福州','广州','台北','南宁','贵阳','昆明']
        list_30=['南京','上海','杭州','合肥','南昌','武汉','成都','重庆','长沙']
        list_35=['济南','郑州','西安','兰州','西宁']
        list_40=['石家庄','呼和浩特','沈阳','北京','天津','太原','银川','大连']
        list_45=['长春','哈尔滨','乌鲁木齐']
        list_lasa=['拉萨']
        global jp_s #太阳总辐射日平均照度
        global jp_e #太阳总辐射日平均照度
        global jp_w #太阳总辐射日平均照度
        global jp_n #太阳总辐射日平均照度
        global jp_sp #太阳总辐射日平均照度
        global cs

        if cs in list_20:
            jp_s = 65
            jp_e = 160
            jp_w = 160
            jp_n = 102
            jp_sp = 325
        elif cs in list_25:
            jp_s = 73
            jp_e = 175
            jp_w = 175
            jp_n = 94
            jp_sp = 353
        elif cs in list_30:
            jp_s = 90
            jp_e = 171
            jp_w = 171
            jp_n = 86
            jp_sp = 328
        elif cs in list_35:
            jp_s = 109
            jp_e = 185
            jp_w = 185
            jp_n = 83
            jp_sp = 355
        elif cs in list_40:
            jp_s = 130
            jp_e = 186
            jp_w = 186
            jp_n = 79
            jp_sp = 333
        elif cs in list_45:
            jp_s = 152
            jp_e = 187
            jp_w = 187
            jp_n = 77
            jp_sp = 345
        elif cs in list_lasa:
            jp_s = 90
            jp_e = 171
            jp_w = 171
            jp_n = 86
            jp_sp = 328
        # print(jp_e,jp_n,jp_s)

        global wqhrxh#不同城市，不同风速下的围护结构外表面换热系数wqhrxh
        if cs in fengsu_1:
            wqhrxh = 14
        elif cs in fengsu_1_5:
            wqhrxh = 17.5
        elif cs in fengsu_2:
            wqhrxh = 19.8
        elif cs in fengsu_2_5:
            wqhrxh = 22.1
        elif cs in fengsu_3:
            wqhrxh = 24.4
        elif cs in fengsu_3_5:
            wqhrxh = 26.1
        elif cs in fengsu_4:
            wqhrxh = 27.9
        # print(wqhrxh)
    def hunao(self):
        m_dongqitttang1 = self.mian_dong.text()
        m_xiqitttang1 = self.mian_xi.text()
        m_nanqitttang1 = self.mian_nan.text()
        m_beiqitttang1 = self.mian_bei.text()
        m_wuditttng1 = self.mian_wu.text()
        if len(m_dongqitttang1)>0 and len(m_xiqitttang1)>0 and len(m_nanqitttang1)>0 and len(m_beiqitttang1)>0 and len(m_wuditttng1)>0:
            self.qiangtimianji.setEnabled(True)

        else:
            self.qiangtimianji.setEnabled(False)
    def hunao_1(self):
        self.qinagwaibianmian.setEnabled(True)
    def hunao_2(self):
        self.wudingwaibm.setEnabled(True)

    def qiangtimianji_button(self):
        global m_dongqiang
        global m_xiqiang
        global m_nanqiang
        global m_beiqiang
        global m_wuding

        m_dongqitttang1 = self.mian_dong.text()
        m_dongqiang = float(m_dongqitttang1)
        m_xiqitttang1= self.mian_xi.text()
        m_xiqiang = float(m_xiqitttang1)
        m_nanqitttang1 = self.mian_nan.text()
        m_nanqiang = float(m_nanqitttang1)
        m_beiqitttang1 = self.mian_bei.text()
        m_beiqiang = float(m_beiqitttang1)
        m_wuditttng1 = self.mian_wu.text()
        m_wuding = float(m_wuditttng1)

        print(m_dongqiang, m_xiqiang,m_nanqiang,m_beiqiang,m_wuding)

    def qiangmian_button(self):
        hhhyy = self.qiangmian.currentText()
        global q_xsxs#墙外表面的太阳辐射热吸收系数
        if hhhyy == "金属：白铁屋面(灰黑色)":
            q_xsxs =0.86
        elif hhhyy == "金属：抛光铝反射板(浅色)":
            q_xsxs = 0.12
        elif hhhyy == "粉刷：拉毛水泥墙面(灰/米黄色)":
            q_xsxs = 0.64
        elif hhhyy == "粉刷：石灰粉刷(白色)":
            q_xsxs = 0.48
        elif hhhyy == "粉刷：陶石子墙面(浅灰色)":
            q_xsxs = 0.68
        elif hhhyy == "粉刷：水泥粉刷墙面(浅蓝色)":
            q_xsxs = 0.56
        elif hhhyy == "粉刷：砂石粉刷墙(深色)":
            q_xsxs = 0.57
        elif hhhyy == "粉刷：浅色饰面砖(浅黄、浅绿色)":
            q_xsxs = 0.5
        elif hhhyy == "红砖墙(红色)旧":
            q_xsxs = 0.75
        elif hhhyy == "混凝土块墙(灰色)":
            q_xsxs = 0.65
        else:
            q_xsxs =0.5
        print(q_xsxs)

    def wuding_button(self):
        global derta_tfps#夏季室外计算日平均温度
        global derta_tfpn
        global derta_tfpe
        global derta_tfpw
        global derta_tfpsp
        hhh_1 = self.qiangmian_2.currentText()
        global w_xsxs  # 屋顶外表面的太阳辐射热吸收系数
        if hhh_1 == "红瓦屋面(红色)旧":
            w_xsxs = 0.56
        elif hhh_1 == "红褐色瓦屋面(红褐色)旧":
            w_xsxs = 0.7
        elif hhh_1 == "灰瓦屋面(浅灰色)旧":
            w_xsxs = 0.52
        elif hhh_1 == "石板瓦(银灰色)旧":
            w_xsxs = 0.75
        elif hhh_1 == "水泥屋面(青灰色)旧":
            w_xsxs = 0.74
        elif hhh_1 ==  "浅色油毛毡(浅黑色)粗糙，新":
            w_xsxs = 0.72
        elif hhh_1 == "黑色油毛毡(深黑色)粗糙，新":
            w_xsxs = 0.86
        print(w_xsxs)


        derta_tfps = (jp_s * q_xsxs)/wqhrxh
        derta_tfpn = (jp_n * q_xsxs)/wqhrxh
        derta_tfpe = (jp_e * q_xsxs)/wqhrxh
        derta_tfpw = (jp_w * q_xsxs)/wqhrxh
        derta_tfpsp = (jp_sp * w_xsxs)/wqhrxh

        self.tainanle.setEnabled(True)

        # print(derta_tfps,derta_tfpn,derta_tfpe,derta_tfpw,derta_tfpsp)

    def tainanle1(self):
        self.zuihzonglea.setEnabled(True)
        self.tainanle_win = MyMainWindow10()
        self.tainanle_win.show()

    def zuizhong(self):
        global dertatw_w
        global dertatw_s77
        global dertatw_n77
        global dertatw_e77
        global dertatw_we77
        global cs
        global beita
        global Q_zuizhong1
        Q_zuizhong1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        dertatw_w=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        dertatw_s77=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        dertatw_n77=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        dertatw_e77=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        dertatw_we77=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        global Q_qiangorwu_wu
        global Q_qiangorwu_qiang
        Q_qiangorwu_wu = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        Q_qiangorwu_qiang = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        list_25or20=['福州','广州','台北','南宁','贵阳','昆明',"海口"]
        list_30or35=['济南','郑州','西安','兰州','西宁','南京','上海','杭州','合肥','南昌','武汉','成都','重庆','拉萨','长沙']
        list_40or45=['长春','哈尔滨','乌鲁木齐','石家庄','呼和浩特','沈阳','北京','天津','太原','银川','大连']
        if cs in list_25or20:
            if beita<=0.3:
                dertatw_w = [-7.2,-7.6,-7.9,-8.1,-8.3,-8.5,-7.4,-5.1,-2.4,0.1,2.3,3.6,4.8,5.0,4.6,3.3,1.4,-1.0,-3.4,-5.1,-5.7,-6.2,-6.6,-7.0]
            elif 0.3<beita<=0.4:

                dertatw_w = [-8.9,-9.5,-9.8,-10.1,-10.4,-10.7,-9.2,-5.9,-2.1,1.3,4.4,6.3,7.9,8.2,7.7,5.8,3.1,-0.2,-3.6,-5.9,-6.7,-7.4,-8,-8.5]
            elif 0.4<beita<=0.5:

                dertatw_w = [-10.6,-11.3,-11.8,-12.2,-12.6,-12.9,-10.9,-6.8,-1.9,2.5,6.5,8.9,11.0,11.4,10.7,8.3,4.9,0.6,-3.8,-6.7,-7.8,-8.7,-9.4,-10.1]
            elif 0.5<beita<=0.6:

                dertatw_w = [-12.3,-13.2,-13.7,-14.2,-14.7,-15,-12.7,-7.6,-1.7,3.7,8.6,11.6,14.1,14.6,13.8,10.8,6.6,1.5,-4,-7.5,-8.9,-10,-10.9,-11.7]
            elif 0.6<beita:

                dertatw_w = [-14,-15,-15.7,-16.3,-16.8,-17.2,-14.5,-8.4,-1.4,4.9,10.8,14.3,17.2,17.8,16.8,13.3,8.3,2.3,-4.1,-8.4,-9.9,-11.3,12.3,13.3]
        elif cs in list_30or35:
            if beita<=0.3:
                dertatw_w = [-7.3,-7.6,-7.9,-8.1,-8.3,-8.5,-7.2,-4.9,-2.3,0,2.2,3.7,4.6,4.9,4.6,3.2,1.4,-0.8,-3.2,-5.1,-5.7,-6.2,-6.6,-7]
            elif 0.3<beita<=0.4:
                dertatw_w = [-9,-9.5,-9.8,-10.2,-10.5,-10.7,-8.9,-5.6,-2.1,1.2,4.3,6.3,7.6,8.1,7.6,5.7,3.2,0.1,-3.3,-5.9,-6.8,-7.5,-8.1,-8.6]
            elif 0.4<beita<=0.5:
                dertatw_w = [-10.8,-11.4,-11.8,-12.2,-12.6,-12.9,-10.6,-6.4,-1.8,2.5,6.4,9,10.7,11.2,10.6,8.2,4.9,1,-3.4,-6.7,-7.8,-8.7,-9.5,-10.2]
            elif 0.5<beita<=0.6:
                dertatw_w = [-12.4,-13.2,-13.8,-14.3,-14.7,-15.1,-12.3,-7.2,-1.5,3.8,8.5,11.7,13.7,14.4,13.6,10.7,6.7,1.8,-3.5,-7.6,-8.9,-10,-10.9,-11.8]
            elif 0.6<beita:
                dertatw_w = [-14.1,-15.1,-15.7,-16.3,-16.9,-17.3,-13.9,-7.9,-1.2,4.9,10.6,14.4,16.7,17.5,16.6,13.2,8.5,2.7,-3.6,-8.4,-10,-11.3,-12.4,-13.1]

        elif cs in list_40or45:
            if beita<= 0.3:
                dertatw_w = [-7.2,-7.6,-7.9,-8.1,-8.3,-8.5,-6.7,-4.5,-2.2,-0.1,1.9,3.3,4.2,4.5,4.2,3,1.4,-0.5,-2.8,-5,-5.7,-6.2,-6.6,-6.9]
            elif 0.3 < beita <= 0.4:
                dertatw_w = [-8.9,-9.4,-9.8,-10.1,-10.4,-10.7,-8.2,-5.2,-1.9,1.1,3.9,5.8,7,7.5,7,5.4,3.2,0.4,-2.7,-5.9,-6.7,-7.4,-8,-8.5]
            elif 0.4 < beita <= 0.5:
                dertatw_w = [-10.6,-11.3,-11.7,-12.2,-12.5,-12.9,-9.7,-5.8,-1.6,2.3,5.9,8.3,9.9,10.4,9.9,7.8,4.9,1.4,-2.6,-6.7,-7.8,-8.7,-9.4,-10.3]
            elif 0.5 < beita <= 0.6:
                dertatw_w = [-12.3,-13.1,-13.7,-14.2,-14.7,-15,-11.7,-6.4,-1.2,3.5,7.8,10.8,12.7,13.4,12.7,10.2,6.7,2.4,-2.5,-7.5,-8.8,-9.9,-10.9,-11.2]
            elif 0.6 < beita:
                dertatw_w = [-14,-15,-15.6,-16.2,-16.8,-17.2,-12.7,-7,-0.9,4.7,9.8,13.4,15.6,16.4,15.6,12.7,8.5,3.4,-2.4,-8.3,-9.9,-11.2,-12.3,-13.3]

    ###以上是屋顶
    ###以下是墙体
        list11_25or20=['福州','广州','台北','南宁','贵阳','昆明',"海口"]
        list11_30or35=['济南','郑州','西安','兰州','西宁','南京','上海','杭州','合肥','南昌','武汉','成都','重庆','拉萨']
        list11_40or45=['长春','哈尔滨','乌鲁木齐','石家庄','呼和浩特','沈阳','北京','天津','太原','银川','大连']
        global zeinan
        if cs in list11_25or20:
            if zeinan <= 0.3:
                dertatw_s77 = [-1.5,-1.8,-2,-2.1,-2.3,-2.4,-2,-1.2,-0.4,0.4,1.3,2.2,2.8,3,2.8,2.5,2,1.5,0.7,0,-0.5,-0.8,-1.1,-1.3]
                dertatw_n77 = [-1.7,-2,-2.1,-2.3,-2.5,-2.6,-1.4,-0.2,0.4,0.7,1,1.5,1.9,2.2,2.3,2.5,2.6,2.5,1.4,-0.1,-0.6,-0.9,-1.2,-1.5]
                dertatw_we77 = [-2.3,-2.7,-2.9,-3.2,-3.3,-3.5,-3.1,-2.3,-1.5,-0.8,-0.2,0.4,0.8,3.3,5.4,6.8,6.9,5.9,2.7,-0.3,-0.9,-1.4,-1.7,-2.1]
                dertatw_e77 = [-2.7,-3,-3.2,-3.4,-3.5,-3.7,-1,2.5,4.4,5.2,4.8,3.5,1.8,2,1.9,1.7,1.2,0.6,-0.2,-1,-1.5,-1.9,-2.2,-2.5]
            elif 0.3<zeinan <= 0.4:
                dertatw_s77 = [-2,-2.4,-2.6,-2.9,-3.1,-3.2,-2.6,-1.5,-0.5,0.6,1.7,2.9,3.7,4,3.7,3.3,2.6,2,1,0,-0.6,-1.1,-1.4,-1.8]
                dertatw_n77 = [-2.2,-2.6,-2.9,-3.1,-3.3,-3.5,-1.9,-0.2,0.5,0.9,1.3,2.1,2.6,3,3.1,3.4,3.5,3.4,1.8,-0.2,-0.8,-1.2,-1.6,-2]
                dertatw_we77 = [-3.1,-3.6,-3.9,-4.2,-4.5,-4.7,-4.1,-3.1,-2.1,-1,-0.2,0.5,1.1,4.3,7.2,9.1,9.2,7.8,3.6,-0.4,-1.2,-1.8,-2.3,-2.8]
                dertatw_e77 = [-3.6,-4,-4.2,-4.5,-4.7,-4.9,-1.3,3.4,5.9,7,6.3,4.7,2.4,2.6,2.6,2.3,1.5,0.8,-0.3,-1.4,-2,-2.5,-2.9,-3.3]
            elif 0.4<zeinan<=0.5:
                dertatw_s77 = [-2.5,-3,-3.3,-3.6,-3.8,-4,-3.3,-1.9,-0.6,0.7,2.1,3.7,4.6,5,4.6,4.1,3.3,2.5,1.2,-0.1,-0.8,-1.3,-1.8,-2.2]
                dertatw_n77 = [-2.8,-3.3,-3.6,-3.9,-4.2,-4.4,-2.3,-0.3,0.7,1.2,1.6,2.6,3.2,3.7,3.9,4.2,4.3,4.2,2.3,-0.2,-1,-1.6,-2,-2.5]
                dertatw_we77 = [-3.9,-4.5,-4.9,-5.3,-5.6,-5.8,-5.2,-3.9,-2.6,-1.3,-0.3,0.7,1.3,5.4,9,11.4,11.5,9.8,4.5,-0.5,-1.5,-2.3,-2.9,-3.5]
                dertatw_e77 = [-4.5,-5,-5.3,-5.6,-5.9,-6.1,-1.6,4.2,7.3,8.7,7.9,5.9,3,3.3,3.2,2.9,1.9,1.1,-0.4,-1.7,-2.5,-3.2,-3.7,-4.2]
            elif 0.5<zeinan <= 0.6:
                dertatw_s77 = [-3,-3.6,-4,-4.2,-4.6,-4.8,-4,-2.4,-0.8,0.8,2.6,4.4,5.6,6,5.6,5,4,3,1.4,0,-1,-1.6,-2.2,-2.6]
                dertatw_n77= [-3.4,-4,-4.1,-4.6,-5,-5.2,-5.2,-2.8,-0.4,0.8,1.4,2,3,3.8,4.4,4.6,5,5.2,5,2.8,-0.2,-1.2,-1.8,-2.4,-3]
                dertatw_we77 = [-4.6,-5.4,-5.8,-6.4,-6.6,-7,-6.2,-4.6,-2.6,-1.6,-0.4,0.8,1.6,6.6,10.8,13.6,13.8,11.8,5.4,-0.6,-1.8,-2.8,-3.4,-4.1]
                dertatw_e77 = [-5.4,-6,-6.4,-6.8,-7,-7.4,-2,5,8.8,10.4,9.6,7,3.6,4,3.8,3.4,2.4,1.2,-0.4,-2,-3,-3.8,-4.4,-5]
            elif 0.6<zeinan:
                dertatw_s77 = [-3.5,-4.2,-4.6,-5,-5.4,-5.6,-4.6,-2.7,-0.9,1,3,5.1,6.5,7,6.5,5.8,4.6,3.5,1.7,0,-1.1,-1.9,-2.5,-3.1]
                dertatw_n77 = [-3.9,-4.6,-5,-5.4,-5.8,-6.1,-3.1,-0.4,0.9,1.6,2.3,3.6,4.5,5.2,5.4,5.9,6.1,5.9,3.2,-0.3,-1.4,-2.1,-3.8,-3.5]
                dertatw_we77 = [-5.4,-6.3,-6.8,-7.4,-7.8,-8.2,-7.2,-5.4,-3.6,-1.8,-0.4,0.9,1.9,7.6,12.6,15.9,16.1,13.7,6.3,-0.7,-2.1,-3.2,-4,-4.9]
                dertatw_e77= [-6.3,-7,-7.4,-7.9,-8.2,-8.6,-2.3,5.9,10.1,12.2,11.1,8.2,4.2,4.6,4.5,4,2.7,1.4,-0.5,-2.4,-3.5,-4.4,-5.1,-5.8]
        elif cs in list11_30or35:
            if zeinan <= 0.3:
                dertatw_s77 = [-1.7,-2,-2.2,-2.4,-2.5,-2.6,-2.1,-1.4,-0.6,0.4,1.7,2.7,3.4,3.6,3.3,2.6,1.9,1.4,0.7,-0.2,-0.6,-1,-1.3,-1.5]
                dertatw_n77 = [-1.6,-1.9,-2.1,-2.3,-2.4,-2.5,-1.1,-0.2,0.1,0.4,1,1.6,2,2.3,2.4,2.3,2.3,2.4,1.6,-0.1,-0.5,-0.9,-1.2,-1.4]
                dertatw_we77 = [-2.3,-2.7,-2.9,-3.2,-3.4,-3.5,-3,-2.3,-1.6,-0.8,-0.2,0.3,0.7,3.2,5.3,6.8,6.9,6,3.2,-0.3,-0.9,-1.4,-1.8,-2.1]
                dertatw_e77 = [-2.7,-3,-3.2,-3.4,-3.6,-3.7,-0.5,2.7,4.5,5.2,4.7,3.5,1.7,1.9,1.9,1.7,1.1,0.6,-0.2,-1.1,-1.5,-1.9,-2.2,-2.5]
            elif 0.3 < zeinan <= 0.4:
                dertatw_s77 = [-2.3,-2.7,-2.9,-3.2,-3.3,-3.5,-2.8,-1.9,-0.8,0.5,2.3,3.6,4.5,4.8,4.4,3.5,2.5,1.9,0.9,-0.3,-0.8,-1.3,-1.7,-2]
                dertatw_n77 = [-2.1,-2.5,-2.8,-3.1,-3.2,-3.3,-1.5,-0.3,0.1,0.5,1.3,2.1,2.7,3.1,3.2,3.1,3.1,3.2,2.1,-0.1,-0.7,-1.2,-1.6,-1.9]
                dertatw_we77 = [-3.1,-3.6,-3.9,-4.3,-4.5,-4.7,-4,-3.1,-2.1,-1.1,-0.3,0.4,0.9,4.3,7.1,9.1,9.2,8,4.3,-0.4,-1.2,-1.9,-2.4,-2.8]
                dertatw_e77 = [-3.6,-4,-4.3,-4.5,-4.8,-4.9,-0.7,3.6,6,6.9,6.3,4.7,2.3,2.5,2.5,2.3,1.5,0.8,-0.3,-1.5,-2,-2.5,-2.9,-3.3]
            elif 0.4< zeinan<=0.5:
                dertatw_s77 = [-2.8,-3.3,-3.6,-3.9,-4.2,-4.4,-3.5,-2.3,-1,0.7,2.8,4.6,5.6,6,5.6,4.3,3.2,2.4,1.1,-0.3,-1,-1.6,-2.1,-2.5]
                dertatw_n77 = [-2.7,-3.2,-3.5,-3.8,-4,-4.2,-1.9,-0.3,0.2,0.7,1.7,2.6,3.3,3.8,4,3.8,3.8,4,2.6,-0.1,-0.9,-1.5,-1.9,-2.4]
                dertatw_we77 = [-3.9,-4.5,-4.9,-5.3,-5.6,-5.9,-5.2,-3.9,-2.6,-1.3,-0.3,0.6,1.2,5.3,8.9,11.3,11.5,10,5.4,-0.5,-1.5,-2.3,-2.9,-3.5]
                dertatw_e77 = [-4.5,-5.1,-5.4,-5.7,-6,-6.2,-0.8,4.5,7.5,8.7,7.9,5.8,2.9,3.2,3.2,2.8,1.9,1.1,-0.3,-1.8,-2.6,-3.2,-2.7,-4.1]
            elif 0.5 < zeinan <= 0.6:
                dertatw_s77 = [-3.4,-4,-4.4,-4.8,-5,-5.2,-4.2,-2.8,-1.2,0.8,3.4,5.4,6.8,7.2,6.6,5.2,3.8,2.8,1.4,-0.4,-1.2,-2,-2.6,-3]
                dertatw_n77 = [-3.2,-3.8,-4.2,-4.6,-4.8,-5,-2.2,-0.4,0.2,0.8,2,3.2,4,4.6,2.8,4.6,4.6,2.8,3.2,-0.2,-1,-1.8,-2.4,-2.8]
                dertatw_we77 = [-4.6,-5.4,-5.8,-6.4,-6.8,-7,-6,-4.6,-3.2,-1.6,-0.4,0.6,1.4,6.4,10.6,13.6,13.8,12,6.4,-0.6,-1.8,-2.8,-3.6,-4.2]
                dertatw_e77 = [-5.4,-6,-6.4,-6.8,-7.2,-7.4,-1,5.4,9,10.4,9.4,7,3.4,3.8,3.8,3.4,2.2,1.2,-0.4,-2.2,-3,-3.8,-4.4,-5]
            elif 0.6<zeinan:
                dertatw_s77 = [-3.9,-4.7,-5.1,-5.6,-5.8,-6.1,-4.9,-3.3,-1.4,0.9,4,6.3,7.9,8.4,7.7,6.1,4.4,3.3,1.6,-0.5,-1.4,-2.3,-3,-3.5]
                dertatw_n77 = [-3.7,-4.4,-4.9,-5.4,-5.6,-5.8,-2.6,-0.5,0.2,0.9,2.3,3.7,4.7,5.4,5.6,5.4,5.4,5.6,3.7,-0.2,-1.2,-2.1,-2.8,-3.3]
                dertatw_we77 = [-5.4,-6.3,-6.8,-7.5,-7.9,-8.2,-7,-5.4,-3.7,-1.9,-0.5,0.7,1.6,7.5,12.4,15.9,16.1,14,7.5,-0.7,-2.1,-3.3,-4.2,-4.9]
                dertatw_e77 = [-6.3,-7,-7.5,-7.9,-8.4,-8.6,-1.2,6.3,10.5,12.1,11,8.2,4,4.4,4.4,4,2.6,1.4,-0.5,-2.4,-3.5,-4.4,-5.1,-5.8]
        elif cs in list11_40or45:
            if zeinan <= 0.3:
                dertatw_s77 = [-2.2,-2.5,-2.6,-2.9,-3,-3.2,-2.5,-1.9,-1,0.9,2.5,3.8,4.6,4.7,4.4,3.4,1.9,1.2,0.5,-0.5,-1,-1.3,-1.7,-1.9]
                dertatw_n77 = [-1.5,-1.8,-2,-2.2,-2.3,-2.5,-0.5,-0.3,-0.4,0.4,1,1.4,1.9,2.2,2.3,2.2,1.7,2.2,2.1,0,-0.5,-0.8,-1.1,-1.3]
                dertatw_we77 = [-2.4,-2.8,-3.1,-3.3,-3.5,-3.7,-2.6,-2.5,-1.8,-1.1,-0.5,0,0.4,2.9,5.2,6.8,7.3,6.9,4.9,-0.3,-0.9,-1.4,-1.8,-2.1]
                dertatw_e77 = [-2.9,-3.2,-3.4,-3.6,-3.8,-3.9,1.1,3.7,5,5.5,4.8,3.4,1.6,1.7,1.7,1.4,0.9,0.5,-0.2,-1.2,-1.7,-2.1,-2.4,-2.7]
            elif 0.3 < zeinan <= 0.4:
                dertatw_s77 = [-2.9,-3.3,-3.5,-3.8,-4,-4.2,-3.4,-2.5,-1.3,1.2,3.4,5,6.1,6.3,5.8,4.6,2.5,1.6,0.7,-0.6,-1.3,-1.8,-2.2,-2.6]
                dertatw_n77 = [-2,-2.4,-2.6,-2.9,-3.1,-3.4,-0.7,-0.4,-0.5,0.5,1.3,1.9,2.5,2,9,3,2.9,2.3,2.9,2.8,0,-0.6,-1,-1.4,-1.8]
                dertatw_we77 = [-3.2,-3.8,-4.1,-4.4,-4.6,-4.9,-4.1,-3.3,-2.4,-1.4,-0.7,-0.1,0.5,3.9,7,9.1,9.8,9.2,6.6,-0.4,-1.2,-1.8,-2.4,-2.9]
                dertatw_e77 = [-3.8,-4.2,-4.6,-4.5,-4.8,-5,-5.2,1.4,5,6.7,7.3,6.3,4.6,2.1,2.2,1.7,1.2,0.6,-0.2,-1.6,-2.2,-2.8,-3.2,-3.6]
            elif 0.4< zeinan<=0.5:
                dertatw_s77 = [-3.6,-4.1,-4.4,-4.8,-5,-5.3,-4.2,-3.1,-1.6,1.5,4.2,6.3,7.6,7.9,7.3,5.7,3.1,2,0.9,-0.8,-1.6,-2.2,-2.8,-3.2]
                dertatw_n77 = [-2.5,-3,-3.3,-3.6,-3.9,-4.2,-0.9,-0.5,-0.6,0.6,1.6,2.4,3.1,3.6,3,8,3.6,3.9,3.6,3.5,0,-0.8,-1.3,-1.8,-2.2]
                dertatw_we77 = [-4,-4.7,-5.1,-5.5,-5.8,-6.1,-5.1,-4.1,-3,-1.8,-0.9,-0.1,0.6,4.9,8.7,11.4,12.2,11.5,8.2,-0.5,-1.5,-2.3,-3,-3.6]
                dertatw_e77 = [-4.8,-5.3,-5.7,-6,-6.3,-6.5,1.8,6.2,8.4,9.1,8,5.7,2.6,2.8,2.8,2.4,1.5,0.8,-0.3,-2,-2.8,-3.5,-4,-4.5]
            elif 0.5 < zeinan <= 0.6:
                dertatw_s77 = [-4.4,-5,-5.2,-5.8,-6,-6.4,-5,-3.8,-2,1.8,5,7.6,9.2,9.4,8.8,6.8,3.8,2.4,1,-1,-2,-2.6,-3.4,-3.8]
                dertatw_n77 = [-3,-3.6,-4,-4.4,-4.6,-5,-1,-0.6,-0.8,0.8,2,2.8,3.8,4.4,4.6,4.4,3.4,4.4,4.2,0,-1,-1.6,-2.2,-2.6]
                dertatw_we77 = [-4.8,-5.6,-6.2,-6.6,-7,-7.4,-5.2,-5,-3.6,-2.2,-1,-0.1,0.8,5.8,10.4,13.6,14.6,13.8,9.8,-0.6,-1.8,-2.8,-3.6,-4.1]
                dertatw_e77 = [-5.8,-6.2,-6.8,-7.2,-7.6,-7.8,2.2,7.4,10,11,9.6,6.8,3.2,3.4,3.4,2.8,1.8,1,-0.4,-2.4,-3.4,-4.1,-4.8,-5.4]
            elif 0.6<zeinan:
                dertatw_s77 = [-5.1,-5.8,-6.2,-6.7,-7,-7.4,-5.9,-4.4,-2.3,2.1,5.9,8.8,10.7,11,10.2,8,4.4,2.8,1.2,-1.1,-2.3,-3.1,-3.9,-4.5]
                dertatw_n77 = [-3.5,-4.2,-4.6,-5.1,-5.4,-5.9,-1.2,-0.7,-0.9,0.9,2.3,3.3,4.4,5.1,5.3,5.1,4,5.1,4.9,0,-1.1,-1.8,-2.5,-3.1]
                dertatw_we77 = [-5.6,-6.6,-7.2,-7.7,-8.1,-8.6,-6.7,-5.8,-4.4,-2.5,-1.2,-0.1,0.9,6.8,12.2,15.9,17.1,16.1,11.5,-0.7,-2.1,-3.2,-4.2,-5]
                dertatw_e77 = [-6.6,-7.4,-8,-8.4,-8.8,-9.1,2.5,8.7,11.7,12.8,11.1,8,3.7,3.9,3.9,3.1,2.1,1.1,-0.4,-2.8,-3.9,-4.9,-5.6,-6.3]
        global xia_pjfs
        for i in range(len(Q_qiangorwu_wu)):
            Q_qiangorwu_wu[i] = k * m_wuding * (xia_shiwpj + derta_tfpsp +dertatw_w[i] -float(xiaji_wendu))
        for i in range(len(Q_qiangorwu_qiang)):
            Q_qiangorwu_qiang[i] = k1*m_nanqiang*(xia_shiwpj+derta_tfps+dertatw_s77[i]-float(xiaji_wendu))+k1*m_beiqiang*(xia_shiwpj+derta_tfpn+dertatw_n77[i]-float(xiaji_wendu))+ k1*m_dongqiang*(xia_shiwpj+derta_tfpe+dertatw_e77[i]-float(xiaji_wendu))+k1*m_xiqiang*(xia_shiwpj+derta_tfpw+dertatw_we77[i]-float(xiaji_wendu))
        print(Q_qiangorwu_wu)
        print(Q_qiangorwu_qiang)
        for i in range(len(Q_qiangorwu_wu)):
            Q_zuizhong1[i] = Q_qiangorwu_wu[i] + Q_qiangorwu_qiang[i]

        print(dertatw_w)
        print(dertatw_s77)
        print(dertatw_n77)
        print(dertatw_we77)
        print(dertatw_e77)
        self.close()

class Ui_Form45(QWidget, Ui_Form45):#人体的散热Q_ren
    def __init__(self):
        # super(Ui_Form4, self).__init__(parent)
        super().__init__()
        self.setupUi(self)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.queding_r.clicked.connect(self.rs_button)  # 确定房间人数


    def rs_button(self):
        global input_renshu
        global qx #每名成年男子的全热散热量。

        global Q_ren

        input_renshu = self.renshu_1.text()
        #下面这个注释是关于QRadiobutton的相关操作。
        # if self.b_jingzuo.isChecked():
        #     if int(xiaji_wendu) == 16:
        #         qx = 116
        #     elif int(xiaji_wendu) == 17:
        #         qx = 113
        #     elif int(xiaji_wendu) == 18:
        #         qx = 112
        #     elif int(xiaji_wendu) == 19:
        #         qx = 110
        #     elif int(xiaji_wendu) == 20:
        #         qx = 110
        #     elif int(xiaji_wendu) == 21:
        #         qx = 108
        #     elif int(xiaji_wendu) == 22:
        #         qx = 108
        #     elif int(xiaji_wendu) == 23:
        #         qx = 108
        #     elif int(xiaji_wendu) == 24:
        #         qx = 108
        #     elif int(xiaji_wendu) == 25:
        #         qx = 108
        #     elif int(xiaji_wendu) == 26:
        #         qx = 108
        #     elif int(xiaji_wendu) == 27:
        #         qx = 108
        #     elif int(xiaji_wendu) == 28:
        #         qx = 108
        #     elif int(xiaji_wendu) == 29:
        #         qx = 108
        #     elif int(xiaji_wendu) == 30:
        #         qx = 108
        #     print(qx)
        #
        #     c11 = self.b_jingzuo.text()
        #     # c11 = 10
        #     print(c11)
        # elif self.b_jq.isChecked():
        #     c11 = self.b_jq.text()
        #     c11 = 20
        #     # print(c11)
        # elif self.b_qing.isChecked():
        #     c11 = self.b_qing.text()
        #     c11 = 30
        #     # print(c11)
        # elif self.b_zhong.isChecked():
        #     c11 = self.b_zhong.text()
        #     c11 = 30
        # elif self.c3.isChecked():
        #     c11 = self.c3.text()
        #     c11 = 30
        #
        # print(int(input_renshu))
        # self.close()#
        laoqiang = self.laoqiang_com.currentText()
        changsuo = self.changsuo_com.currentText()
        if laoqiang == '静坐':
            if int(xiaji_wendu) == 16:
                qx = 116
            elif int(xiaji_wendu) == 17:
                qx = 113
            elif int(xiaji_wendu) == 18:
                qx = 112
            elif int(xiaji_wendu) == 19:
                qx = 110
            elif int(xiaji_wendu) == 20:
                qx = 110
            elif int(xiaji_wendu) == 21:
                qx = 108
            elif int(xiaji_wendu) == 22:
                qx = 108
            elif int(xiaji_wendu) == 23:
                qx = 108
            elif int(xiaji_wendu) == 24:
                qx = 108
            elif int(xiaji_wendu) == 25:
                qx = 108
            elif int(xiaji_wendu) == 26:
                qx = 108
            elif int(xiaji_wendu) == 27:
                qx = 108
            elif int(xiaji_wendu) == 28:
                qx = 108
            elif int(xiaji_wendu) == 29:
                qx = 108
            elif int(xiaji_wendu) == 30:
                qx = 108
        if laoqiang == '极轻等劳动':
            if int(xiaji_wendu) == 16:
                qx = 142
            elif int(xiaji_wendu) == 17:
                qx = 141
            elif int(xiaji_wendu) == 18:
                qx = 140
            elif int(xiaji_wendu) == 19:
                qx = 140
            elif int(xiaji_wendu) == 20:
                qx = 137
            elif int(xiaji_wendu) == 21:
                qx = 136
            elif int(xiaji_wendu) == 22:
                qx = 135
            elif int(xiaji_wendu) == 23:
                qx = 134
            elif int(xiaji_wendu) == 24:
                qx = 134
            elif int(xiaji_wendu) == 25:
                qx = 134
            elif int(xiaji_wendu) == 26:
                qx = 134
            elif int(xiaji_wendu) == 27:
                qx = 134
            elif int(xiaji_wendu) == 28:
                qx = 134
            elif int(xiaji_wendu) == 29:
                qx = 134
            elif int(xiaji_wendu) == 30:
                qx = 134
        if laoqiang == '轻等劳动':
            if int(xiaji_wendu) == 16:
                qx = 188
            elif int(xiaji_wendu) == 17:
                qx = 186
            elif int(xiaji_wendu) == 18:
                qx = 185
            elif int(xiaji_wendu) == 19:
                qx = 183
            elif int(xiaji_wendu) == 20:
                qx = 183
            elif int(xiaji_wendu) == 21:
                qx = 181
            elif int(xiaji_wendu) == 22:
                qx = 181
            elif int(xiaji_wendu) == 23:
                qx = 182
            elif int(xiaji_wendu) == 24:
                qx = 182
            elif int(xiaji_wendu) == 25:
                qx = 181
            elif int(xiaji_wendu) == 26:
                qx = 181
            elif int(xiaji_wendu) == 27:
                qx = 181
            elif int(xiaji_wendu) == 28:
                qx = 182
            elif int(xiaji_wendu) == 29:
                qx = 182
            elif int(xiaji_wendu) == 30:
                qx = 182
        if laoqiang == '中等劳动':
            if int(xiaji_wendu) == 16:
                qx = 236
            elif int(xiaji_wendu) == 17:
                qx = 236
            elif int(xiaji_wendu) == 18:
                qx = 236
            elif int(xiaji_wendu) == 19:
                qx = 236
            elif int(xiaji_wendu) == 20:
                qx = 235
            elif int(xiaji_wendu) == 21:
                qx = 235
            elif int(xiaji_wendu) == 22:
                qx = 235
            elif int(xiaji_wendu) == 23:
                qx = 235
            elif int(xiaji_wendu) == 24:
                qx = 235
            elif int(xiaji_wendu) == 25:
                qx = 235
            elif int(xiaji_wendu) == 26:
                qx = 235
            elif int(xiaji_wendu) == 27:
                qx = 235
            elif int(xiaji_wendu) == 28:
                qx = 235
            elif int(xiaji_wendu) == 29:
                qx = 235
            elif int(xiaji_wendu) == 30:
                qx = 235
        if laoqiang == '重度劳动':
            if int(xiaji_wendu) == 16:
                qx = 407
            elif int(xiaji_wendu) == 17:
                qx = 407
            elif int(xiaji_wendu) == 18:
                qx = 407
            elif int(xiaji_wendu) == 19:
                qx = 407
            elif int(xiaji_wendu) == 20:
                qx = 407
            elif int(xiaji_wendu) == 21:
                qx = 407
            elif int(xiaji_wendu) == 22:
                qx = 407
            elif int(xiaji_wendu) == 23:
                qx = 407
            elif int(xiaji_wendu) == 24:
                qx = 407
            elif int(xiaji_wendu) == 25:
                qx = 407
            elif int(xiaji_wendu) == 26:
                qx = 407
            elif int(xiaji_wendu) == 27:
                qx = 407
            elif int(xiaji_wendu) == 28:
                qx = 407
            elif int(xiaji_wendu) == 29:
                qx = 407
            elif int(xiaji_wendu) == 30:
                qx = 407
        global qjxs_1  # 不同场所的群集系数
        if changsuo == '影剧院':
            # global qjxs_1
            qjxs_1 = 0.89
        elif changsuo == '旅店':
            # global qjxs_1
            qjxs_1 = 0.93
        elif changsuo == '百货商场（售货）':
            # global qjxs_1
            qjxs_1 = 0.89
        elif changsuo == '图书馆阅览室':
            # global qjxs_1
            qjxs_1 = 0.96
        elif changsuo == '纺织厂':
            # global qjxs_1
            qjxs_1 = 0.9
        elif changsuo == '铸造车间':
            # global qjxs_1
            qjxs_1 = 1.0
        elif changsuo == '炼钢车间':
            # global qjxs_1
            qjxs_1 = 1.0
        elif changsuo == '体育馆':
            # global qjxs_1
            qjxs_1 = 0.92
        avav = int(input_renshu)
        Q_ren = avav * qjxs_1 * qx
        print(Q_ren)
        self.close()

class Ui_Form5(QMainWindow, Ui_Form5):#照明设备

    def __init__(self, parent=None):
        super(Ui_Form5, self).__init__(parent)
        self.setupUi(self)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.pushButton.clicked.connect(self.dengguang_button)  # 确定灯光照明设备Q_dengguang

    def dengguang_button(self):
        # global input_dengguang
        global n3
        global Q_dengguang
        n3 = 0.75  # 同时使用系数n3
        self.input_dengguang = float(self.lineEdit.text())
        self.input_dengguanggeshu = float(self.lineEdit_2.text())
        deng = self.comboBox.currentText()
        if deng == '明装白炽灯':
            Q_dengguang = 1000 * self.input_dengguang * n3 * self.input_dengguanggeshu
            print(Q_dengguang)
        elif deng == '荧光灯（整流器在空调房间内部）':
            self.n6 = 1.2#整流器消耗功率系数n6
            self.n7 = 1#安装系数
            Q_dengguang = 1000 * self.input_dengguang * self.n6 * self.n7 * n3*self.input_dengguanggeshu
            print(Q_dengguang)
        elif deng == '荧光灯（整流器在吊顶内，且灯罩有小孔）':
            self.n6 = 1#整流器消耗功率系数n6
            self.n7 = 0.55#安装系数
            Q_dengguang = 1000 * self.input_dengguang * self.n6 * self.n7 * n3*self.input_dengguanggeshu
            print(Q_dengguang)
        elif deng == '荧光灯（整流器在吊顶内，且灯罩无小孔））':
            self.n6 = 1#整流器消耗功率系数n6
            self.n7 = 0.7#安装系数
            Q_dengguang = 1000 * self.input_dengguang * self.n6 * self.n7 * n3*self.input_dengguanggeshu
            print(Q_dengguang)
        self.close()

class Ui_Form32(QWidget,Ui_Form3):#城市的选择
    # send_cs = pyqtSignal()
    def __init__(self):
        # super(Ui_Form3, self).__init__(parent)
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)


        self.queding_cheng.clicked.connect(self.cs_button)
    #     self.queding_cheng.clicked['bool'].connect(self.cs_button1)
    #
    # def cs_button1(self):
    #     self.send_cs.emit()
    def cs_button(self):

        global ttao
        global xia_shiwpj
        global dong_shiwpj
        global xia_pjfs
        global cs
        global fengsu_1,fengsu_1_5,fengsu_2,fengsu_2_5,fengsu_3,fengsu_3_5,fengsu_4

        cs = self.chengshi.currentText()
        # self.send_cs.emit(cs)

        print(cs)

        if cs == '北京':
            ttao = 0
            xia_shiwpj = 29.6
            xia_pjfs = 2.1
            dong_shiwpj = -7.6
        elif cs == '天津':
            ttao = 0
            xia_shiwpj = 29.8
            xia_pjfs = 2.2
            dong_shiwpj =-7
        elif cs == '石家庄':
            ttao = 1
            xia_shiwpj = 30.8
            xia_pjfs = 1.7
            dong_shiwpj =-6.2
        elif cs == '太原':
            ttao = -2
            xia_shiwpj = 27.8
            xia_pjfs = 1.8
            dong_shiwpj =-10.1
        elif cs == '呼和浩特':
            ttao = -4
            xia_shiwpj = 26.5
            xia_pjfs = 1.8
            dong_shiwpj =-17
        elif cs == '沈阳':
            ttao = -1
            xia_shiwpj = 28.2
            xia_pjfs = 2.6
            dong_shiwpj =-16.9
        elif cs == '长春':
            ttao = -3
            xia_shiwpj = 26.6
            xia_pjfs = 3.2
            dong_shiwpj =-21.1
        elif cs == '哈尔滨':
            ttao = -3
            xia_shiwpj = 26.8
            xia_pjfs = 3.2
            dong_shiwpj =-24.2
        elif cs == '上海':
            ttao = 1
            xia_shiwpj = 31.2
            xia_pjfs = 3.1
            dong_shiwpj =-0.3
        elif cs == '南京':
            ttao = 3
            xia_shiwpj = 31.2
            xia_pjfs = 2.6
            dong_shiwpj =-1.8
        elif cs == '杭州':
            ttao = 3
            xia_shiwpj = 32.3
            xia_pjfs = 2.4
            dong_shiwpj = 0
        elif cs == '合肥':
            ttao = 3
            xia_shiwpj = 31.4
            xia_pjfs = 2.9
            dong_shiwpj =-1.7
        elif cs == '福州':
            ttao = 2
            xia_shiwpj = 33.1
            xia_pjfs = 3
            dong_shiwpj =6.3
        elif cs == '南昌':
            ttao = 3
            xia_shiwpj = 32.7
            xia_pjfs = 2.2
            dong_shiwpj =0.7
        elif cs == '济南':
            ttao = 3
            xia_shiwpj = 30.9
            xia_pjfs = 2.8
            dong_shiwpj = -5.3
        elif cs == '郑州':
            ttao = 2
            xia_shiwpj = 30.9
            xia_pjfs = 2.2
            dong_shiwpj =-3.8
        elif cs == '武汉':
            ttao = 3
            xia_shiwpj = 32
            xia_pjfs = 2
            dong_shiwpj = -0.3
        elif cs == '长沙':
            ttao = 3
            xia_shiwpj = 32.9
            xia_pjfs = 2.1
            dong_shiwpj = 0.3
        elif cs == '广州':
            ttao = 1
            xia_shiwpj = 31.8
            xia_pjfs = 1.7
            dong_shiwpj = 8
        elif cs == '南宁':
            ttao = 1
            xia_shiwpj = 31.8
            xia_pjfs = 1.5
            dong_shiwpj = 7.6
        elif cs == '成都':
            ttao = -1
            xia_shiwpj = 28.5
            xia_pjfs = 1.2
            dong_shiwpj = 2.7
        elif cs == '贵阳':
            ttao = -3
            xia_shiwpj = 27.1
            xia_pjfs = 2.1
            dong_shiwpj = -0.3
        elif cs == '昆明':
            ttao = -6
            xia_shiwpj = 23
            xia_pjfs = 1.8
            dong_shiwpj = 3.6
        elif cs == '拉萨':
            ttao = -11
            xia_shiwpj = 19.2
            xia_pjfs = 1.8
            dong_shiwpj = -5.2
        elif cs == '西安':
            ttao = 2
            xia_shiwpj = 30.6
            xia_pjfs = 1.9
            dong_shiwpj = -3.4
        elif cs == '兰州':
            ttao = -3
            xia_shiwpj = 26.5
            xia_pjfs = 1.2
            dong_shiwpj = -9
        elif cs == '西宁':
            ttao = -8
            xia_shiwpj = 21.9
            xia_pjfs = 1.5
            dong_shiwpj = -11.4
        elif cs == '银川':
            ttao = -3
            xia_shiwpj = 27.6
            xia_pjfs = 2.1
            dong_shiwpj = -13.1
        elif cs == '乌鲁木齐':
            ttao = 1
            xia_shiwpj = 27.5
            xia_pjfs = 3
            dong_shiwpj = -19.7
        elif cs == '台北':
            ttao = 1
            xia_shiwpj = 31
            xia_pjfs = 2.8
            dong_shiwpj = 11
        elif cs == '大连':
            ttao = -2
            xia_shiwpj = 26.3
            xia_pjfs = 4.1
            dong_shiwpj = -9.8
        elif cs == '海口':
            ttao = 1
            xia_shiwpj = 32.2
            xia_pjfs = 2.3
            dong_shiwpj = 12.6
        elif cs == '重庆':
            ttao = 3
            xia_shiwpj = 31.7
            xia_pjfs = 1.5
            dong_shiwpj = 4.1
        print(ttao)
        print(xia_shiwpj)
        print(xia_pjfs)


        fengsu_1 = ['兰州','成都']
        fengsu_1_5 = ['重庆','西宁','南宁','广州','石家庄']
        fengsu_2 = ['银川','西安','拉萨','昆明','贵阳','长沙','武汉','北京','天津','郑州','南昌','太原','呼和浩特']
        fengsu_2_5 = ['海口','杭州','南京','沈阳']
        fengsu_3 = ['乌鲁木齐','台北','济南','福州','合肥','上海','长春','哈尔滨']
        fengsu_3_5 = []
        fengsu_4 = ['大连']

        self.chengshi1_win = MyMainWindow9()
        self.chengshi1_win.show()
        self.close()

class MyMainWindow7(QWidget, Ui_Form7):#玻璃窗传热形成的负荷Q_bolichuanre
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)#####有背景图片一定加这句话！！！！！
        self.setupUi(self)
        self.queding_ds.clicked.connect(self.ds_button)
        self.queding_ck.clicked.connect(self.ck_button)
        self.queding_cw.clicked.connect(self.cw_button)
        self.queding_cn.clicked.connect(self.cn_button)
        self.queding_chuangk.clicked.connect(self.boli_button)
        self.dsbl_com.currentTextChanged.connect(self.wuliao)
        self.chuangk_com.currentTextChanged.connect(self.wuliao_1)
        self.chuangw.currentTextChanged.connect(self.wuliao_2)
        self.chuangn.currentTextChanged.connect(self.wuliao_3)
        self.chuangmian.textChanged.connect(self.wuliao_4)


    def ds_button(self):
        global ds
        ds = self.dsbl_com.currentText()
        print(ds)

    def ck_button(self):
        global k_xz
        ck = self.chuangk_com.currentText()#获取窗框信息
        if ds == "单层窗玻璃":
            if ck == '全部金属':
                k_xz = 1
            elif ck =="木窗框（80%玻璃）":
                k_xz = 0.9
            elif ck == "木窗框（60%玻璃）":
                k_xz = 0.8
            else:
                k_xz = 1
        elif ds == '双层窗玻璃':
            if ck == '全部金属':
                k_xz = 1
            elif ck == "木窗框（80%玻璃）":
                k_xz = 0.95
            elif ck == "木窗框（60%玻璃）":
                k_xz = 0.85
            else:
                k_xz = 1.2
        print(k_xz)


    def cw_button(self):
        global cw
        cw = self.chuangw.currentText()
        print(cw)#如果print（int（cw））就会出错。

    def cn_button(self):
        global k_danchuang
        cn = self.chuangn.currentText()
        if ds == "单层窗玻璃":#注意：困扰了将近一天。一定加引号，他是文本，不是整数！
            if cw == "11.6":
                if cn =="5.8":
                    k_danchuang =3.87
                elif cn == '6.4':
                    k_danchuang = 4.13
                elif cn == '7.0':
                    k_danchuang = 4.36
                elif cn == '7.6':
                    k_danchuang = 4.58
                elif cn == '8.2':
                    k_danchuang = 4.79
                elif cn == '8.7':
                    k_danchuang = 4.99
                elif cn == '9.4':
                    k_danchuang = 5.16
                elif cn == '9.9':
                    k_danchuang = 5.34
                elif cn == '10.5':
                    k_danchuang = 5.51
                else:
                    k_danchuang = 5.66
            elif cw == '12.8':
                if cn == '5.8':
                    k_danchuang = 4
                elif cn == '6.4':
                    k_danchuang = 4.27
                elif cn == '7.0':
                    k_danchuang = 4.51
                elif cn == '7.6':
                    k_danchuang = 4.76
                elif cn == '8.2':
                    k_danchuang = 4.98
                elif cn == '8.7':
                    k_danchuang = 5.19
                elif cn == '9.4':
                    k_danchuang = 5.38
                elif cn == '9.9':
                    k_danchuang = 5.57
                elif cn == '10.5':
                    k_danchuang = 5.76
                elif cn == '11.1':
                    k_danchuang = 5.93
            elif cw == '14.0':
                if cn == '5.8':
                    k_danchuang = 4.11
                elif cn == '6.4':
                    k_danchuang = 4.38
                elif cn == '7.0':
                    k_danchuang = 4.65
                elif cn == '7.6':
                    k_danchuang = 4.91
                elif cn == '8.2':
                    k_danchuang = 5.14
                elif cn == '8.7':
                    k_danchuang = 5.37
                elif cn == '9.4':
                    k_danchuang = 5.58
                elif cn == '9.9':
                    k_danchuang = 5.79
                elif cn == '10.5':
                    k_danchuang = 5.81
                elif cn == '11.1':
                    k_danchuang = 6.16
            elif cw == '15.1':
                if cn == '5.8':
                    k_danchuang = 4.2
                elif cn == '6.4':
                    k_danchuang = 4.49
                elif cn == '7.0':
                    k_danchuang = 4.78
                elif cn == '7.6':
                    k_danchuang = 5.04
                elif cn == '8.2':
                    k_danchuang = 5.29
                elif cn == '8.7':
                    k_danchuang = 5.54
                elif cn == '9.4':
                    k_danchuang = 5.76
                elif cn == '9.9':
                    k_danchuang = 5.98
                elif cn == '10.5':
                    k_danchuang = 6.19
                elif cn == '11.1':
                    k_danchuang = 6.38
            elif cw == '16.3':
                if cn == '5.8':
                    k_danchuang = 4.28
                elif cn == '6.4':
                    k_danchuang = 4.6
                elif cn == '7.0':
                    k_danchuang = 4.88
                elif cn == '7.6':
                    k_danchuang = 5.16
                elif cn == '8.2':
                    k_danchuang = 5.43
                elif cn == '8.7':
                    k_danchuang = 5.68
                elif cn == '9.4':
                    k_danchuang = 5.92
                elif cn == '9.9':
                    k_danchuang = 6.15
                elif cn == '10.5':
                    k_danchuang = 6.37
                elif cn == '11.1':
                    k_danchuang = 6.58
            elif cw == '17.5':
                if cn == '5.8':
                    k_danchuang = 4.37
                elif cn == '6.4':
                    k_danchuang = 4.68
                elif cn == '7.0':
                    k_danchuang = 4.99
                elif cn == '7.6':
                    k_danchuang = 5.27
                elif cn == '8.2':
                    k_danchuang = 5.55
                elif cn == '8.7':
                    k_danchuang = 5.82
                elif cn == '9.4':
                    k_danchuang = 6.07
                elif cn == '9.9':
                    k_danchuang = 6.32
                elif cn == '10.5':
                    k_danchuang = 6.55
                elif cn == '11.1':
                    k_danchuang = 6.77
            elif cw == '18.6':
                if cn == '5.8':
                    k_danchuang = 4.43
                elif cn == '6.4':
                    k_danchuang = 4.76
                elif cn == '7.0':
                    k_danchuang = 5.07
                elif cn == '7.6':
                    k_danchuang = 5.61
                elif cn == '8.2':
                    k_danchuang = 5.66
                elif cn == '8.7':
                    k_danchuang = 5.94
                elif cn == '9.4':
                    k_danchuang = 6.2
                elif cn == '9.9':
                    k_danchuang = 6.45
                elif cn == '10.5':
                    k_danchuang = 6.7
                elif cn == '11.1':
                    k_danchuang = 6.93
            elif cw == '19.8':
                if cn == '5.8':
                    k_danchuang = 4.49
                elif cn == '6.4':
                    k_danchuang = 4.84
                elif cn == '7.0':
                    k_danchuang = 5.15
                elif cn == '7.6':
                    k_danchuang = 5.47
                elif cn == '8.2':
                    k_danchuang = 5.77
                elif cn == '8.7':
                    k_danchuang = 6.05
                elif cn == '9.4':
                    k_danchuang = 6.33
                elif cn == '9.9':
                    k_danchuang = 6.59
                elif cn == '10.5':
                    k_danchuang = 6.34
                elif cn == '11.1':
                    k_danchuang = 7.08
            elif cw == '20.9':
                if cn == '5.8':
                    k_danchuang = 4.55
                elif cn == '6.4':
                    k_danchuang = 4.9
                elif cn == '7.0':
                    k_danchuang = 5.23
                elif cn == '7.6':
                    k_danchuang = 5.59
                elif cn == '8.2':
                    k_danchuang = 5.86
                elif cn == '8.7':
                    k_danchuang = 6.15
                elif cn == '9.4':
                    k_danchuang = 6.44
                elif cn == '9.9':
                    k_danchuang = 6.71
                elif cn == '10.5':
                    k_danchuang = 6.98
                elif cn == '11.1':
                    k_danchuang = 7.23
            elif cw == '22.1':
                if cn == '5.8':
                    k_danchuang = 4.61
                elif cn == '6.4':
                    k_danchuang = 4.97
                elif cn == '7.0':
                    k_danchuang = 5.3
                elif cn == '7.6':
                    k_danchuang = 5.63
                elif cn == '8.2':
                    k_danchuang = 5.95
                elif cn == '8.7':
                    k_danchuang = 6.26
                elif cn == '9.4':
                    k_danchuang = 6.55
                elif cn == '9.9':
                    k_danchuang = 6.83
                elif cn == '10.5':
                    k_danchuang = 7.11
                elif cn == '11.1':
                    k_danchuang = 7.36
            elif cw == '23.3':
                if cn == '5.8':
                    k_danchuang = 4.65
                elif cn == '6.4':
                    k_danchuang = 5.01
                elif cn == '7.0':
                    k_danchuang = 5.37
                elif cn == '7.6':
                    k_danchuang = 5.71
                elif cn == '8.2':
                    k_danchuang = 6.04
                elif cn == '8.7':
                    k_danchuang = 6.34
                elif cn == '9.4':
                    k_danchuang = 6.64
                elif cn == '9.9':
                    k_danchuang = 6.93
                elif cn == '10.5':
                    k_danchuang = 7.22
                elif cn == '11.1':
                    k_danchuang = 7.49
            elif cw == '24.4':
                if cn == '5.8':
                    k_danchuang = 4.7
                elif cn == '6.4':
                    k_danchuang = 5.07
                elif cn == '7.0':
                    k_danchuang = 5.43
                elif cn == '7.6':
                    k_danchuang = 5.77
                elif cn == '8.2':
                    k_danchuang = 6.11
                elif cn == '8.7':
                    k_danchuang = 6.43
                elif cn == '9.4':
                    k_danchuang = 6.73
                elif cn == '9.9':
                    k_danchuang = 7.04
                elif cn == '10.5':
                    k_danchuang = 7.33
                elif cn == '11.1':
                    k_danchuang = 7.61
            elif cw == '25.6':
                if cn == '5.8':
                    k_danchuang = 4.73
                elif cn == '6.4':
                    k_danchuang = 5.12
                elif cn == '7.0':
                    k_danchuang = 5.48
                elif cn == '7.6':
                    k_danchuang = 5.84
                elif cn == '8.2':
                    k_danchuang = 6.18
                elif cn == '8.7':
                    k_danchuang = 6.5
                elif cn == '9.4':
                    k_danchuang = 6.83
                elif cn == '9.9':
                    k_danchuang = 7.13
                elif cn == '10.5':
                    k_danchuang = 7.43
                elif cn == '11.1':
                    k_danchuang = 7.69
            elif cw == '26.7':
                if cn == '5.8':
                    k_danchuang = 4.78
                elif cn == '6.4':
                    k_danchuang = 5.16
                elif cn == '7.0':
                    k_danchuang = 5.54
                elif cn == '7.6':
                    k_danchuang = 5.9
                elif cn == '8.2':
                    k_danchuang = 6.25
                elif cn == '8.7':
                    k_danchuang = 6.58
                elif cn == '9.4':
                    k_danchuang = 6.91
                elif cn == '9.9':
                    k_danchuang = 7.22
                elif cn == '10.5':
                    k_danchuang = 7.52
                elif cn == '11.1':
                    k_danchuang = 7.82
            elif cw == '27.9':
                if cn == '5.8':
                    k_danchuang = 4.81
                elif cn == '6.4':
                    k_danchuang = 5.2
                elif cn == '7.0':
                    k_danchuang = 5.58
                elif cn == '7.6':
                    k_danchuang = 5.94
                elif cn == '8.2':
                    k_danchuang = 6.3
                elif cn == '8.7':
                    k_danchuang = 6.64
                elif cn == '9.4':
                    k_danchuang = 6.98
                elif cn == '9.9':
                    k_danchuang = 7.3
                elif cn == '10.5':
                    k_danchuang = 7.62
                elif cn == '11.1':
                    k_danchuang = 7.92
            elif cw == '29.1':
                if cn == '5.8':
                    k_danchuang = 4.85
                elif cn == '6.4':
                    k_danchuang = 5.25
                elif cn == '7.0':
                    k_danchuang = 5.63
                elif cn == '7.6':
                    k_danchuang = 6
                elif cn == '8.2':
                    k_danchuang = 6.36
                elif cn == '8.7':
                    k_danchuang = 6.71
                elif cn == '9.4':
                    k_danchuang = 7.05
                elif cn == '9.9':
                    k_danchuang = 7.37
                elif cn == '10.5':
                    k_danchuang = 7.7
                elif cn == '11.1':
                    k_danchuang = 8
        if ds == "双层窗玻璃":
            if cw == "11.6":
                if cn == "5.8":
                    k_danchuang = 2.37
                elif cn == '6.4':
                    k_danchuang = 2.47
                elif cn == '7.0':
                    k_danchuang = 2.55
                elif cn == '7.6':
                    k_danchuang = 2.62
                elif cn == '8.2':
                    k_danchuang = 2.69
                elif cn == '8.7':
                    k_danchuang = 2.74
                elif cn == '9.4':
                    k_danchuang = 2.8
                elif cn == '9.9':
                    k_danchuang = 2.85
                elif cn == '10.5':
                    k_danchuang = 2.9
                else:
                    k_danchuang = 2.73
            elif cw == '12.8':
                if cn == '5.8':
                    k_danchuang = 2.42
                elif cn == '6.4':
                    k_danchuang = 2.51
                elif cn == '7.0':
                    k_danchuang = 2.59
                elif cn == '7.6':
                    k_danchuang = 2.67
                elif cn == '8.2':
                    k_danchuang = 2.74
                elif cn == '8.7':
                    k_danchuang = 2.8
                elif cn == '9.4':
                    k_danchuang = 2.86
                elif cn == '9.9':
                    k_danchuang = 2.92
                elif cn == '10.5':
                    k_danchuang = 2.97
                elif cn == '11.1':
                    k_danchuang = 3.01
            elif cw == '14.0':
                if cn == '5.8':
                    k_danchuang = 2.45
                elif cn == '6.4':
                    k_danchuang = 2.56
                elif cn == '7.0':
                    k_danchuang = 2.64
                elif cn == '7.6':
                    k_danchuang = 2.72
                elif cn == '8.2':
                    k_danchuang = 2.79
                elif cn == '8.7':
                    k_danchuang = 2.86
                elif cn == '9.4':
                    k_danchuang = 2.92
                elif cn == '9.9':
                    k_danchuang = 2.98
                elif cn == '10.5':
                    k_danchuang = 3.02
                elif cn == '11.1':
                    k_danchuang = 3.07
            elif cw == '15.1':
                if cn == '5.8':
                    k_danchuang = 2.49
                elif cn == '6.4':
                    k_danchuang = 2.59
                elif cn == '7.0':
                    k_danchuang = 2.69
                elif cn == '7.6':
                    k_danchuang = 2.77
                elif cn == '8.2':
                    k_danchuang = 2.84
                elif cn == '8.7':
                    k_danchuang = 2.91
                elif cn == '9.4':
                    k_danchuang = 2.97
                elif cn == '9.9':
                    k_danchuang = 3.02
                elif cn == '10.5':
                    k_danchuang = 3.08
                elif cn == '11.1':
                    k_danchuang = 3.13
            elif cw == '16.3':
                if cn == '5.8':
                    k_danchuang = 2.52
                elif cn == '6.4':
                    k_danchuang = 2.63
                elif cn == '7.0':
                    k_danchuang = 2.72
                elif cn == '7.6':
                    k_danchuang = 2.8
                elif cn == '8.2':
                    k_danchuang = 2.87
                elif cn == '8.7':
                    k_danchuang = 2.94
                elif cn == '9.4':
                    k_danchuang = 3.01
                elif cn == '9.9':
                    k_danchuang = 3.07
                elif cn == '10.5':
                    k_danchuang = 3.12
                elif cn == '11.1':
                    k_danchuang = 3.17
            elif cw == '17.5':
                if cn == '5.8':
                    k_danchuang = 2.55
                elif cn == '6.4':
                    k_danchuang = 2.65
                elif cn == '7.0':
                    k_danchuang = 2.74
                elif cn == '7.6':
                    k_danchuang = 2.84
                elif cn == '8.2':
                    k_danchuang = 2.91
                elif cn == '8.7':
                    k_danchuang = 2.98
                elif cn == '9.4':
                    k_danchuang = 3.05
                elif cn == '9.9':
                    k_danchuang = 3.11
                elif cn == '10.5':
                    k_danchuang = 3.16
                elif cn == '11.1':
                    k_danchuang = 3.21
            elif cw == '18.6':
                if cn == '5.8':
                    k_danchuang = 2.57
                elif cn == '6.4':
                    k_danchuang = 2.67
                elif cn == '7.0':
                    k_danchuang = 2.78
                elif cn == '7.6':
                    k_danchuang = 2.86
                elif cn == '8.2':
                    k_danchuang = 2.94
                elif cn == '8.7':
                    k_danchuang = 3.01
                elif cn == '9.4':
                    k_danchuang = 3.08
                elif cn == '9.9':
                    k_danchuang = 3.14
                elif cn == '10.5':
                    k_danchuang = 3.2
                elif cn == '11.1':
                    k_danchuang = 3.25
            elif cw == '19.8':
                if cn == '5.8':
                    k_danchuang = 2.59
                elif cn == '6.4':
                    k_danchuang = 2.7
                elif cn == '7.0':
                    k_danchuang = 2.8
                elif cn == '7.6':
                    k_danchuang = 2.88
                elif cn == '8.2':
                    k_danchuang = 2.97
                elif cn == '8.7':
                    k_danchuang = 3.05
                elif cn == '9.4':
                    k_danchuang = 3.12
                elif cn == '9.9':
                    k_danchuang = 3.17
                elif cn == '10.5':
                    k_danchuang = 3.23
                elif cn == '11.1':
                    k_danchuang = 3.28
            elif cw == '20.9':
                if cn == '5.8':
                    k_danchuang = 2.61
                elif cn == '6.4':
                    k_danchuang = 2.72
                elif cn == '7.0':
                    k_danchuang = 2.83
                elif cn == '7.6':
                    k_danchuang = 2.91
                elif cn == '8.2':
                    k_danchuang = 2.99
                elif cn == '8.7':
                    k_danchuang = 3.07
                elif cn == '9.4':
                    k_danchuang = 3.14
                elif cn == '9.9':
                    k_danchuang = 3.2
                elif cn == '10.5':
                    k_danchuang = 3.26
                elif cn == '11.1':
                    k_danchuang = 3.31
            elif cw == '22.1':
                if cn == '5.8':
                    k_danchuang = 2.63
                elif cn == '6.4':
                    k_danchuang = 2.74
                elif cn == '7.0':
                    k_danchuang = 2.84
                elif cn == '7.6':
                    k_danchuang = 2.93
                elif cn == '8.2':
                    k_danchuang =3.01
                elif cn == '8.7':
                    k_danchuang = 3.09
                elif cn == '9.4':
                    k_danchuang = 3.16
                elif cn == '9.9':
                    k_danchuang = 3.23
                elif cn == '10.5':
                    k_danchuang = 3.29
                elif cn == '11.1':
                    k_danchuang = 3.34
            elif cw == '23.3':
                if cn == '5.8':
                    k_danchuang = 2.64
                elif cn == '6.4':
                    k_danchuang = 2.76
                elif cn == '7.0':
                    k_danchuang = 2.86
                elif cn == '7.6':
                    k_danchuang = 2.95
                elif cn == '8.2':
                    k_danchuang = 3.04
                elif cn == '8.7':
                    k_danchuang = 3.12
                elif cn == '9.4':
                    k_danchuang = 3.19
                elif cn == '9.9':
                    k_danchuang = 3.25
                elif cn == '10.5':
                    k_danchuang = 3.31
                elif cn == '11.1':
                    k_danchuang = 3.37
            elif cw == '24.4':
                if cn == '5.8':
                    k_danchuang = 2.66
                elif cn == '6.4':
                    k_danchuang = 2.77
                elif cn == '7.0':
                    k_danchuang = 2.87
                elif cn == '7.6':
                    k_danchuang = 2.97
                elif cn == '8.2':
                    k_danchuang = 3.06
                elif cn == '8.7':
                    k_danchuang = 3.14
                elif cn == '9.4':
                    k_danchuang = 3.21
                elif cn == '9.9':
                    k_danchuang = 3.27
                elif cn == '10.5':
                    k_danchuang = 3.34
                elif cn == '11.1':
                    k_danchuang = 3.4
            elif cw == '25.6':
                if cn == '5.8':
                    k_danchuang = 2.67
                elif cn == '6.4':
                    k_danchuang = 2.79
                elif cn == '7.0':
                    k_danchuang = 2.9
                elif cn == '7.6':
                    k_danchuang = 2.99
                elif cn == '8.2':
                    k_danchuang = 3.07
                elif cn == '8.7':
                    k_danchuang = 3.15
                elif cn == '9.4':
                    k_danchuang = 3.2
                elif cn == '9.9':
                    k_danchuang = 3.29
                elif cn == '10.5':
                    k_danchuang = 3.36
                elif cn == '11.1':
                    k_danchuang = 3.41
            elif cw == '26.7':
                if cn == '5.8':
                    k_danchuang = 2.69
                elif cn == '6.4':
                    k_danchuang = 2.8
                elif cn == '7.0':
                    k_danchuang = 2.91
                elif cn == '7.6':
                    k_danchuang = 3
                elif cn == '8.2':
                    k_danchuang = 3.09
                elif cn == '8.7':
                    k_danchuang = 3.17
                elif cn == '9.4':
                    k_danchuang = 3.24
                elif cn == '9.9':
                    k_danchuang = 3.31
                elif cn == '10.5':
                    k_danchuang = 3.37
                elif cn == '11.1':
                    k_danchuang = 3.43
            elif cw == '27.9':
                if cn == '5.8':
                    k_danchuang = 2.7
                elif cn == '6.4':
                    k_danchuang = 2.81
                elif cn == '7.0':
                    k_danchuang = 2.92
                elif cn == '7.6':
                    k_danchuang = 3.01
                elif cn == '8.2':
                    k_danchuang = 3.11
                elif cn == '8.7':
                    k_danchuang = 3.19
                elif cn == '9.4':
                    k_danchuang = 3.25
                elif cn == '9.9':
                    k_danchuang = 3.33
                elif cn == '10.5':
                    k_danchuang = 3.4
                elif cn == '11.1':
                    k_danchuang = 3.45
            elif cw == '29.1':
                if cn == '5.8':
                    k_danchuang = 2.71
                elif cn == '6.4':
                    k_danchuang = 2.83
                elif cn == '7.0':
                    k_danchuang = 2.93
                elif cn == '7.6':
                    k_danchuang = 3.04
                elif cn == '8.2':
                    k_danchuang = 3.12
                elif cn == '8.7':
                    k_danchuang = 3.2
                elif cn == '9.4':
                    k_danchuang = 3.28
                elif cn == '9.9':
                    k_danchuang = 3.35
                elif cn == '10.5':
                    k_danchuang = 3.41
                elif cn == '11.1':
                    k_danchuang = 3.47
        print(k_danchuang)

    def boli_button(self):
        global Q_bolichuanre
        f_boli = self.chuangmian.text()
        f_chuangkou = float(f_boli)
        # print(f_chuangkou)
        # print(ttao)
        Q_bolichuanre = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        tl_boli = [27.2, 26.7, 26.2, 25.8, 25.5, 25.3, 25.4, 26, 26.9, 27.9, 29, 29.9, 30.8, 31.5, 31.9, 32.2, 32.2, 32, 31.6, 30.8, 29.9, 29.1, 28.4, 27.8]
        for i in range(len(tl_boli)):
            tl_boli[i] = ttao + tl_boli[i] - float(xiaji_wendu)
            Q_bolichuanre[i] = k_xz * f_chuangkou * k_danchuang * tl_boli[i]
        print(Q_bolichuanre)
        self.close()
    def wuliao(self):
        self.queding_ds.setEnabled(True)
    def wuliao_1(self):
        self.queding_ck.setEnabled(True)
    def wuliao_2(self):
        self.queding_cw.setEnabled(True)
    def wuliao_3(self):
        self.queding_cn.setEnabled(True)
    def wuliao_4(self):
        self.queding_chuangk.setEnabled(True)

class MyMainWindow8(QMainWindow, Ui_Form88):#透过玻璃的日射冷负荷Q_rs
    def __init__(self, parent=None):
        super(MyMainWindow8, self).__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground, True)  #####有背景图片一定加这句话！！！！！
        self.setupUi(self)
        self.pushButton.clicked.connect(self.chaoxiang_button)
        self.chaung_gui.clicked.connect(self.chuanggui_button)
        self.chuang_bo.clicked.connect(self.chuangbo_button)
        self.chuang_zhe.clicked.connect(self.chuangzhe_button)
        self.wancheng.clicked.connect(self.wancheng_button)
        self.bei.textChanged.connect(self.wuliaoaaa)
        self.dong.textChanged.connect(self.wuliaoaaa)
        self.xi.textChanged.connect(self.wuliaoaaa)
        self.nan.textChanged.connect(self.wuliaoaaa)
        self.shuiping.textChanged.connect(self.wuliaoaaa)
        self.comboBox.currentTextChanged.connect(self.wuliaoaaa_1)
        self.comboBox_2.currentTextChanged.connect(self.wuliaoaaa_2)
        self.comboBox_3.currentTextChanged.connect(self.wuliaoaaa_3)

    def wuliaoaaa(self):
        cx_bei6 = self.bei.text()
        cx_xi6 = self.xi.text()
        cx_nan6 = self.nan.text()
        cx_dong6 = self.dong.text()
        cx_shuiping6 = self.shuiping.text()
        if len(cx_bei6)>0 and len(cx_xi6)>0 and len(cx_nan6)>0 and len(cx_dong6)>0 and len(cx_shuiping6)>0:
            self.pushButton.setEnabled(True)
        else:
            self.pushButton.setEnabled(False)
    def wuliaoaaa_1(self):
        self.chaung_gui.setEnabled(True)
    def wuliaoaaa_2(self):
        self.chuang_bo.setEnabled(True)
    def wuliaoaaa_3(self):
        self.chuang_zhe.setEnabled(True)

    def chaoxiang_button(self):
        global cx_nan
        global cx_bei
        global cx_dong
        global cx_xi
        global cx_shuiping
        global cx_nan6
        global cx_bei6
        global cx_dong6
        global cx_xi6
        global cx_shuiping6
        cx_bei6 = self.bei.text()
        cx_bei = float(cx_bei6)
        cx_xi6 = self.xi.text()
        cx_xi = float(cx_xi6)
        cx_nan6 = self.nan.text()
        cx_nan = float(cx_nan6)
        cx_dong6 = self.dong.text()
        cx_dong = float(cx_dong6)
        cx_shuiping6 = self.shuiping.text()
        cx_shuiping = float(cx_shuiping6)

        print(cx_bei)
        print(cx_xi)
        print(cx_dong)
        print(cx_nan)
        print(cx_shuiping)

    def chuanggui_button(self):
        global ca#窗有效面积系数值ca
        chuanggui = self.comboBox.currentText()
        if chuanggui == "单层钢窗":
            ca = 0.85
        elif chuanggui == "单层木窗":
            ca = 0.7
        elif chuanggui == "双层钢窗":
            ca = 0.75
        elif chuanggui == "双层木窗":
            ca = 0.5
        print(ca)

    def chuangbo_button(self):#大注意：：：：坑惨了！！！！原名字叫CS和城市一个名！！！！！！改成了cs1
        global cs1#窗玻璃的遮挡系数cs1
        chuangbo = self.comboBox_2.currentText()
        if chuangbo == "标准玻璃":
            cs1 = 1.0
        elif chuangbo == "5mm厚普通玻璃":
            cs1 = 0.93
        elif chuangbo == "6mm厚普通玻璃":
            cs1 = 0.89
        elif chuangbo == "3mm厚吸热玻璃":
            cs1 = 0.96
        elif chuangbo == "5mm厚吸热玻璃":
            cs1 = 0.88
        elif chuangbo == "6mm厚吸热玻璃":
            cs1 = 0.83
        elif chuangbo == "双层3mm厚普通玻璃":
            cs1 = 0.86
        elif chuangbo == "双层5mm厚普通玻璃":
            cs1 = 0.78
        elif chuangbo == "双层6mm厚普通玻璃":
            cs1 = 0.74
        print(cs1)

    def chuangzhe_button(self):
        global cn#窗内遮阳设施的遮阳系数cn
        global chuangzhe1
        chuangzhe1 = self.comboBox_3.currentText()
        if chuangzhe1 == "白布帘（浅色）":
            cn = 0.5
        elif chuangzhe1 == "浅蓝色布帘（中间色）":
            cn = 0.6
        elif chuangzhe1 == "深黄、紫红、深绿色布帘（深色）":
            cn = 0.65
        elif chuangzhe1 == "活动百叶帘（中间色）":
            cn = 0.6
        elif chuangzhe1 == "无遮阳设备":
            cn = 1.0
        print(cn)
        self.wancheng.setEnabled(True)

    def wancheng_button(self):
        global Q_rs
        beiwu_S = [0.16,0.15,0.14,0.13,0.12,0.11,0.13,0.17,0.21,0.28,0.39,0.49,0.54,0.65,0.6,0.42,0.36,0.32,0.27,0.23,0.21,0.2,0.18,0.17]
        beiwu_N = [0.26,0.24,0.23,0.21,0.19,0.18,0.44,0.42,0.43,0.49,0.56,0.61,0.64,0.66,0.66,0.63,0.59,0.64,0.64,0.38,0.35,0.32,0.3,0.28]
        beiwu_E = [0.12,0.11,0.1,0.09,0.09,0.08,0.29,0.41,0.49,0.6,0.56,0.37,0.29,0.29,0.28,0.26,0.24,0.22,0.19,0.17,0.16,0.15,0.14,0.13]
        beiwu_W = [0.17,0.16,0.15,0.14,0.13,0.12,0.12,0.14,0.15,0.16,0.17,0.17,0.18,0.25,0.37,0.47,0.52,0.62,0.55,0.24,0.23,0.21,0.2,0.18]
        beiwu_SP = [0.2,0.18,0.17,0.16,0.15,0.14,0.16,0.22,0.31,0.39,0.47,0.47,0.57,0.69,0.68,0.55,0.49,0.41,0.33,0.28,0.26,0.25,0.23,0.21]
        beiyou_S = [0.07,0.07,0.06,0.06,0.06,0.05,0.11,0.18,0.26,0.4,0.58,0.72,0.84,0.8,0.62,0.45,0.32,0.24,0.16,0.1,0.09,0.09,0.08,0.08]
        beiyou_N = [0.12,0.11,0.11,0.1,0.09,0.09,0.59,0.54,0.54,0.65,0.75,0.81,0.83,0.83,0.79,0.71,0.6,0.61,0.68,0.17,0.16,0.15,0.14,0.13]
        beiyou_E = [0.06,0.05,0.05,0.05,0.04,0.04,0.47,0.68,0.82,0.79,0.59,0.38,0.24,0.24,0.23,0.21,0.18,0.15,0.11,0.08,0.07,0.07,0.06,0.06]
        beiyou_W = [0.08,0.07,0.07,0.06,0.06,0.06,0.08,0.11,0.14,0.17,0.18,0.19,0.2,0.34,0.56,0.72,0.83,0.77,0.53,0.11,0.1,0.09,0.09,0.08]
        beiyou_SP = [0.09,0.09,0.08,0.08,0.07,0.07,0.13,0.26,0.42,0.57,0.69,0.77,0.85,0.84,0.73,0.84,0.49,0.33,0.19,0.13,0.12,0.11,0.1,0.09]
        nanwu_S = [0.21,0.19,0.18,0.17,0.16,0.14,0.17,0.25,0.33,0.42,0.48,0.54,0.59,0.7,0.7,0.57,0.52,0.44,0.35,0.3,0.28,0.26,0.26,0.22]
        nanwu_N = [0.28,0.25,0.24,0.22,0.21,0.19,0.38,0.49,0.52,0.55,0.59,0.63,0.66,0.68,0.68,0.68,0.69,0.69,0.6,0.4,0.37,0.35,0.32,0.3]
        nanwu_E = [0.12,0.11,0.1,0.09,0.09,0.08,0.24,0.39,0.48,0.61,0.57,0.38,0.31,0.3,0.29,0.28,0.27,0.23,0.21,0.18,0.17,0.15,0.14,0.13]
        nanwu_W = [0.17,0.16,0.15,0.14,0.13,0.12,0.12,0.14,0.16,0.17,0.18,0.19,0.2,0.28,0.4,0.5,0.54,0.61,0.5,0.24,0.23,0.21,0.2,0.18]
        nanwu_SP = [0.19,0.17,0.16,0.15,0.14,0.13,0.14,0.19,0.28,0.37,0.45,0.52,0.56,0.68,0.67,0.53,0.46,0.38,0.3,0.27,0.25,0.23,0.22,0.2]
        nanyou_S = [0.1,0.09,0.09,0.08,0.08,0.07,0.14,0.31,0.47,0.6,0.69,0.77,0.87,0.84,0.74,0.66,0.54,0.38,0.2,0.13,0.12,0.12,0.11,0.1]
        nanyou_N = [0.13,0.12,0.12,0.1,0.1,0.1,0.47,0.67,0.7,0.72,0.77,0.83,0.85,0.84,0.81,0.78,0.77,0.75,0.56,0.18,0.17,0.16,0.15,0.14]
        nanyou_E = [0.06,0.05,0.05,0.05,0.04,0.04,0.36,0.63,0.81,0.81,0.63,0.41,0.27,0.27,0.25,0.23,0.2,0.15,0.1,0.08,0.07,0.07,0.07,0.06]
        nanyou_W = [0.08,0.07,0.07,0.06,0.06,0.06,0.07,0.12,0.16,0.19,0.21,0.22,0.23,0.37,0.6,0.75,0.84,0.73,0.42,0.1,0.1,0.09,0.09,0.08]
        nanyou_SP = [0.09,0.08,0.08,0.07,0.07,0.06,0.09,0.21,0.38,0.54,0.67,0.76,0.85,0.83,0.72,0.61,0.45,0.28,0.16,0.12,0.11,0.1,0.1,0.09]
        Q_rss1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        Q_rsn1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        Q_rse1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        Q_rsw1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        Q_rssp1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        Q_rs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


        list_bei = ['南京','上海','杭州','合肥','南昌','武汉','成都','重庆','济南','郑州','西安','兰州','西宁','石家庄','呼和浩特','沈阳','北京','天津','太原','银川','大连','长春','哈尔滨','乌鲁木齐','拉萨']
        list_nan = ['福州','广州','台北','南宁','贵阳','昆明',"海口"]


        if (cs in list_bei) and (chuangzhe1 == "无遮阳设备"):
            for i in range(len(Q_rss1)):
                Q_rss1[i] = float(cx_nan6) * ca * cs1 * cn * beiwu_S[i]#大注意：：：：坑惨了！！！！一定注意：引用单行文本编辑框数据的时候，一定转换成int。
            for i in range(len(Q_rsn1)):
                Q_rsn1[i] = float(cx_bei6)*ca*cs1*cn*beiwu_N[i]
            for i in range(len(Q_rsw1)):
                Q_rsw1[i] = float(cx_xi6)*ca*cs1*cn*beiwu_W[i]
            for i in range(len(Q_rse1)):
                Q_rse1[i] = float(cx_dong6)*ca*cs1*cn*beiwu_E[i]
            for i in range(len(Q_rssp1)):
                Q_rssp1[i] = float(cx_shuiping6)*ca*cs1*cn*beiwu_SP[i]
            # for i in range(len(Q_rs1)):
            #     Q_rs1[i] = Q_rss1[i] + Q_rss1[i] + Q_rsw1[i] + Q_rse1[i] +Q_rssp1[i]
            # print(Q_rs1)
        #
        elif (cs in list_bei) and (chuangzhe1 =="浅蓝色布帘（中间色）" or chuangzhe1 =="深黄、紫红、深绿色布帘（深色）" or chuangzhe1 == "活动百叶帘（中间色）" or chuangzhe1 == "白布帘（浅色）"):
            for i in range(len(Q_rss1)):
                Q_rss1[i] = float(cx_nan6) * ca * cs1 * cn * beiyou_S[i]  # 大注意：：：：坑惨了！！！！一定注意：引用单行文本编辑框数据的时候，一定转换成int。
            for i in range(len(Q_rsn1)):
                Q_rsn1[i] = float(cx_bei6) * ca * cs1 * cn * beiyou_N[i]
            for i in range(len(Q_rsw1)):
                Q_rsw1[i] = float(cx_xi6) * ca * cs1 * cn * beiyou_W[i]
            for i in range(len(Q_rse1)):
                Q_rse1[i] = float(cx_dong6) * ca * cs1 * cn * beiyou_E[i]
            for i in range(len(Q_rssp1)):
                Q_rssp1[i] = float(cx_shuiping6) * ca * cs1 * cn * beiyou_SP[i]
            # for i in range(len(Q_rs1)):
            #     Q_rs1[i] = Q_rss1[i] + Q_rss1[i] + Q_rsw1[i] + Q_rse1[i] + Q_rssp1[i]
            # print(Q_rs1)
        #
        elif (cs in list_nan) and (chuangzhe1 == "无遮阳设备"):
            for i in range(len(Q_rss1)):
                Q_rss1[i] = float(cx_nan6) * ca * cs1 * cn * nanwu_S[i]  # 大注意：：：：坑惨了！！！！一定注意：引用单行文本编辑框数据的时候，一定转换成int。
            for i in range(len(Q_rsn1)):
                Q_rsn1[i] = float(cx_bei6) * ca * cs1 * cn * nanwu_N[i]
            for i in range(len(Q_rsw1)):
                Q_rsw1[i] = float(cx_xi6) * ca * cs1 * cn * nanwu_W[i]
            for i in range(len(Q_rse1)):
                Q_rse1[i] = float(cx_dong6) * ca * cs1 * cn * nanwu_E[i]
            for i in range(len(Q_rssp1)):
                Q_rssp1[i] = float(cx_shuiping6) * ca * cs1 * cn * nanwu_SP[i]
            # for i in range(len(Q_rs1)):
            #     Q_rs1[i] = Q_rss1[i] + Q_rss1[i] + Q_rsw1[i] + Q_rse1[i] + Q_rssp1[i]
            # print(Q_rs1)
        #
        elif (cs in list_nan) and (chuangzhe1 =="浅蓝色布帘（中间色）" or chuangzhe1 =="深黄、紫红、\
        深绿色布帘（深色）" or chuangzhe1 == "活动百叶帘（中间色）" or chuangzhe1 == "白布帘（浅色）"):
            for i in range(len(Q_rss1)):
                Q_rss1[i] = float(cx_nan6) * ca * cs1 * cn * nanyou_S[i]  # 大注意：：：：坑惨了！！！！一定注意：引用单行文本编辑框数据的时候，一定转换成int。
            for i in range(len(Q_rsn1)):
                Q_rsn1[i] = float(cx_bei6) * ca * cs1 * cn * nanyou_N[i]
            for i in range(len(Q_rsw1)):
                Q_rsw1[i] = float(cx_xi6) * ca * cs1 * cn * nanyou_W[i]
            for i in range(len(Q_rse1)):
                Q_rse1[i] = float(cx_dong6) * ca * cs1 * cn * nanyou_E[i]
            for i in range(len(Q_rssp1)):
                Q_rssp1[i] = float(cx_shuiping6) * ca * cs1 * cn * nanyou_SP[i]
            # for i in range(len(Q_rs1)):
            #     Q_rs1[i] = Q_rss1[i] + Q_rss1[i] + Q_rsw1[i] + Q_rse1[i] + Q_rssp1[i]
            # print(Q_rs1)

        print(Q_rssp1)
        print(Q_rse1)
        print(Q_rsw1)
        print(Q_rsn1)
        print(Q_rss1)

        list_20=["海口"]
        list_25=['福州','广州','台北','南宁','贵阳','昆明']
        list_30=['南京','上海','杭州','合肥','南昌','武汉','成都','重庆']
        list_35=['济南','郑州','西安','兰州','西宁']
        list_40=['石家庄','呼和浩特','沈阳','北京','天津','太原','银川','大连']
        list_45=['长春','哈尔滨','乌鲁木齐']
        list_lasa=['拉萨']

        if cs in list_20:
            self.s_20 = 130.0
            self.e_20 = 540.0
            self.n_20 = 130.0
            self.w_20 = 540.0
            self.sp_20 = 874.0
            for i in range(len(Q_rs)):
                Q_rs[i] = Q_rss1[i]*self.s_20 + Q_rsn1[i]*self.n_20 + Q_rsw1[i]*self.w_20 + Q_rse1[i]*self.e_20 + Q_rssp1[i]*self.sp_20
            print(Q_rs)
        elif cs in list_25:
            self.s_25 = 145.0
            self.e_25 = 509.0
            self.n_25 = 134.0
            self.w_25 = 509.0
            self.sp_25 = 833.0
            for i in range(len(Q_rs)):
                Q_rs[i] = Q_rss1[i]*self.s_25 + Q_rsn1[i]*self.n_25 + Q_rsw1[i]*self.w_25 + Q_rse1[i]*self.e_25 + Q_rssp1[i]*self.sp_25
            print(Q_rs)
        elif cs in list_30:
            self.s_30 = 173.0
            self.e_30 = 538.0
            self.n_30 = 115.0
            self.w_30 = 538.0
            self.sp_30 = 831.0
            for i in range(len(Q_rs)):
                Q_rs[i] = Q_rss1[i]*self.s_30 + Q_rsn1[i]*self.n_30 + Q_rsw1[i]*self.w_30 + Q_rse1[i]*self.e_30 + Q_rssp1[i]*self.sp_30
            print(Q_rs)
        elif cs in list_35:
            self.s_35 = 251.0
            self.e_35 = 574.0
            self.n_35 = 122.0
            self.w_35 = 574.0
            self.sp_35 = 843.0
            for i in range(len(Q_rs)):
                Q_rs[i] = Q_rss1[i]*self.s_35 + Q_rsn1[i]*self.n_35 + Q_rsw1[i]*self.w_35 + Q_rse1[i]*self.e_35 + Q_rssp1[i]*self.sp_35
            print(Q_rs)
        elif cs in list_40:
            self.s_40 = 302.0
            self.e_40 = 598.0
            self.n_40 = 114.0
            self.w_40 = 598.0
            self.sp_40 = 841.0
            for i in range(len(Q_rs)):
                Q_rs[i] = Q_rss1[i]*self.s_40 + Q_rsn1[i]*self.n_40 + Q_rsw1[i]*self.w_40 + Q_rse1[i]*self.e_40 + Q_rssp1[i]*self.sp_40
            print(Q_rs)
        elif cs in list_45:
            self.s_45 = 367.0
            self.e_45 = 597.0
            self.n_45 = 109.0
            self.w_45 = 597.0
            self.sp_45 = 810.0
            for i in range(len(Q_rs)):
                Q_rs[i] = Q_rss1[i]*self.s_45 + Q_rsn1[i]*self.n_45 + Q_rsw1[i]*self.w_45 + Q_rse1[i]*self.e_45 + Q_rssp1[i]*self.sp_45
            print(Q_rs)
        elif cs in list_lasa:
            self.s_lasa = 174.0
            self.e_lasa = 726.0
            self.n_lasa = 132.0
            self.w_lasa = 726.0
            self.sp_lasa = 989.0
            for i in range(len(Q_rs)):
                Q_rs[i] = Q_rss1[i]*self.s_lasa + Q_rsn1[i]*self.n_lasa + Q_rsw1[i]*self.w_lasa + Q_rse1[i]*self.e_lasa + Q_rssp1[i]*self.sp_lasa
            print(Q_rs)
        self.close()

class MyMainWindow9(QMainWindow, Ui_MainWindow9):
    def __init__(self, parent=None):
        super(MyMainWindow9, self).__init__(parent)
        self.setupUi(self)
        self.xiajishuju.setPlainText(str(cs)+',' +"夏季空调室外计算日平均温度为:"+str(xia_shiwpj) + "℃")
        self.xiajishuju_2.setPlainText(str(cs)+',' +"夏季空调室外平均风速为:"+str(xia_pjfs) + 'm/s')

class MyMainWindow10(QMainWindow, Ui_MainWindow10):
    def __init__(self, parent=None):
        super(MyMainWindow10, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.wud11ing_button)
        self.pushButton.clicked.connect(self.qiangti_button)
        self.pushButton_3.clicked.connect(self.zhenjbn_button)
        global k1
        global k
        global zeinan
        global beita

    def wud11ing_button(self):
        bala = self.comboBox_2.currentText()
        if bala == "保温屋盖，保温材料：加气混凝土":
            self.wuding1_win = MyMainWindow11()
            self.wuding1_win.show()
        elif bala == "保温屋盖，保温材料：水泥膨胀珍珠岩":
            self.wuding2_win = MyMainWindow12()
            self.wuding2_win.show()
        elif bala == "保温屋盖，保温材料：沥青膨胀珍珠岩":
            self.wuding3_win = MyMainWindow13()
            self.wuding3_win.show()
        elif bala == "通风屋盖，保温材料：加气混凝土":
            self.wuding4_win = MyMainWindow14()
            self.wuding4_win.show()
        elif bala == "通风屋盖，保温材料：水泥膨胀珍珠岩":
            self.wuding5_win = MyMainWindow15()
            self.wuding5_win.show()
        elif bala == "通风屋盖，保温材料：沥青膨胀珍珠岩":
            self.wuding6_win = MyMainWindow16()
            self.wuding6_win.show()
        elif bala == "吊顶屋盖(一)，保温材料：脲醛泡沫塑料":
            self.wuding7_win = MyMainWindow17()
            self.wuding7_win.show()
        elif bala == "吊顶屋盖(一)，保温材料：膨胀珍珠岩粉":
            self.wuding8_win = MyMainWindow18()
            self.wuding8_win.show()
        elif bala == "吊顶屋盖(一)，保温材料：沥青玻璃棉毡":
            self.wuding9_win = MyMainWindow19()
            self.wuding9_win.show()
        elif bala == "吊顶屋盖(一)，保温材料：膨胀蛭石":
            self.wuding10_win = MyMainWindow20()
            self.wuding10_win.show()
        elif bala == "吊顶屋盖(一)，保温材料：沥青矿渣棉毡":
            self.wuding11_win = MyMainWindow21()
            self.wuding11_win.show()
        elif bala =="吊顶屋盖(二)，保温材料：脲醛泡沫塑料":
            self.wuding12_win = MyMainWindow22()
            self.wuding12_win.show()
        elif bala ==  "吊顶屋盖(二)，保温材料：膨胀珍珠岩粉":
            self.wuding13_win = MyMainWindow23()
            self.wuding13_win.show()
        elif bala ==  "吊顶屋盖(二)，保温材料：沥青玻璃棉毡":
            self.wuding14_win = MyMainWindow24()
            self.wuding14_win.show()
        elif bala == "吊顶屋盖(二)，保温材料：膨胀蛭石":
            self.wuding15_win = MyMainWindow25()
            self.wuding15_win.show()
        elif bala == "吊顶屋盖(二)，保温材料：沥青矿渣棉毡":
            self.wuding16_win = MyMainWindow26()
            self.wuding16_win.show()
        elif bala =="吊顶屋盖(三)，保温材料：脲醛泡沫塑料":
            self.wuding17_win = MyMainWindow27()
            self.wuding17_win.show()
        elif bala ==  "吊顶屋盖(三)，保温材料：膨胀珍珠岩粉":
            self.wuding18_win = MyMainWindow28()
            self.wuding18_win.show()
        elif bala ==  "吊顶屋盖(三)，保温材料：沥青玻璃棉毡":
            self.wuding19_win = MyMainWindow29()
            self.wuding19_win.show()
        elif bala ==  "吊顶屋盖(三)，保温材料：膨胀蛭石":
            self.wuding20_win = MyMainWindow30()
            self.wuding20_win.show()
        elif bala == "吊顶屋盖(三)，保温材料：沥青矿渣棉毡":
            self.wuding21_win = MyMainWindow31()
            self.wuding21_win.show()

    def qiangti_button(self):
        laba = self.comboBox.currentText()
        if laba =="保温墙体(一)，保温材料：加气混凝土":
            self.qiangti1_win = MyMainWindow32()
            self.qiangti1_win.show()
        elif laba =="保温墙体(一)，保温材料：水泥膨胀珍珠岩":
            self.qiangti2_win = MyMainWindow33()
            self.qiangti2_win.show()
        elif laba =="保温墙体(一)，保温材料：沥青膨胀珍珠岩":
            self.qiangti3_win = MyMainWindow34()
            self.qiangti3_win.show()
        elif laba =="保温墙体(二)，保温材料：沥青矿渣棉毡":
            self.qiangti4_win = MyMainWindow35()
            self.qiangti4_win.show()
        elif laba =="保温墙体(二)，保温材料：塑料袋装膨胀蛭石":
            self.qiangti5_win = MyMainWindow36()
            self.qiangti5_win.show()
        elif laba =="保温墙体(二)，保温材料：塑料袋装膨胀珍珠岩粉":
            self.qiangti6_win = MyMainWindow37()
            self.qiangti6_win.show()
        elif laba =="保温墙体(二)，保温材料：沥青玻璃棉毡":
            self.qiangti7_win = MyMainWindow38()
            self.qiangti7_win.show()
        elif laba =="保温墙体(二)，保温材料：塑料袋装脲醛泡沫塑料":
            self.qiangti8_win = MyMainWindow39()
            self.qiangti8_win.show()
        elif laba =="保温墙体(三)，保温材料：沥青矿渣棉毡":
            self.qiangti9_win = MyMainWindow40()
            self.qiangti9_win.show()
        elif laba =="保温墙体(三)，保温材料：塑料袋装膨胀蛭石":
            self.qiangti10_win = MyMainWindow41()
            self.qiangti10_win.show()
        elif laba =="保温墙体(三)，保温材料：塑料袋装膨胀珍珠岩粉":
            self.qiangti11_win = MyMainWindow42()
            self.qiangti11_win.show()
        elif laba =="保温墙体(三)，保温材料：沥青玻璃棉毡":
            self.qiangti12_win = MyMainWindow43()
            self.qiangti12_win.show()
        elif laba =="保温墙体(三)，保温材料：塑料袋装脲醛泡沫塑料":
            self.qiangti13_win = MyMainWindow44()
            self.qiangti13_win.show()
        elif laba =="砖墙":
            self.qiangti14_win = MyMainWindow45()
            self.qiangti14_win.show()
        elif laba =="陶粒页岩混凝土大板280":
            self.qiangti15_win = MyMainWindow46()
            self.qiangti15_win.show()
        elif laba =="混凝土、加气混凝土复合板240":
            self.qiangti16_win = MyMainWindow47()
            self.qiangti16_win.show()
        elif laba =="填泡沫混凝土的钢筋混凝土墙板180":
            self.qiangti17_win = MyMainWindow48()
            self.qiangti17_win.show()
        elif laba =="填泡沫混凝土的钢筋混凝土墙板220":
            self.qiangti18_win = MyMainWindow49()
            self.qiangti18_win.show()
        elif laba =="膨珠混凝土大版280":
            self.qiangti19_win = MyMainWindow50()
            self.qiangti19_win.show()
        elif laba =="混凝土、加气混凝土复合板280（一）":
            self.qiangti20_win = MyMainWindow51()
            self.qiangti20_win.show()
        elif laba =="混凝土、加气混凝土复合板280（二）":
            self.qiangti21_win = MyMainWindow52()
            self.qiangti21_win.show()
        elif laba =="纯加气混凝土大板":
            self.qiangti22_win = MyMainWindow53()
            self.qiangti22_win.show()
        elif laba =="矿棉轻质复合板182":
            self.qiangti23_win = MyMainWindow54()
            self.qiangti23_win.show()
        elif laba =="矿棉轻质复合板98":
            self.qiangti24_win = MyMainWindow55()
            self.qiangti24_win.show()
        elif laba =="钢筋混凝土剪力墙":
            self.qiangti25_win = MyMainWindow56()
            self.qiangti25_win.show()
    def zhenjbn_button(self):
        global zeinan
        global beita
        print(beita)
        print(zeinan)
        self.close()

class MyMainWindow5555(QMainWindow, Ui_Form5555):#output中的类名！

    def __init__(self, parent=None):
        super(MyMainWindow5555, self).__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        self.comboBox.currentTextChanged.connect(self.shebei_1)
        self.comboBox_2.currentTextChanged.connect(self.shebei_2)
        self.comboBox_3.currentTextChanged.connect(self.shebei_3)
        self.pushButton.clicked.connect(self.shebei_4)
        self.pushButton_3.clicked.connect(self.shebei_5)
        self.pushButton_2.clicked.connect(self.shebei_6)
        self.pushButton_5.clicked.connect(self.shebei_7)
        self.pushButton_4.clicked.connect(self.shebei_8)
        self.pushButton_6.clicked.connect(self.shebei_9)
        self.pushButton_7.clicked.connect(self.shebei_10)
    def shebei_1(self):
        # global Q_diandong
        self.shebeizhonglei = self.comboBox.currentText()
        if self.shebeizhonglei =='无任何电动设备':
            self.Q_diandong = 0
            print(self.Q_diandong)
            QMessageBox.information(self, '请注意：', u'可跳过‘电动设备’栏的填写！')
        else:
            self.pushButton.setEnabled(True)
    def shebei_4(self):
        self.Clll, clll = QInputDialog.getDouble(self, u'电动设备的安装功率（KW）', u'请在此输入电动设备的安装功率（KW）：', 6.0, 0,10000)
        print(self.Clll)
        self.pushButton_3.setEnabled(True)
        if self.Clll<=1.1:
            self.xiaolv = 0.76
        elif 1.1<self.Clll<=1.5:
            self.xiaolv = 0.78
        elif 1.5<self.Clll<=2.2:
            self.xiaolv = 0.8
        elif 2.2<self.Clll<=3:
            self.xiaolv = 0.82
        elif 3<self.Clll<=4:
            self.xiaolv = 0.83
        elif 4<self.Clll<=5.5:
            self.xiaolv = 0.84
        elif 5.5<self.Clll<=7.5:
            self.xiaolv = 0.85
        elif 7.5<self.Clll<=10:
            self.xiaolv = 0.86
        elif 10<self.Clll<=13:
            self.xiaolv = 0.87
        elif 13<self.Clll<=17:
            self.xiaolv = 0.875
        elif 17<self.Clll:
            self.xiaolv = 0.88
        print(self.xiaolv)
    def shebei_5(self):
        # global Q_diandong
        self.n1 = 0.8 #利用系数
        self.n2 = 0.7#同时使用系数
        self.n3 = 0.5 #负荷系数
        self.Clll_1, clll_1 = QInputDialog.getDouble(self, u'电动设备的个数', u'请在此输入电动设备的个数', 10, 0, 10000)
        print(self.Clll_1)
        if self.shebeizhonglei == '无任何电动设备':
            self.Q_diandong = 0
        elif self.shebeizhonglei=='工艺设备及其电动设备均在室内':
            self.Q_diandong = (1000 * self.n1 * self.n2*  self.n3 *self.Clll * self.Clll_1)/self.xiaolv
        elif self.shebeizhonglei=="工艺设备在室内，电动机不在室内":
            self.Q_diandong = (1000 * self.n1 * self.n2 * self.n3 * self.Clll * self.Clll_1)
        elif self.shebeizhonglei=="工艺设备不在室内，电动机在室内":
            self.Q_diandong = (1000 * self.n1 * self.n2 * self.n3 * self.Clll * self.Clll_1*(1-self.xiaolv))/self.xiaolv
        print(self.Q_diandong)

        ###以下是屋顶结构

    def shebei_2(self):
        # global Q_dianre
        self.shebeidianre = self.comboBox_2.currentText()
        if self.shebeidianre =='无任何电热设备':
            self.Q_dianre = 0
            print(self.Q_dianre)
            QMessageBox.information(self, '请注意：', u'可跳过‘电热设备’栏的填写！')
        else:
            self.pushButton_2.setEnabled(True)
    def shebei_6(self):
        self.Clll_2, clll_2 = QInputDialog.getDouble(self, u'电热设备的安装功率（KW）', u'请在此输入电热设备的安装功率（KW）：', 6.0, 0, 10000)
        print(self.Clll_2)
        self.pushButton_5.setEnabled(True)
    def shebei_7(self):
        self.n4 = 0.5#排风带走热量的系数
        self.n1 = 0.8 #利用系数
        self.n2 = 0.7#同时使用系数
        self.n3 = 0.5 #负荷系数
        self.Clll_3, clll_3 = QInputDialog.getDouble(self, u'电热设备的个数', u'请在此输入电热设备的个数', 10, 0, 10000)
        print(self.Clll_3)
        if self.shebeidianre =='无任何电热设备':
            self.Q_dianre = 0
            print(self.Q_dianre)
        elif self.shebeidianre =="有保温密闭罩的电热设备":
            self.Q_dianre = 1000*self.n1*self.n2*self.n3*self.n4* self.Clll_3 * self.Clll_2
            print(self.Q_dianre)

    def shebei_3(self):
        # global Q_dianzi
        self.shebeidianzi = self.comboBox_3.currentText()
        if self.shebeidianzi =='无任何电子设备':
            self.Q_dianzi = 0
            print(self.Q_dianzi)
            QMessageBox.information(self, '请注意：', u'可跳过‘电子设备’栏的填写！')
            self.pushButton_7.setEnabled(True)
        else:
            self.pushButton_4.setEnabled(True)
    def shebei_8(self):
        self.Clll_4, clll_4 = QInputDialog.getDouble(self, u'电子设备的功率（KW）', u'请在此输入电子设备的功率（KW）：', 1, 0, 10000)
        self.pushButton_6.setEnabled(True)
        print(self.Clll_4)
    def shebei_9(self):
        self.n1 = 0.8 #利用系数
        self.n2 = 0.7#同时使用系数
        self.n3 = 0.5 #负荷系数
        self.Clll_5, clll_5 = QInputDialog.getDouble(self, u'电子设备的个数', u'请在此输入电子设备的个数', 1, 0, 10000)
        print(self.Clll_5)
        if self.shebeidianzi == '无任何电子设备':
            self.Q_dianzi = 0
            print(self.Q_dianzi)
        elif self.shebeidianzi == "电子计算机":
            self.Q_dianzi = 1000 *self.n1*self.n2*1*self.Clll_4*self.Clll_5
            print(self.Q_dianzi)
        elif self.shebeidianzi == "一般仪表":
            self.Q_dianzi = 1000 * self.n1 * self.n2 * 0.78 * self.Clll_4 * self.Clll_5
            print(self.Q_dianzi)
        elif self.shebeidianzi == '其他电子设备':
            self.Q_dianzi = 1000 * self.n1 * self.n2 * 0.78 * self.Clll_4 * self.Clll_5
            print(self.Q_dianzi)
        self.pushButton_7.setEnabled(True)
    def shebei_10(self):
        global Q_shebei
        # global Q_dianre
        # global Q_diandong
        # global Q_dianzi
        Q_shebei = self.Q_dianre + self.Q_dianzi + self.Q_diandong
        print(Q_shebei)
        self.close()

class MyMainWindow2777(QMainWindow, Ui_MainWindow277):
    def __init__(self, parent=None):
        super(MyMainWindow2777, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.hushuo)
        self.pushButton_3.clicked.connect(self.cf)
        self.pushButton_2.clicked.connect(self.cf1)
        global cx_nan
        global cx_bei
        global cx_dong
        global cx_xi
        global cx_shuiping
        global Q_dongtian
        global dongji_wendu1
        global dong_shiwpj
        global k
        global k1
        global m_dongqiang
        global m_xiqiang
        global m_nanqiang
        global m_beiqiang
        global m_wuding
        global k_danchuang
        print(dongji_wendu1)
        self.Q_refuheqiangwu = (m_dongqiang*0.95*k1+m_xiqiang*0.95*k1+m_nanqiang*k1*0.8+m_beiqiang*k1+k*m_wuding)*(dongji_wendu1-dong_shiwpj)
        self.Q_refuhechuang = (k_danchuang*cx_nan*0.8+k_danchuang*cx_bei+k_danchuang*cx_dong*0.95+k_danchuang*cx_xi*0.95+k_danchuang*cx_shuiping*0.7)*(dongji_wendu1-dong_shiwpj)
        Q_dongtian = self.Q_refuhechuang+self.Q_refuheqiangwu

    def hushuo(self):

        self.jieguo1.setPlainText("冬季热负荷为：："+str(Q_dongtian))
    def cf(self):
        self.Q_dongtianhuitu = [Q_dongtian]*24

        plt1 = pg.plot(title='冬季热负荷图表')
        plt1.addLegend()

        c1 = plt1.plot([0, 1,2, 3, 4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],self.Q_dongtianhuitu, pen='r', name='冬季热负荷负荷/W')
    def cf1(self):
        self.jieguo1.clear()








class MyMainWindow11(QMainWindow, Ui_MainWindow11,Ui_MainWindow3):
    def __init__(self, parent=None):
        super(MyMainWindow11, self).__init__(parent)
        self.setupUi(self)
        self.fffw_1.clicked.connect(self.fffw1_button)
        # global beita
    def fffw1_button(self):
        global k
        global huali
        global beita

        ffw_1 = self.comboBox.currentText()
        if ffw_1=="200":
            k = 0.79
            huali = 0.31
        elif ffw_1 == "170":
            k = 0.90
            huali = 0.37
        elif ffw_1 == "140":
            k = 1.02
            huali = 0.42
        elif ffw_1 == "110":
            k = 1.20
            huali = 0.47
        elif ffw_1== "90":
            k = 1.36
            huali = 0.50
        beita = w_xsxs * huali
        print(beita)
        print(k,huali)
        self.close()
class MyMainWindow12(QMainWindow, Ui_MainWindow12,Ui_MainWindow3):
    def __init__(self, parent=None):
        super(MyMainWindow12, self).__init__(parent)
        self.setupUi(self)
        self.fffw_2.clicked.connect(self.fffw2_button)

    def fffw2_button(self):
        global k
        global huali
        global beita
        ffw_2 = self.comboBox.currentText()
        if ffw_2=="200":
            k = 0.49
            huali = 0.33
        elif ffw_2 == "150":
            k = 0.63
            huali = 0.42
        elif ffw_2 == "120":
            k = 0.74
            huali = 0.46
        elif ffw_2 == "90":
            k = 0.93
            huali = 0.50
        elif ffw_2 == "70":
            k = 1.10
            huali = 0.52
        elif ffw_2 == "60":
            k = 1.22
            huali = 0.54
        elif ffw_2 == "50":
            k = 1.36
            huali = 0.55
        beita = w_xsxs * huali
        print(beita)
        print(k,huali)
        self.close()
class MyMainWindow13(QMainWindow, Ui_MainWindow13,Ui_MainWindow3):
    def __init__(self, parent=None):
        super(MyMainWindow13, self).__init__(parent)
        self.setupUi(self)
        self.fffw_3.clicked.connect(self.fffw3_button)

    def fffw3_button(self):
        global k
        global huali
        global beita
        ffw_3 = self.comboBox.currentText()
        if ffw_3=="160":
            k = 0.49
            huali = 0.37
        elif ffw_3 == "120":
            k = 0.63
            huali = 0.44
        elif ffw_3 == "90":
            k = 0.79
            huali = 0.48
        elif ffw_3 == "70":
            k = 0.94
            huali = 0.51
        elif ffw_3 == "60":
            k = 1.05
            huali = 0.52
        elif ffw_3== "50":
            k = 1.19
            huali = 0.54
        elif ffw_3 == "40":
            k = 1.24
            huali = 0.56
        beita = w_xsxs * huali
        print(beita)
        print(k,huali)
        self.close()
class MyMainWindow14(QMainWindow, Ui_MainWindow14,Ui_MainWindow3):
    def __init__(self, parent=None):
        super(MyMainWindow14, self).__init__(parent)
        self.setupUi(self)
        self.fffw_4.clicked.connect(self.fffw4_button)

    def fffw4_button(self):
        global k
        global huali
        global beita
        ffw_4 = self.comboBox.currentText()
        if ffw_4=="200":
            k = 0.63
            huali = 0.20
        elif ffw_4== "170":
            k = 0.70
            huali = 0.24
        elif ffw_4== "140":
            k = 0.77
            huali = 0.28
        elif ffw_4 == "110":
            k = 0.86
            huali = 0.33
        elif ffw_4 == "90":
            k = 0.94
            huali = 0.37
        beita = w_xsxs * huali
        print(beita)
        print(k,huali)
        self.close()
class MyMainWindow15(QMainWindow, Ui_MainWindow15,Ui_MainWindow3):
    def __init__(self, parent=None):
        super(MyMainWindow15, self).__init__(parent)
        self.setupUi(self)
        self.fffw_5.clicked.connect(self.fffw5_button)

    def fffw5_button(self):
        global k
        global huali
        global beita
        ffw_5 = self.comboBox.currentText()
        if ffw_5=="200":
            k = 0.43
            huali = 0.22
        elif ffw_5 == "150":
            k = 0.52
            huali = 0.28
        elif ffw_5 == "120":
            k = 0.60
            huali = 0.33
        elif ffw_5 == "90":
            k = 0.71
            huali = 0.37
        elif ffw_5 == "70":
            k = 0.81
            huali = 0.40
        elif ffw_5 == "60":
            k = 0.87
            huali = 0.42
        elif ffw_5 == "50":
            k = 0.94
            huali = 0.44
        beita = w_xsxs * huali
        print(beita)
        print(k,huali)
        self.close()
class MyMainWindow16(QMainWindow, Ui_MainWindow16,Ui_MainWindow3):
    def __init__(self, parent=None):
        super(MyMainWindow16, self).__init__(parent)
        self.setupUi(self)
        self.fffw_6.clicked.connect(self.fffw6_button)

    def fffw6_button(self):
        global k
        global huali
        global beita
        ffw_6 = self.comboBox.currentText()
        if ffw_6=="160":
            k = 0.43
            huali = 0.25
        elif ffw_6 == "120":
            k = 0.52
            huali = 0.31
        elif ffw_6 == "90":
            k = 0.63
            huali = 0.35
        elif ffw_6 == "70":
            k = 0.72
            huali = 0.39
        elif ffw_6 == "60":
            k = 0.78
            huali = 0.41
        elif ffw_6 == "50":
            k = 0.86
            huali = 0.42
        elif ffw_6== "40":
            k = 0.94
            huali = 0.44
        beita = w_xsxs * huali
        print(beita)
        print(k,huali)
        self.close()
class MyMainWindow17(QMainWindow, Ui_MainWindow17):
    def __init__(self, parent=None):
        super(MyMainWindow17, self).__init__(parent)
        self.setupUi(self)
        self.fffw_7.clicked.connect(self.fffw7_button)

    def fffw7_button(self):
        global k
        global huali
        global beita
        ffw_7 = self.comboBox.currentText()
        if ffw_7=="80":
            k = 0.44
            huali = 0.50
        elif ffw_7 == "60":
            k = 0.53
            huali = 0.51
        elif ffw_7 == "50":
            k = 0.60
            huali = 0.51
        elif ffw_7 == "40":
            k = 0.70
            huali = 0.52
        elif ffw_7 == "30":
            k = 0.83
            huali = 0.53
        beita = w_xsxs * huali
        print(beita)
        print(k,huali)
        self.close()
class MyMainWindow18(QMainWindow, Ui_MainWindow18):
    def __init__(self, parent=None):
        super(MyMainWindow18, self).__init__(parent)
        self.setupUi(self)
        self.fffw_8.clicked.connect(self.fffw8_button)

    def fffw8_button(self):
        global k
        global huali
        global beita
        ffw_8 = self.comboBox.currentText()
        if ffw_8=="100":
            k = 0.44
            huali = 0.49
        elif ffw_8 == "80":
            k = 0.51
            huali = 0.50
        elif ffw_8 == "60":
            k = 0.63
            huali = 0.51
        elif ffw_8 == "50":
            k = 0.70
            huali = 0.52
        elif ffw_8 == "40":
            k = 0.79
            huali = 0.53
        elif ffw_8 == "30":
            k = 0.92
            huali = 0.54
        elif ffw_8 == "25":
            k = 1.0
            huali = 0.54
        beita = w_xsxs * huali
        print(beita)
        print(k,huali)
        self.close()
class MyMainWindow19(QMainWindow, Ui_MainWindow19):
    def __init__(self, parent=None):
        super(MyMainWindow19, self).__init__(parent)
        self.setupUi(self)
        self.fffw_9.clicked.connect(self.fffw9_button)

    def fffw9_button(self):
        global k
        global huali
        global beita
        ffw_9 = self.comboBox.currentText()
        if ffw_9=="100":
            k = 0.44
            huali = 0.49
        elif ffw_9 == "80":
            k = 0.51
            huali = 0.50
        elif ffw_9 == "60":
            k = 0.63
            huali = 0.51
        elif ffw_9 == "50":
            k = 0.70
            huali = 0.52
        elif ffw_9 == "40":
            k = 0.79
            huali = 0.53
        elif ffw_9 == "30":
            k = 0.92
            huali = 0.54
        elif ffw_9 == "25":
            k = 1.0
            huali = 0.54
        beita = w_xsxs * huali
        print(beita)
        print(k,huali)
        self.close()
class MyMainWindow20(QMainWindow, Ui_MainWindow20):
    def __init__(self, parent=None):
        super(MyMainWindow20, self).__init__(parent)
        self.setupUi(self)
        self.fffw_10.clicked.connect(self.fffw10_button)

    def fffw10_button(self):
        global k
        global huali
        global beita
        ffw_10 = self.comboBox.currentText()
        if ffw_10=="120":
            k = 0.44
            huali = 0.48
        elif ffw_10 == "90":
            k = 0.53
            huali = 0.5
        elif ffw_10== "70":
            k = 0.64
            huali = 0.51
        elif ffw_10 == "60":
            k = 0.70
            huali = 0.52
        elif ffw_10 == "50":
            k = 0.78
            huali = 0.52
        elif ffw_10 == "40":
            k = 0.87
            huali = 0.53
        elif ffw_10 == "30":
            k = 1.0
            huali = 0.54
        beita = w_xsxs * huali
        print(beita)
        print(k,huali)
        self.close()
class MyMainWindow21(QMainWindow, Ui_MainWindow21):
    def __init__(self, parent=None):
        super(MyMainWindow21, self).__init__(parent)
        self.setupUi(self)
        self.fffw_11.clicked.connect(self.fffw11_button)

    def fffw11_button(self):
        global k
        global huali
        global beita
        ffw_11 = self.comboBox.currentText()
        if ffw_11=="120":
            k = 0.44
            huali = 0.48
        elif ffw_11 == "90":
            k = 0.53
            huali = 0.50
        elif ffw_11 == "70":
            k = 0.64
            huali = 0.51
        elif ffw_11 == "60":
            k = 0.70
            huali = 0.52
        elif ffw_11 == "50":
            k = 0.78
            huali = 0.52
        elif ffw_11 == "40":
            k = 0.87
            huali = 0.53
        elif ffw_11 == "30":
            k = 1.0
            huali = 0.54
        beita = w_xsxs * huali
        print(beita)
        print(k,huali)
        self.close()
class MyMainWindow22(QMainWindow, Ui_MainWindow22):
    def __init__(self, parent=None):
        super(MyMainWindow22, self).__init__(parent)
        self.setupUi(self)
        self.fffw_12.clicked.connect(self.fffw12_button)

    def fffw12_button(self):
        global k
        global huali
        global beita
        ffw_12 = self.comboBox.currentText()
        if ffw_12=="80":
            k = 0.44
            huali = 0.48
        elif ffw_12 == "60":
            k = 0.55
            huali = 0.49
        elif ffw_12 == "50":
            k = 0.62
            huali = 0.49
        elif ffw_12 == "40":
            k = 0.71
            huali = 0.50
        elif ffw_12 == "30":
            k = 0.84
            huali = 0.51
        beita = w_xsxs * huali
        print(beita)
        print(k,huali)
        self.close()
class MyMainWindow23(QMainWindow, Ui_MainWindow23):
    def __init__(self, parent=None):
        super(MyMainWindow23, self).__init__(parent)
        self.setupUi(self)
        self.fffw_13.clicked.connect(self.fffw13_button)

    def fffw13_button(self):
        global k
        global huali
        global beita
        ffw_13 = self.comboBox.currentText()
        if ffw_13=="100":
            k = 0.44
            huali = 0.47
        elif ffw_13 == "80":
            k = 0.52
            huali = 0.48
        elif ffw_13 == "60":
            k = 0.64
            huali = 0.49
        elif ffw_13 == "50":
            k = 0.71
            huali = 0.49
        elif ffw_13 == "40":
            k = 0.81
            huali = 0.50
        elif ffw_13 == "30":
            k = 0.94
            huali = 0.51
        elif ffw_13 == "25":
            k = 1.02
            huali = 0.52
        beita = w_xsxs * huali
        print(beita)
        print(k,huali)
        self.close()
class MyMainWindow24(QMainWindow, Ui_MainWindow24):
    def __init__(self, parent=None):
        super(MyMainWindow24, self).__init__(parent)
        self.setupUi(self)
        self.fffw_14.clicked.connect(self.fffw14_button)

    def fffw14_button(self):
        global k
        global huali
        global beita
        ffw_14 = self.comboBox.currentText()
        if ffw_14=="100":
            k = 0.44
            huali = 0.47
        elif ffw_14 == "80":
            k = 0.52
            huali = 0.48
        elif ffw_14 == "60":
            k = 0.64
            huali = 0.49
        elif ffw_14 == "50":
            k = 0.71
            huali = 0.50
        elif ffw_14 == "40":
            k = 0.81
            huali = 0.50
        elif ffw_14 == "30":
            k = 0.94
            huali = 0.51
        elif ffw_14 == "25":
            k = 1.02
            huali = 0.52
        beita = w_xsxs * huali
        print(beita)
        print(k,huali)
        self.close()
class MyMainWindow25(QMainWindow, Ui_MainWindow25):
    def __init__(self, parent=None):
        super(MyMainWindow25, self).__init__(parent)
        self.setupUi(self)
        self.fffw_15.clicked.connect(self.fffw15_button)

    def fffw15_button(self):
        global k
        global huali
        global beita
        ffw_15 = self.comboBox.currentText()
        if ffw_15=="120":
            k = 0.44
            huali = 0.46
        elif ffw_15 == "90":
            k = 0.55
            huali = 0.47
        elif ffw_15 == "70":
            k = 0.65
            huali = 0.49
        elif ffw_15 == "60":
            k = 0.71
            huali = 0.49
        elif ffw_15 == "50":
            k = 0.79
            huali = 0.50
        elif ffw_15 == "40":
            k = 0.90
            huali = 0.51
        elif ffw_15 == "30":
            k = 1.02
            huali = 0.52
        beita = w_xsxs * huali
        print(beita)
        print(k,huali)
        self.close()
class MyMainWindow26(QMainWindow, Ui_MainWindow26):
    def __init__(self, parent=None):
        super(MyMainWindow26, self).__init__(parent)
        self.setupUi(self)
        self.fffw_16.clicked.connect(self.fffw16_button)

    def fffw16_button(self):
        global k
        global huali
        global beita
        ffw_16 = self.comboBox.currentText()
        if ffw_16=="120":
            k = 0.44
            huali = 0.45
        elif ffw_16 == "90":
            k = 0.55
            huali = 0.47
        elif ffw_16 == "70":
            k = 0.65
            huali = 0.48
        elif ffw_16 == "60":
            k = 0.71
            huali = 0.49
        elif ffw_16 == "50":
            k = 0.79
            huali = 0.50
        elif ffw_16 == "40":
            k = 0.90
            huali = 0.51
        elif ffw_16 == "30":
            k = 1.02
            huali = 0.52
        beita = w_xsxs * huali
        print(beita)
        print(k,huali)
        self.close()
class MyMainWindow27(QMainWindow, Ui_MainWindow27):
    def __init__(self, parent=None):
        super(MyMainWindow27, self).__init__(parent)
        self.setupUi(self)
        self.fffw_17.clicked.connect(self.fffw17_button)

    def fffw17_button(self):
        global k
        global huali
        global beita
        ffw_17 = self.comboBox.currentText()
        if ffw_17=="80":
            k = 0.42
            huali = 0.42
        elif ffw_17 == "60":
            k = 0.50
            huali = 0.45
        elif ffw_17 == "40":
            k = 0.64
            huali = 0.46
        elif ffw_17 == "35":
            k = 0.69
            huali = 0.47
        elif ffw_17 == "25":
            k = 0.81
            huali = 0.48
        beita = w_xsxs * huali
        print(beita)
        print(k,huali)
        self.close()
class MyMainWindow28(QMainWindow, Ui_MainWindow28):
    def __init__(self, parent=None):
        super(MyMainWindow28, self).__init__(parent)
        self.setupUi(self)
        self.fffw_18.clicked.connect(self.fffw18_button)

    def fffw18_button(self):
        global k
        global huali
        global beita
        ffw_18 = self.comboBox.currentText()
        if ffw_18=="95":
            k = 0.43
            huali = 0.43
        elif ffw_18 == "70":
            k = 0.52
            huali = 0.44
        elif ffw_18 == "55":
            k = 0.60
            huali = 0.45
        elif ffw_18 == "40":
            k = 0.72
            huali = 0.46
        elif ffw_18 == "30":
            k = 0.83
            huali = 0.47
        elif ffw_18 == "25":
            k = 0.88
            huali = 0.48
        beita = w_xsxs * huali
        print(beita)
        print(k,huali)
        self.close()
class MyMainWindow29(QMainWindow, Ui_MainWindow29):
    def __init__(self, parent=None):
        super(MyMainWindow29, self).__init__(parent)
        self.setupUi(self)
        self.fffw_19.clicked.connect(self.fffw19_button)

    def fffw19_button(self):
        global k
        global huali
        global beita
        ffw_19 = self.comboBox.currentText()
        if ffw_19=="95":
            k = 0.43
            huali = 0.43
        elif ffw_19 == "70":
            k = 0.52
            huali = 0.44
        elif ffw_19 == "55":
            k = 0.60
            huali = 0.45
        elif ffw_19 == "40":
            k = 0.72
            huali = 0.46
        elif ffw_19 == "30":
            k = 0.83
            huali = 0.47
        elif ffw_19 == "25":
            k = 0.88
            huali = 0.48
        beita = w_xsxs * huali
        print(beita)
        print(k,huali)
        self.close()
class MyMainWindow30(QMainWindow, Ui_MainWindow30):
    def __init__(self, parent=None):
        super(MyMainWindow30, self).__init__(parent)
        self.setupUi(self)
        self.fffw_20.clicked.connect(self.fffw20_button)

    def fffw20_button(self):
        global k
        global huali
        global beita
        ffw_20 = self.comboBox.currentText()
        if ffw_20=="115":
            k = 0.43
            huali = 0.42
        elif ffw_20 == "85":
            k = 0.52
            huali = 0.44
        elif ffw_20 == "65":
            k = 0.62
            huali = 0.45
        elif ffw_20 == "50":
            k = 0.71
            huali = 0.46
        elif ffw_20 == "40":
            k = 0.79
            huali = 0.47
        elif ffw_20 == "30":
            k = 0.88
            huali = 0.48
        beita = w_xsxs * huali
        print(beita)
        print(k,huali)
        self.close()
class MyMainWindow31(QMainWindow, Ui_MainWindow31):
    def __init__(self, parent=None):
        super(MyMainWindow31, self).__init__(parent)
        self.setupUi(self)
        self.fffw_21.clicked.connect(self.fffw21_button)

    def fffw21_button(self):
        global k
        global huali
        global beita
        ffw_21 = self.comboBox.currentText()
        if ffw_21=="115":
            k = 0.43
            huali = 0.41
        elif ffw_21 == "85":
            k = 0.52
            huali = 0.43
        elif ffw_21 == "65":
            k = 0.62
            huali = 0.45
        elif ffw_21 == "50":
            k = 0.71
            huali = 0.46
        elif ffw_21 == "40":
            k = 0.79
            huali = 0.47
        elif ffw_21 == "30":
            k = 0.88
            huali = 0.48
        beita = w_xsxs * huali
        print(beita)
        print(k,huali)
        self.close()

###以下是墙体结构
class MyMainWindow32(QMainWindow, Ui_MainWindow32):
    def __init__(self, parent=None):
        super(MyMainWindow32, self).__init__(parent)
        self.setupUi(self)
        self.fffq_1.clicked.connect(self.fffq1_button)

    def fffq1_button(self):
        global k1
        global huali1
        global zeinan
        ffq1 = self.comboBox.currentText()
        if ffq1=="250":
            k1 = 0.59
            huali1 = 0.08
        elif ffq1 == "190":
            k1 = 0.71
            huali1 = 0.12
        elif ffq1 == "150":
            k1 = 0.81
            huali1 = 0.15
        elif ffq1 == "120":
            k1 = 0.93
            huali1 = 0.17
        elif ffq1 == "90":
            k1 = 1.07
            huali1 = 0.20
        elif ffq1 == "70":
            k1 = 1.19
            huali1 = 0.22
        zeinan = q_xsxs * huali1
        print(zeinan)
        print(k1,huali1)
        self.close()
class MyMainWindow33(QMainWindow, Ui_MainWindow33):
    def __init__(self, parent=None):
        super(MyMainWindow33, self).__init__(parent)
        self.setupUi(self)
        self.fffq_2.clicked.connect(self.fffq2_button)

    def fffq2_button(self):
        global k1
        global huali1
        global zeinan
        ffq2 = self.comboBox.currentText()
        if ffq2=="140":
            k1 = 0.58
            huali1 = 0.16
        elif ffq2 == "110":
            k1 = 0.69
            huali1 = 0.17
        elif ffq2 == "80":
            k1 = 0.84
            huali1 = 0.19
        elif ffq2 == "60":
            k1 = 0.98
            huali1 = 0.21
        elif ffq2 == "50":
            k1 = 1.07
            huali1 = 0.22
        elif ffq2 == "40":
            k1 = 1.17
            huali1 = 0.23
        zeinan= q_xsxs * huali1
        print(zeinan)
        print(k1,huali1)
        self.close()
class MyMainWindow34(QMainWindow, Ui_MainWindow34):
    def __init__(self, parent=None):
        super(MyMainWindow34, self).__init__(parent)
        self.setupUi(self)
        self.fffq_3.clicked.connect(self.fffq3_button)

    def fffq3_button(self):
        global k1
        global huali1
        global zeinan
        ffq3 = self.comboBox.currentText()
        if ffq3=="160":
            k1 = 0.45
            huali1 = 0.13
        elif ffq3 == "110":
            k1 = 0.59
            huali1 = 0.16
        elif ffq3 == "80":
            k1 = 0.73
            huali1 = 0.19
        elif ffq3 == "65":
            k1 = 0.83
            huali1 = 0.20
        elif ffq3 == "50":
            k1 = 0.95
            huali1 = 0.21
        elif ffq3 == "40":
            k1 = 1.07
            huali1 = 0.22
        zeinan = q_xsxs * huali1
        print(zeinan)
        print(k1,huali1)
        self.close()
class MyMainWindow35(QMainWindow, Ui_MainWindow35):
    def __init__(self, parent=None):
        super(MyMainWindow35, self).__init__(parent)
        self.setupUi(self)
        self.fffq_4.clicked.connect(self.fffq4_button)

    def fffq4_button(self):
        global k1
        global huali1
        global zeinan
        ffq4 = self.comboBox.currentText()
        if ffq4=="100":
            k1 = 0.48
            huali1 = 0.16
        elif ffq4 == "80":
            k1 = 0.56
            huali1 = 0.17
        elif ffq4 == "70":
            k1 = 0.60
            huali1 = 0.17
        elif ffq4 == "50":
            k1 = 0.73
            huali1 = 0.18
        elif ffq4 == "40":
            k1 = 0.81
            huali1 = 0.19
        elif ffq4 == "30":
            k1 = 0.93
            huali1 = 0.20
        zeinan = q_xsxs * huali1
        print(zeinan)
        print(k1,huali1)
        self.close()
class MyMainWindow36(QMainWindow, Ui_MainWindow36):
    def __init__(self, parent=None):
        super(MyMainWindow36, self).__init__(parent)
        self.setupUi(self)
        self.fffq_5.clicked.connect(self.fffq5_button)

    def fffq5_button(self):
        global k1
        global huali1
        global zeinan
        ffq5 = self.comboBox.currentText()
        if ffq5=="100":
            k1 = 0.48
            huali1 = 0.16
        elif ffq5 == "80":
            k1 = 0.56
            huali1 = 0.17
        elif ffq5 == "70":
            k1 = 0.60
            huali1 = 0.17
        elif ffq5 == "50":
            k1 = 0.73
            huali1 = 0.18
        elif ffq5 == "40":
            k1 = 0.81
            huali1 = 0.19
        elif ffq5 == "30":
            k1 = 0.93
            huali1 = 0.20
        zeinan = q_xsxs * huali1
        print(zeinan)
        print(k1,huali1)
        self.close()
class MyMainWindow37(QMainWindow, Ui_MainWindow37):
    def __init__(self, parent=None):
        super(MyMainWindow37, self).__init__(parent)
        self.setupUi(self)
        self.fffq_6.clicked.connect(self.fffq6_button)

    def fffq6_button(self):
        global k1
        global huali1
        global zeinan
        ffq6 = self.comboBox.currentText()
        if ffq6=="85":
            k1 = 0.48
            huali1 = 0.16
        elif ffq6 == "60":
            k1 = 0.59
            huali1 = 0.17
        elif ffq6 == "50":
            k1 = 0.66
            huali1 = 0.18
        elif ffq6 == "40":
            k1 = 0.74
            huali1 = 0.18
        elif ffq6 == "30":
            k1 = 0.86
            huali1 = 0.19
        elif ffq6 == "25":
            k1 = 0.93
            huali1 = 0.20
        zeinan = q_xsxs * huali1
        print(zeinan)
        print(k1,huali1)
        self.close()
class MyMainWindow38(QMainWindow, Ui_MainWindow38):
    def __init__(self, parent=None):
        super(MyMainWindow38, self).__init__(parent)
        self.setupUi(self)
        self.fffq_7.clicked.connect(self.fffq7_button)

    def fffq7_button(self):
        global k1
        global huali1
        global zeinan
        ffq7 = self.comboBox.currentText()
        if ffq7 == "85":
            k1 = 0.48
            huali1 = 0.16
        elif ffq7 == "60":
            k1 = 0.59
            huali1 = 0.17
        elif ffq7 == "50":
            k1 = 0.66
            huali1 = 0.18
        elif ffq7 == "40":
            k1 = 0.74
            huali1 = 0.18
        elif ffq7 == "30":
            k1 = 0.86
            huali1 = 0.19
        elif ffq7 == "25":
            k1 = 0.93
            huali1 = 0.20
        zeinan = q_xsxs * huali1
        print(zeinan)
        print(k1,huali1)
        self.close()
class MyMainWindow39(QMainWindow, Ui_MainWindow39):
    def __init__(self, parent=None):
        super(MyMainWindow39, self).__init__(parent)
        self.setupUi(self)
        self.fffq_8.clicked.connect(self.fffq8_button)

    def fffq8_button(self):
        global k1
        global huali1
        global zeinan
        ffq8 = self.comboBox.currentText()
        if ffq8 == "70":
            k1 = 0.47
            huali1 = 0.16
        elif ffq8 == "60":
            k1 = 0.51
            huali1 = 0.17
        elif ffq8 == "50":
            k1 = 0.58
            huali1 = 0.17
        elif ffq8 == "35":
            k1 = 0.71
            huali1 = 0.18
        elif ffq8 == "25":
            k1 = 0.84
            huali1 = 0.19
        elif ffq8 == "20":
            k1 = 0.93
            huali1 = 0.20
        zeinan = q_xsxs * huali1
        print(zeinan)
        print(k1,huali1)
        self.close()
class MyMainWindow40(QMainWindow, Ui_MainWindow40):
    def __init__(self, parent=None):
        super(MyMainWindow40, self).__init__(parent)
        self.setupUi(self)
        self.fffq_9.clicked.connect(self.fffq9_button)

    def fffq9_button(self):
        global k1
        global huali1
        global zeinan
        ffq9 = self.comboBox.currentText()
        if ffq9 == "110":
            k1 = 0.49
            huali1 = 0.17
        elif ffq9 == "80":
            k1 = 0.60
            huali1 = 0.18
        elif ffq9 == "50":
            k1 = 0.83
            huali1 = 0.20
        elif ffq9 == "40":
            k1 = 0.93
            huali1 = 0.21
        elif ffq9 == "30":
            k1 = 1.08
            huali1 = 0.22
        elif ffq9 == "25":
            k1 = 1.17
            huali1 = 0.23
        zeinan = q_xsxs * huali1
        print(zeinan)
        print(k1,huali1)
        self.close()
class MyMainWindow41(QMainWindow, Ui_MainWindow41):
    def __init__(self, parent=None):
        super(MyMainWindow41, self).__init__(parent)
        self.setupUi(self)
        self.fffq_10.clicked.connect(self.fffq10_button)

    def fffq10_button(self):
        global k1
        global huali1
        global zeinan
        ffq10 = self.comboBox.currentText()
        if ffq10 == "110":
            k1 = 0.49
            huali1 = 0.17
        elif ffq10 == "80":
            k1 = 0.60
            huali1 = 0.18
        elif ffq10 == "50":
            k1 = 0.83
            huali1 = 0.20
        elif ffq10 == "40":
            k1 = 0.93
            huali1 = 0.21
        elif ffq10 == "30":
            k1 = 1.08
            huali1 = 0.22
        elif ffq10 == "25":
            k1 = 1.17
            huali1 = 0.23
        zeinan = q_xsxs * huali1
        print(zeinan)
        print(k1,huali1)
        self.close()
class MyMainWindow42(QMainWindow, Ui_MainWindow42):
    def __init__(self, parent=None):
        super(MyMainWindow42, self).__init__(parent)
        self.setupUi(self)
        self.fffq_11.clicked.connect(self.fffq11_button)

    def fffq11_button(self):
        global k1
        global huali1
        global zeinan
        ffq11 = self.comboBox.currentText()
        if ffq11 == "95":
            k1 = 0.47
            huali1 = 0.17
        elif ffq11 == "70":
            k1 = 0.59
            huali1 = 0.18
        elif ffq11 == "50":
            k1 = 0.73
            huali1 = 0.19
        elif ffq11 == "40":
            k1 = 0.85
            huali1 = 0.20
        elif ffq11 == "30":
            k1 = 0.99
            huali1 = 0.22
        elif ffq11 == "25":
            k1 = 1.08
            huali1 = 0.23
        zeinan = q_xsxs * huali1
        print(zeinan)
        print(k1,huali1)
        self.close()
class MyMainWindow43(QMainWindow, Ui_MainWindow43):
    def __init__(self, parent=None):
        super(MyMainWindow43, self).__init__(parent)
        self.setupUi(self)
        self.fffq_12.clicked.connect(self.fffq12_button)

    def fffq12_button(self):
        global k1
        global huali1
        global zeinan
        ffq12 = self.comboBox.currentText()
        if ffq12 == "95":
            k1 = 0.47
            huali1 = 0.17
        elif ffq12 == "70":
            k1 = 0.59
            huali1 = 0.18
        elif ffq12 == "50":
            k1 = 0.73
            huali1 = 0.19
        elif ffq12 == "40":
            k1 = 0.85
            huali1 = 0.20
        elif ffq12 == "30":
            k1 = 0.99
            huali1 = 0.22
        elif ffq12 == "25":
            k1 = 1.08
            huali1 = 0.23
        zeinan = q_xsxs * huali1
        print(zeinan)
        print(k1,huali1)
        self.close()
class MyMainWindow44(QMainWindow, Ui_MainWindow44):
    def __init__(self, parent=None):
        super(MyMainWindow44, self).__init__(parent)
        self.setupUi(self)
        self.fffq_13.clicked.connect(self.fffq13_button)

    def fffq13_button(self):
        global k1
        global huali1
        global zeinan
        ffq13 = self.comboBox.currentText()
        if ffq13 == "75":
            k1 = 0.48
            huali1 = 0.18
        elif ffq13 == "65":
            k1 = 0.52
            huali1 = 0.18
        elif ffq13 == "55":
            k1 = 0.59
            huali1 = 0.19
        elif ffq13 == "40":
            k1 = 0.73
            huali1 = 0.20
        elif ffq13 == "30":
            k1 = 0.87
            huali1 = 0.21
        elif ffq13 == "25":
            k1 = 0.97
            huali1 = 0.22
        zeinan = q_xsxs * huali1
        print(zeinan)
        print(k1,huali1)
        self.close()
class MyMainWindow45(QMainWindow, Ui_MainWindow45):
    def __init__(self, parent=None):
        super(MyMainWindow45, self).__init__(parent)
        self.setupUi(self)
        self.fffq_14.clicked.connect(self.fffq14_button)

    def fffq14_button(self):
        global k1
        global huali1
        global zeinan
        ffq14 = self.comboBox.currentText()
        if ffq14 == "370":
            k1 = 1.49
            huali1 = 0.15
        elif ffq14 == "240":
            k1 = 1.94
            huali1 = 0.35
        zeinan = q_xsxs * huali1
        print(zeinan)
        print(k1,huali1)
        self.close()
class MyMainWindow46(QMainWindow, Ui_MainWindow46):
    def __init__(self, parent=None):
        super(MyMainWindow46, self).__init__(parent)
        self.setupUi(self)
        self.bububu.clicked.connect(self.ccc_button)
    def ccc_button(self):
        global k1
        global huali1
        global zeinan
        k1 = 1.59
        huali1 = 0.35
        zeinan = q_xsxs * huali1
        print(zeinan)
        print(k1,huali1)
        self.close()
class MyMainWindow47(QMainWindow, Ui_MainWindow47):
    def __init__(self, parent=None):
        super(MyMainWindow47, self).__init__(parent)
        self.setupUi(self)
        self.bububu_1.clicked.connect(self.ccc1_button)
    def ccc1_button(self):
        global k1
        global huali1
        global zeinan
        k1 = 1.59
        huali1 = 0.35
        zeinan = q_xsxs * huali1
        print(zeinan)
        print(k1, huali1)
        self.close()
class MyMainWindow48(QMainWindow, Ui_MainWindow48):
    def __init__(self, parent=None):
        super(MyMainWindow48, self).__init__(parent)
        self.setupUi(self)
        self.bububu_2.clicked.connect(self.ccc2_button)

    def ccc2_button(self):
        global k1
        global huali1
        global zeinan
        k1 = 1.59
        huali1 = 0.35
        zeinan = q_xsxs * huali1
        print(zeinan)
        print(k1, huali1)
        self.close()
class MyMainWindow49(QMainWindow, Ui_MainWindow49):
    def __init__(self, parent=None):
        super(MyMainWindow49, self).__init__(parent)
        self.setupUi(self)
        self.bububu_3.clicked.connect(self.ccc3_button)

    def ccc3_button(self):
        global k1
        global huali1
        global zeinan
        k1 = 1.59
        huali1 = 0.35
        zeinan = q_xsxs * huali1
        print(zeinan)
        print(k1, huali1)
        self.close()
class MyMainWindow50(QMainWindow, Ui_MainWindow50):
    def __init__(self, parent=None):
        super(MyMainWindow50, self).__init__(parent)
        self.setupUi(self)
        self.bububu_4.clicked.connect(self.ccc4_button)

    def ccc4_button(self):
        global k1
        global huali1
        global zeinan
        k1 = 1.59
        huali1 = 0.35
        zeinan = q_xsxs * huali1
        print(zeinan)
        print(k1, huali1)
        self.close()
class MyMainWindow51(QMainWindow, Ui_MainWindow51):
    def __init__(self, parent=None):
        super(MyMainWindow51, self).__init__(parent)
        self.setupUi(self)
        self.bububu_5.clicked.connect(self.ccc5_button)

    def ccc5_button(self):
        global k1
        global huali1
        global zeinan
        k1 = 1.59
        huali1 = 0.35
        zeinan = q_xsxs * huali1
        print(zeinan)
        print(k1, huali1)
        self.close()
class MyMainWindow52(QMainWindow, Ui_MainWindow52):
    def __init__(self, parent=None):
        super(MyMainWindow52, self).__init__(parent)
        self.setupUi(self)
        self.bububu_6.clicked.connect(self.ccc6_button)

    def ccc6_button(self):
        global k1
        global huali1
        global zeinan
        k1 = 1.59
        huali1 = 0.35
        zeinan = q_xsxs * huali1
        print(zeinan)
        print(k1, huali1)
        self.close()
class MyMainWindow53(QMainWindow, Ui_MainWindow53):
    def __init__(self, parent=None):
        super(MyMainWindow53, self).__init__(parent)
        self.setupUi(self)
        self.bububu_7.clicked.connect(self.ccc7_button)

    def ccc7_button(self):
        global huali1
        global k1
        global zeinan
        ffq_b1 = self.comboBox.currentText()
        if ffq_b1 == "175":
            k1 = 0.95
            huali1 = 0.75
        elif ffq_b1 == "200":
            k1 = 0.86
            huali1 = 0.68
        zeinan = q_xsxs *huali1
        print(zeinan)
        print(k1, huali1)
        self.close()
class MyMainWindow54(QMainWindow, Ui_MainWindow54):
    def __init__(self, parent=None):
        super(MyMainWindow54, self).__init__(parent)
        self.setupUi(self)
        self.bububu_8.clicked.connect(self.ccc8_button)

    def ccc8_button(self):
        global k1
        global huali1
        global zeinan
        k1 = 1.59
        huali1 = 0.35
        zeinan = q_xsxs * huali1
        print(zeinan)
        print(k1, huali1)
        self.close()
class MyMainWindow55(QMainWindow, Ui_MainWindow55):
    def __init__(self, parent=None):
        super(MyMainWindow55, self).__init__(parent)
        self.setupUi(self)
        self.bububu_9.clicked.connect(self.ccc9_button)

    def ccc9_button(self):
        global k1
        global huali1
        global zeinan
        k1 = 1.59
        huali1 = 0.35
        zeinan = q_xsxs * huali1
        print(zeinan)
        print(k1, huali1)
        self.close()
class MyMainWindow56(QMainWindow, Ui_MainWindow56):
    def __init__(self, parent=None):
        super(MyMainWindow56, self).__init__(parent)
        self.setupUi(self)
        self.bububu_11.clicked.connect(self.ccc11_button)

    def ccc11_button(self):
        global k1
        global huali1
        global zeinan
        ffq_11 = self.comboBox.currentText()
        if ffq_11 == "400":
            k1 = 2.15
            huali1 = 0.14
        elif ffq_11 == "350":
            k1 = 2.30
            huali1 = 0.18
        elif ffq_11 == "300":
            k1 = 2.48
            huali1 = 0.24
        elif ffq_11 == "250":
            k1 = 2.67
            huali1 = 0.31
        elif ffq_11 == "200":
            k1 = 2.92
            huali1 = 0.40
        zeinan = q_xsxs * huali1
        print(zeinan)
        print(k1,huali1)
        self.close()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    myWin = Ui_Form1()
    # my = Ui_Form32()
    # my.send_cs.connect(myWin.fangjian_button)
    # my.cs_button()

    # Qt.WindowMaximized
    myWin.show()
    sys.exit(app.exec_())


import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip, QPushButton, QDesktopWidget,
                             QMainWindow, QFileDialog, QInputDialog, QLineEdit)
from PyQt5.QtGui import QIcon, QFont, QPalette, QBrush, QPixmap, QPainter, QColor
from PyQt5.QtCore import QCoreApplication, QSize, pyqtSlot


class Interface_UI(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()  # 界面绘制交给InitUi方法

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        self.background_init()
        self.botton_init()
        self.resize(440, 900)
        self.setMinimumSize(440, 900)
        self.setMaximumSize(440, 900)
        self.center()  # 界面居中
        self.setWindowTitle('华为多屏协同')  # 设置窗口的标题
        self.setWindowIcon(QIcon('../resource/pic/huawei.jpg'))  # 设置窗口的图标引用华为图片
        self.show()  # 显示窗口

    def center(self):
        qr = self.frameGeometry()  # 获得窗口
        cp = QDesktopWidget().availableGeometry().center()  # 获得屏幕中心点
        qr.moveCenter(cp)  # 显示到屏幕中心
        self.move(qr.topLeft())

    def botton_init(self):
        app_pos = []
        for i in range(12):
            app_pos.append((40 + 100 * (i % 4), 60 + 120 * ((i // 4) + 4)))
        for i in range(12):
            botton_name = "btn_" + str(i)
            botton_name = QPushButton('Button', self)
            botton_name.resize(60, 60)  # btn.sizeHint()显示默认尺寸
            botton_name.move(app_pos[i][0], app_pos[i][1])  # 移动窗口的位置

        # 0-音乐
        btn_0 = QPushButton('', self)
        btn_0.resize(60, 60)
        btn_0.move(app_pos[0][0], app_pos[0][1])
        icon_0 = QIcon('../resource/pic/music.jpg')
        btn_0.setIcon(icon_0)
        size = QSize(60, 60)
        btn_0.setIconSize(size)
        btn_0.clicked.connect(self.click_0)
        # 1-日历
        btn_1 = QPushButton('', self)
        btn_1.resize(60, 60)
        btn_1.move(app_pos[1][0], app_pos[1][1])
        icon_1 = QIcon('../resource/pic/calendar.jpg')
        btn_1.setIcon(icon_1)
        size = QSize(60, 60)
        btn_1.setIconSize(size)
        btn_1.clicked.connect(self.click_1)
        # 2-时钟报时
        btn_2 = QPushButton('', self)
        btn_2.resize(60, 60)
        btn_2.move(app_pos[2][0], app_pos[2][1])
        icon_2 = QIcon('../resource/pic/time.png')
        btn_2.setIcon(icon_2)
        size = QSize(60, 60)
        btn_2.setIconSize(size)
        btn_2.clicked.connect(self.click_2)
        # 3-天气预报
        btn_3 = QPushButton('', self)
        btn_3.resize(60, 60)
        btn_3.move(app_pos[3][0], app_pos[3][1])
        icon_3 = QIcon('../resource/pic/weather.png')
        btn_3.setIcon(icon_3)
        size = QSize(60, 60)
        btn_3.setIconSize(size)
        btn_3.clicked.connect(self.click_3)
        # 4-百度百科查词
        btn_4 = QPushButton('', self)
        btn_4.resize(60, 60)
        btn_4.move(app_pos[4][0], app_pos[4][1])
        icon_4 = QIcon('../resource/pic/baike.png')
        btn_4.setIcon(icon_4)
        size = QSize(60, 60)
        btn_4.setIconSize(size)
        btn_4.clicked.connect(self.click_4)
        # 5-淘宝购物
        btn_5 = QPushButton('', self)
        btn_5.resize(60, 60)
        btn_5.move(app_pos[5][0], app_pos[5][1])
        icon_5 = QIcon('../resource/pic/taobao.png')
        btn_5.setIcon(icon_5)
        size = QSize(60, 60)
        btn_5.setIconSize(size)
        btn_5.clicked.connect(self.click_5)
        # 6-链家买房
        btn_6 = QPushButton('', self)
        btn_6.resize(60, 60)
        btn_6.move(app_pos[6][0], app_pos[6][1])
        icon_6 = QIcon('../resource/pic/buyhouse.png')
        btn_6.setIcon(icon_6)
        size = QSize(60, 60)
        btn_6.setIconSize(size)
        btn_6.clicked.connect(self.click_6)
        # 7-百度翻译
        btn_7 = QPushButton('', self)
        btn_7.resize(60, 60)
        btn_7.move(app_pos[7][0], app_pos[7][1])
        icon_7 = QIcon('../resource/pic/translate.jpg')
        btn_7.setIcon(icon_7)
        size = QSize(60, 60)
        btn_7.setIconSize(size)
        btn_7.clicked.connect(self.click_7)
        # 8-进击的小鸟
        btn_8 = QPushButton('', self)
        btn_8.resize(60, 60)
        btn_8.move(app_pos[8][0], app_pos[8][1])
        icon_8 = QIcon('../resource/pic/bird_icon.png')
        btn_8.setIcon(icon_8)
        size = QSize(60, 60)
        btn_8.setIconSize(size)
        btn_8.clicked.connect(self.click_8)
        # 9-王者荣耀
        btn_9 = QPushButton('', self)
        btn_9.resize(60, 60)
        btn_9.move(app_pos[9][0], app_pos[9][1])
        icon_9 = QIcon('../resource/pic/king_logo.png')
        btn_9.setIcon(icon_9)
        size = QSize(60, 60)
        btn_9.setIconSize(size)
        btn_9.clicked.connect(self.click_9)
        # 10-俄罗斯方块
        btn_10 = QPushButton('', self)
        btn_10.resize(60, 60)
        btn_10.move(app_pos[10][0], app_pos[10][1])
        icon_10 = QIcon('../resource/pic/tetris.png')
        btn_10.setIcon(icon_10)
        size = QSize(60, 60)
        btn_10.setIconSize(size)
        btn_10.clicked.connect(self.click_10)
        # 11-计算器
        btn_11 = QPushButton('', self)
        btn_11.resize(60, 60)
        btn_11.move(app_pos[11][0], app_pos[11][1])
        icon_11 = QIcon('../resource/pic/calculate.png')
        btn_11.setIcon(icon_11)
        size = QSize(60, 60)
        btn_11.setIconSize(size)
        btn_11.clicked.connect(self.click_11)

    @pyqtSlot()
    def click_0(self):
        print("运行音乐")
        os.system("python music.py")

    @pyqtSlot()
    def click_1(self):
        print("运行日历")
        os.system("python calendar.py")

    @pyqtSlot()
    def click_2(self):
        print("运行时钟")
        os.system("python timer.py")

    @pyqtSlot()
    def click_3(self):
        print("运行天气预报查询")
        os.system("python weather.py")

    @pyqtSlot()
    def click_4(self):
        print("运行词典")
        os.system("python wikipedia.py")

    @pyqtSlot()
    def click_5(self):
        print("运行淘宝购物")
        os.system("python taobao.py")

    @pyqtSlot()
    def click_6(self):
        print("运行链家查房价")
        os.system("python buy_house.py")

    @pyqtSlot()
    def click_7(self):
        print("运行百度翻译")
        os.system("python translation.py")

    @pyqtSlot()
    def click_8(self):
        print("运行进击的小鸟")
        os.system("python bird_main.py")

    @pyqtSlot()
    def click_9(self):
        print("运行五子棋")

    @pyqtSlot()
    def click_10(self):
        print("运行俄罗斯方块")
        os.system("python tetris.py")

    @pyqtSlot()
    def click_11(self):
        print("运行计算器")
        os.system("python calculate.py")

    def background_init(self):
        self.setWindowTitle("设置背景图片")
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("../resource/pic/phone_bg.png")))
        self.setPalette(window_pale)

        btn_pic = QPushButton('', self)
        btn_pic.resize(360, 420)
        btn_pic.move(40, 60)
        icon_pic = QIcon('../resource/pic/dolphins.jpg')
        btn_pic.setIcon(icon_pic)
        size = QSize(360, 420)
        btn_pic.setIconSize(size)


def begin_interface():
    app = QApplication(sys.argv)
    ex = Interface_UI()
    sys.exit(app.exec_())


if __name__ == '__main__':
    begin_interface()

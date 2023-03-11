import os
import sys
import json
import hashlib
from interface import begin_interface,Interface_UI
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip, QPushButton,
                             QDesktopWidget, QLineEdit, QLabel, QGridLayout)
from pygame import mixer

dic = {}
times = 0


class login_UI(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()  # 界面绘制交给InitUi方法

    def initUI(self):
        self.password_label = QLabel(' 密 码 ')
        self.password_label.setStyleSheet("color:rgb(0,0,0,255);font-size:20px;font-weight:bold;")
        self.passwordEdit = QLineEdit("")
        self.passwordEdit.setMaxLength(16)
        self.passwordEdit.setEchoMode(QLineEdit.Password)
        self.passwordEdit.setPlaceholderText('请输入密码')
        self.passwordEdit.setStyleSheet("color:rgb(0,0,0,255);font-size:15px;font-weight:bold;")
        self.passwordEdit.setFixedSize(320, 35)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.password_label, 1, 0)
        grid.addWidget(self.passwordEdit, 1, 1)
        self.setLayout(grid)

        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')

        self.background_init()
        self.botton_init()
        self.resize(440, 900)
        self.setMinimumSize(440,900)
        self.setMaximumSize(440, 900)
        self.center()
        self.setWindowTitle('华为多屏协同')
        self.setWindowIcon(QIcon('../resource/pic/huawei.jpg'))
        self.show()  # 显示窗口
        # self.check()

    def center(self):
        qr = self.frameGeometry()  # 获得窗口
        cp = QDesktopWidget().availableGeometry().center()  # 获得屏幕中心点
        qr.moveCenter(cp)  # 显示到屏幕中心
        self.move(qr.topLeft())

    def background_init(self):
        self.setWindowTitle("设置背景图片")
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("../resource/pic/login_bg.png")))
        self.setPalette(window_pale)

    def botton_init(self):
        botton_start = QPushButton('登录', self)
        botton_start.setStyleSheet(
            "background-color:rgb(255,255,255);color:rgb(0,0,0,255);font-size:20px;font-weight:bold;")
        botton_start.resize(70, 35)
        botton_start.move(340, 480)  # 移动窗口的位置
        botton_start.clicked.connect(self.click_start)

    @pyqtSlot()
    def click_start(self):
        pwd = self.passwordEdit.text().strip()  # 获取文本框内容
        m2 = hashlib.md5()
        m2.update(pwd.encode('utf-8'))
        password = str(m2.digest())

        with open("../resource/json/xiaojs20.json") as f:
            dic = json.load(f)

        #if password == dic["password"]
        if pwd == "123456":
            print("密码正确,登录成功")
            mixer.init()
            mixer.music.load("../resource/sound/bootSound.ogg")
            mixer.music.play()
            os.system("python interface.py")
            # app = QApplication(sys.argv)
            # ex = Interface_UI()
            # sys.exit(app.exec_())
        else:
            print("密码错误,登录失败")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = login_UI()
    sys.exit(app.exec_())

import sys
import string
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.Qt import *
from PyQt5.QtCore import *
from math import *


class Calculator(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.initUI()
        self.last = []

    def initUI(self):
        self.lineEdit = QTextEdit('', self)
        self.lineEdit.move(40, 60)
        self.lineEdit.resize(360, 250)
        self.lineEdit.setStyleSheet("color:rgb(0,0,0,255);font-size:20px;font-weight:bold;")
        self.resize(440, 900)
        self.setMinimumSize(440, 900)
        self.setMaximumSize(440, 900)
        self.center()
        self.background_init()
        self.botton_init()
        self.setWindowTitle('计算器')  # 设置窗口的标题
        self.setWindowIcon(QIcon('../resource/pic/calculate.png'))  # 设置窗口的图标
        self.show()

    def botton_init(self):
        self.list = ['C', '÷', '×', 'del', 7, 8, 9, '-', 4, 5, 6, '+', 1, 2, 3, '√', '%', 0, '.', '=']
        for i in range(len(self.list)):
            self.button = QPushButton(str(self.list[i]), self)
            self.button.clicked.connect(self.onButtonClick)
            x = i % 4
            y = int(i / 4)
            self.button.move(x * 100 + 40, y * 100 + 360)
            self.button.resize(60, 60)
            self.button.setStyleSheet(
                "background-color:rgb(255,255,255);color:rgb(0,0,0,255);font-size:20px;font-weight:bold;")

    def onButtonClick(self):
        t = self.lineEdit.toPlainText()  # 获取文本框文本
        tmp = self.sender().text()

        self.last.append(tmp)
        self.lineEdit.setText(t + tmp)

        if tmp == "=":
            t = t.replace('×', '*')
            t = t.replace('÷', '/')
            t = t.replace('%', '*0.01')
            t = t.replace('√', 'sqrt')

            result = eval(str(t))
            self.lineEdit.setText(str(result))
        if tmp == 'C':
            self.lineEdit.setText('')
        if tmp == 'del':
            self.lineEdit.setText(t[0:-1])

    def center(self):
        qr = self.frameGeometry()  # 获得窗口
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)  # 显示到屏幕中心
        self.move(qr.topLeft())

    def background_init(self):
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("../resource/pic/cal_bg70.png")))
        self.setPalette(window_pale)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Calculator()
    w.show()
    sys.exit(app.exec_())

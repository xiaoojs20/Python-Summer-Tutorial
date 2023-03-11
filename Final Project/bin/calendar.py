# 日历
import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QCalendarWidget, QApplication, \
    QLabel, QVBoxLayout, QDesktopWidget
from PyQt5.QtCore import QDate
from PyQt5.QtGui import *


class Calendar_UI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 将多个控件加入到qt的布局管理器中。建立一个箱布局
        vbox = QVBoxLayout(self)
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        # 点击日历，传入QDate数据，同showDate函数相关联
        cal.clicked[QDate].connect(self.showDate)

        # 把日历加入到这个箱子中
        vbox.addWidget(cal)
        # 显示选定的日期的label
        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        # 把label也加入到这个箱子中
        vbox.addWidget(self.lbl)
        # 要给vbox设置布局
        self.setLayout(vbox)

        self.resize(440, 900)
        self.setMinimumSize(440, 900)
        self.setMaximumSize(440, 900)
        self.center()
        self.background_init()
        self.setWindowTitle('日历')
        self.setWindowIcon(QIcon('../resource/pic/calendar.jpg'))  # 设置窗口的图标
        self.show()

    def center(self):
        qr = self.frameGeometry()  # 获得窗口
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)  # 显示到屏幕中心
        self.move(qr.topLeft())

    def background_init(self):
        self.setWindowTitle("设置背景图片")
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("../resource/pic/cal_bg70.png")))
        self.setPalette(window_pale)

    def showDate(self, date):
        self.lbl.setText(date.toString())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calendar_UI()
    sys.exit(app.exec_())

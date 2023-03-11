import sys
import time
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from math import *


class Timer(QWidget):
    def __init__(self):
        super().__init__()
        self.timer = QBasicTimer()
        self.timer.start(1000, self)
        self.initUI()

    def initUI(self):
        self.resize(440, 900)
        self.setWindowTitle("时钟")
        self.setWindowIcon(QIcon('../resource/pic/time.png'))
        self.center()
        self.background_init()
        self.lcd_init()
        # self.clock_init()

        # 两种时钟布局
        self.label1 = self.lcd
        # self.label2 = self.painter
        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        # layout.addWidget(self.label2)
        self.setLayout(layout)


    def lcd_init(self):
        # lcd数字屏
        self.lcd = QLCDNumber()
        self.lcd.setDigitCount(8)
        self.lcd.setMode(QLCDNumber.Dec)
        self.lcd.setSegmentStyle(QLCDNumber.Flat)
        self.lcd.move(100, 200)
        self.lcd.display(time.strftime("%X", time.localtime()))
        self.lcd.setStyleSheet("border: None;")  # 可以消除边框
    #
    # # 绘制时钟
    # def clock_init(self):
    #     # 时钟指针坐标点
    #     hourPoint = [QPoint(7, 8), QPoint(-7, 8), QPoint(0, -30)]
    #     minPoint = [QPoint(7, 8), QPoint(-7, 8), QPoint(0, -65)]
    #     secPoint = [QPoint(7, 8), QPoint(-7, 8), QPoint(0, -80)]
    #     # 时钟指针颜色
    #     hourColor = QColor(200, 100, 0, 200)
    #     minColor = QColor(0, 127, 127, 150)
    #     secColor = QColor(0, 160, 230, 150)
    #
    #     side = min(self.width(), self.height())
    #
    #     self.painter = QPainter(self)
    #     self.painter.setRenderHint(QPainter.Antialiasing)
    #     self.painter.translate(self.width() / 2, self.height() / 2)  # painter坐标系原点移至widget中央
    #     self.painter.scale(side / 200, side / 200)  # 缩放painterwidget坐标系，使绘制的时钟位于widge中央,即钟表支持缩放
    #
    #     # 绘制小时和分钟刻度线
    #     self.painter.save()
    #     for i in range(0, 60):
    #         if (i % 5) != 0:
    #             self.painter.setPen(minColor)
    #             self.painter.drawLine(92, 0, 96, 0)  # 绘制分钟刻度线
    #         else:
    #             self.painter.setPen(hourColor)
    #             self.painter.drawLine(88, 0, 96, 0)  # 绘制小时刻度线
    #         self.painter.rotate(360 / 60)
    #     self.painter.restore()
    #
    #     # 绘制小时数字
    #     self.painter.save()
    #     font = self.painter.font()
    #     font.setBold(True)
    #     self.painter.setFont(font)
    #     pointSize = font.pointSize()
    #     self.painter.setPen(hourColor)
    #     nhour = 0
    #     radius = 100
    #     for i in range(0, 12):
    #         nhour = i + 3  # 按QT-Qpainter的坐标系换算，3小时的刻度线对应坐标轴0度
    #         if nhour > 12:
    #             nhour = nhour - 12
    #
    #         x = radius * 0.8 * cos(i * 30 * pi / 180.0) - pointSize
    #         y = radius * 0.8 * sin(i * 30 * pi / 180.0) - pointSize / 2.0
    #         width = pointSize * 2
    #         height = pointSize
    #         self.painter.drawText(QRectF(x, y, width, height), Qt.AlignCenter, str(nhour))
    #     self.painter.restore()
    #
    #     time = QTime.currentTime()
    #
    #     # 绘制小时指针
    #     self.painter.save()
    #     self.painter.setPen(Qt.NoPen)  # 无轮廓线
    #     self.painter.setBrush(hourColor)  # 填充色
    #     self.painter.rotate(30 * (time.hour() + time.minute() / 60))  # 每圈360° = 12h 即：旋转角度 = 小时数 * 30°
    #     self.painter.drawConvexPolygon(QPolygonF(hourPoint))
    #     self.painter.restore()
    #
    #     # 绘制分钟指针
    #     self.painter.save()
    #     self.painter.setPen(Qt.NoPen)  # 无轮廓线
    #     self.painter.setBrush(minColor)  # 填充色
    #     self.painter.rotate(6 * (time.minute() + time.second() / 60))  # 每圈360° = 60m 即：旋转角度 = 分钟数 * 6°
    #     self.painter.drawConvexPolygon(QPolygonF(minPoint))
    #     self.painter.restore()
    #
    #     # 绘制秒钟指针
    #     self.painter.save()
    #     self.painter.setPen(Qt.NoPen)  # 无轮廓线
    #     self.painter.setBrush(secColor)  # 填充色
    #     self.painter.rotate(6 * time.second())
    #     self.painter.drawConvexPolygon(QPolygonF(secPoint))  # 每圈360° = 60s 即：旋转角度 = 秒数 * 6°
    #     self.painter.restore()

    def center(self):
        qr = self.frameGeometry()  # 获得窗口
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)  # 显示到屏幕中心
        self.move(qr.topLeft())

    def background_init(self):
        self.setWindowTitle("时钟")
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("../resource/pic/cal_bg70.png")))
        self.setPalette(window_pale)

    # 计时器事件处理
    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            self.lcd.display(time.strftime("%X", time.localtime()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    timer = Timer()
    timer.show()
    sys.exit(app.exec_())

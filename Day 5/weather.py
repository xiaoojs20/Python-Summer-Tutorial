# 天气预报
import sys
from bs4 import BeautifulSoup
from selenium import webdriver
from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip, QPushButton,
                             QDesktopWidget, QLineEdit, QLabel, QGridLayout)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot


class weather_UI(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()  # 界面绘制交给InitUi方法

    def initUI(self):
        self.place_label = QLabel(' 输入地方     ')
        self.placeEdit = QLineEdit(" ")
        self.weather_label = QLabel(' 查询结果     ')
        self.weatherEdit = QLineEdit(" ")
        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.place_label, 1, 0)
        grid.addWidget(self.placeEdit, 1, 1)
        grid.addWidget(self.weather_label, 2, 0)
        grid.addWidget(self.weatherEdit, 2, 1)

        self.setLayout(grid)

        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        self.botton_init()
        self.resize(440, 900)
        self.center()  # 界面居中
        self.setWindowTitle('天气预报')  # 设置窗口的标题
        self.setWindowIcon(QIcon('pic/weather.png'))
        self.show()  # 显示窗口

    def center(self):
        qr = self.frameGeometry()  # 获得窗口
        cp = QDesktopWidget().availableGeometry().center()  # 获得屏幕中心点
        qr.moveCenter(cp)  # 显示到屏幕中心
        self.move(qr.topLeft())

    def botton_init(self):
        botton_translate = QPushButton('search', self)
        botton_translate.resize(100, 35)  # btn.sizeHint()显示默认尺寸
        botton_translate.move(320, 340)  # 移动窗口的位置
        botton_translate.clicked.connect(self.click_search)

    @pyqtSlot()
    def click_search(self):
        self.place = self.placeEdit.text().strip()  # 获取文本框内容
        self.check_weather_forecast()

    def check_weather_forecast(self):
        url = "https://www.qixiangwang.cn/" + self.place + ".htm"

        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        driver = webdriver.Chrome(options=option)
        driver.get(url)

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        weather_strs = soup.select("div.tqqk li")
        weather_str = " "
        for i in range(len(weather_str)):
            weather_strs[i] = weather_strs[i].text.strip()
            # weather_str += weather_strs[i]

        print(weather_strs)
        self.weatherEdit.setText(weather_str)
        driver.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = weather_UI()
    sys.exit(app.exec_())

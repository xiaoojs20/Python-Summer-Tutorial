# 天气预报
import sys
from bs4 import BeautifulSoup
from selenium import webdriver
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot


class Weather_UI(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()  # 界面绘制交给InitUi方法

    def initUI(self):
        self.place_label = QLabel(' 输入地方 ')
        self.place_label.setStyleSheet("color:rgb(0,0,0,255);font-size:20px;font-weight:bold;")
        self.placeEdit = QLineEdit("")
        self.placeEdit.setFixedSize(290, 30)
        self.placeEdit.setPlaceholderText('请用拼音输入地级市名称')
        self.placeEdit.setStyleSheet("color:rgb(0,0,0,255);font-size:15px;font-weight:bold;")
        self.weather_browser = QTextBrowser()
        self.weather_browser.setFixedSize(290, 400)
        self.weather_browser.setStyleSheet("color:rgb(0,0,0,255);font-size:15px;font-weight:bold;")
        self.weather_cmb = QComboBox()
        self.weather_cmb.setStyle(QStyleFactory.create('Fusion'))
        self.weather_cmb.addItem('天气情况')
        self.weather_cmb.addItem('空气质量')
        self.weather_cmb.addItem('生活指数')
        self.weather_cmb.setFixedSize(120, 30)
        self.weather_cmb.setStyleSheet("color:rgb(0,0,0,255);font-size:18px;font-weight:bold;")

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.place_label, 1, 0)
        grid.addWidget(self.placeEdit, 1, 1)
        grid.addWidget(self.weather_cmb, 2, 0)
        grid.addWidget(self.weather_browser, 2, 1)

        self.setLayout(grid)

        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        self.background_init()
        self.botton_init()
        self.resize(440, 900)
        self.setMinimumSize(440, 900)
        self.setMaximumSize(440, 900)
        self.center()
        self.setWindowTitle('天气预报')  # 设置窗口的标题
        self.setWindowIcon(QIcon('../resource/pic/weather.png'))
        self.show()

    def center(self):
        qr = self.frameGeometry()  # 获得窗口
        cp = QDesktopWidget().availableGeometry().center()  # 获得屏幕中心点
        qr.moveCenter(cp)  # 显示到屏幕中心
        self.move(qr.topLeft())

    def background_init(self):
        self.setWindowTitle("设置背景图片")
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("../resource/pic/blue-sky-clouds-field.png")))
        self.setPalette(window_pale)

    def botton_init(self):
        botton_search = QPushButton('查 询', self)
        botton_search.resize(100, 35)
        botton_search.setStyleSheet(
            "background-color:rgb(255,255,255);color:rgb(0,0,0,255);font-size:20px;font-weight:bold;")
        botton_search.move(320, 240)  # 移动窗口的位置
        botton_search.clicked.connect(self.click_search)

    @pyqtSlot()
    def click_search(self):
        self.place = self.placeEdit.text().strip()  # 获取文本框内容
        if self.place:
            self.check_weather_forecast()
        else:
            pass

    def check_weather_forecast(self):
        url = "https://www.qixiangwang.cn/" + self.place + ".htm"

        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        driver = webdriver.Chrome(options=option)
        driver.get(url)

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        if self.weather_cmb.currentIndex() == 0:
            weather_strs = soup.select("div.tqqk li")
            weather_str = ""
            for i in range(len(weather_strs)):
                weather_strs[i] = weather_strs[i].text.strip()
                weather_str += (weather_strs[i] + "\n" * 2)

            print(weather_str)
            self.weather_browser.clear()
            self.weather_browser.append(weather_str)
        elif self.weather_cmb.currentIndex() == 1:
            weather_strs = soup.select("div.aqikuang")
            weather_str = ""
            for i in range(len(weather_strs)):
                weather_strs[i] = weather_strs[i].text.strip()
                weather_str += (weather_strs[i] + "\n" * 2)
            weather_str = weather_str[:-5]
            print(weather_str)
            self.weather_browser.clear()
            self.weather_browser.append(weather_str)
        elif self.weather_cmb.currentIndex() == 2:
            weather_strs = soup.select("div.bbox_c3")
            print(weather_strs)
            weather_str = ""
            for i in range(len(weather_strs)):
                weather_strs[i] = weather_strs[i].text.strip()
                weather_str += weather_strs[i]
            weather_str = weather_str[:-1]
            print(weather_str)
            self.weather_browser.clear()
            self.weather_browser.append(weather_str)

        driver.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Weather_UI()
    sys.exit(app.exec_())

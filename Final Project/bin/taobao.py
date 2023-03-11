import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot
from bs4 import BeautifulSoup
from selenium import webdriver


class Buyhouse_UI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.movie_label = QLabel(' 电影名称 ')
        self.movie_label.setStyleSheet("color:rgb(0,0,0,255);font-size:20px;font-weight:bold;")
        self.movieEdit = QLineEdit("")
        self.movieEdit.setPlaceholderText('请输入电影名称')
        self.movieEdit.setFixedSize(290, 30)
        self.movieEdit.setStyleSheet("color:rgb(0,0,0,255);font-size:15px;font-weight:bold;")
        self.price_browser = QTextBrowser()
        self.price_browser.setFixedSize(290, 400)
        self.price_browser.setStyleSheet("color:rgb(0,0,0,255);font-size:15px;font-weight:bold;")

        # 省-市-区选择
        # 省
        self.province_cmb = QComboBox()
        self.province_cmb.setStyle(QStyleFactory.create('Fusion'))
        self.province_cmb.addItem('北京市')
        self.province_cmb.setFixedSize(120, 30)
        self.province_cmb.setStyleSheet("color:rgb(0,0,0,255);font-size:18px;font-weight:bold;")

        # 市
        self.city_cmb = QComboBox()
        self.city_cmb.setStyle(QStyleFactory.create('Fusion'))
        self.city_cmb.addItem('北京市')
        self.city_cmb.setFixedSize(120, 30)
        self.city_cmb.setStyleSheet("color:rgb(0,0,0,255);font-size:18px;font-weight:bold;")

        # 区
        self.distrit_cmb = QComboBox()
        self.distrit_cmb.setStyle(QStyleFactory.create('Fusion'))
        self.distrit_cmb.addItem('海淀区')
        self.distrit_cmb.addItem('朝阳区')
        self.distrit_cmb.setFixedSize(120, 30)
        self.distrit_cmb.setStyleSheet("color:rgb(0,0,0,255);font-size:18px;font-weight:bold;")

        # 网站名选择
        self.web_cmb = QComboBox()
        self.web_cmb.setStyle(QStyleFactory.create('Fusion'))
        self.web_cmb.addItem('猫眼电影')
        self.web_cmb.addItem('淘票票')
        self.web_cmb.setFixedSize(120, 30)
        self.web_cmb.setStyleSheet("color:rgb(0,0,0,255);font-size:18px;font-weight:bold;")

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.province_cmb, 1, 0)
        grid.addWidget(self.city_cmb, 1, 1)
        grid.addWidget(self.distrit_cmb, 1, 2)
        grid.addWidget(self.movie_label, 2, 0)
        grid.addWidget(self.movieEdit, 2, 1)
        grid.addWidget(self.web_cmb, 3, 0)
        grid.addWidget(self.price_browser, 3, 1)

        self.setLayout(grid)

        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        self.background_init()
        self.botton_init()
        self.resize(440, 900)
        self.setMinimumSize(440, 900)
        self.setMaximumSize(440, 900)
        self.center()
        self.setWindowTitle('电影查询')
        self.setWindowIcon(QIcon('../resource/pic/taobao.png'))
        self.show()

    def center(self):
        qr = self.frameGeometry()  # 获得窗口
        cp = QDesktopWidget().availableGeometry().center()  # 获得屏幕中心点
        qr.moveCenter(cp)  # 显示到屏幕中心
        self.move(qr.topLeft())

    def background_init(self):
        self.setWindowTitle("设置背景图片")
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("../resource/pic/movie.png")))
        self.setPalette(window_pale)

    def botton_init(self):
        botton_hitmovie = QPushButton('热映电影', self)
        botton_hitmovie.resize(100, 35)
        botton_hitmovie.setStyleSheet(
            "background-color:rgb(255,255,255);color:rgb(0,0,0,255);font-size:20px;font-weight:bold;")
        botton_hitmovie.move(40, 300)
        botton_hitmovie.clicked.connect(self.click_hit)

        botton_info = QPushButton('详细信息', self)
        botton_info.resize(100, 35)
        botton_info.setStyleSheet(
            "background-color:rgb(255,255,255);color:rgb(0,0,0,255);font-size:20px;font-weight:bold;")
        botton_info.move(170, 300)  # 移动窗口的位置
        botton_info.clicked.connect(self.click_info)

        botton_price = QPushButton('查询票价', self)
        botton_price.resize(100, 35)
        botton_price.setStyleSheet(
            "background-color:rgb(255,255,255);color:rgb(0,0,0,255);font-size:20px;font-weight:bold;")
        botton_price.move(300, 300)  # 移动窗口的位置
        botton_price.clicked.connect(self.click_price)

    @pyqtSlot()
    def click_hit(self):
        url = "https://movie.douban.com/cinema/nowplaying/beijing/"
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        driver = webdriver.Chrome(options=option)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        hit_movie_name = soup.select("li.stitle>a")[0:15]
        hit_movie_name_str = ""
        for idx in range(len(hit_movie_name)):
            hit_movie_name[idx] = hit_movie_name[idx]["title"].strip()
            hit_movie_name_str += (hit_movie_name[idx] + "\n")
        print(hit_movie_name_str)
        self.price_browser.clear()
        self.price_browser.append(hit_movie_name_str)

    @pyqtSlot()
    def click_info(self):
        self.place = self.placeEdit.text().strip()  # 获取文本框内容
        if self.place:
            self.movie_price()
        else:
            pass

    def movie_info(self):
       pass

    @pyqtSlot()
    def click_price(self):
        self.place = self.placeEdit.text().strip()  # 获取文本框内容
        if self.place:
            self.movie_price()
        else:
            pass

    def movie_price(self):
        url = "https://bj.lianjia.com/ershoufang/rs" + self.place + "/"

        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        driver = webdriver.Chrome(options=option)
        driver.get(url)

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        house_name_list = []
        house_place_list = []
        house_room_list = []
        house_type_list = []
        house_square_list = []
        house_floor_list = []
        house_time_list = []
        house_info_list = []

        house_name = soup.select("div.leftContent>ul.sellListContent")
        if len(house_name) == 0:
            print("这附近没有可卖二手房")
            exit()
        h = house_name[0]
        all_house_name = h.select("div.positionInfo a")
        researched_house_name = []
        for i in range(len(all_house_name)):
            researched_house_name.append(all_house_name[i].text.strip())

        for i in range(len(researched_house_name)):
            if i % 2 == 0:
                house_name_list.append(researched_house_name[i])
            else:
                house_place_list.append(researched_house_name[i])

        house_info = h.select("div.houseInfo")
        for i in range(len(house_info)):
            house_info[i] = house_info[i].text.strip()
            infos = house_info[i].split('|')
            house_room_list.append(infos[0].strip())
            house_square_list.append(infos[1].strip())
            house_floor_list.append(infos[4].strip())
            house_time_list.append(infos[5].strip())
            house_type_list.append(infos[6].strip())

        price = h.select("div.unitPrice span")
        for i in range(len(price)):
            price[i] = price[i].text.strip()

        tprice = h.select("div.totalPrice span")
        for i in range(len(tprice)):
            tprice[i] = tprice[i].text.strip()
        for i in range(len(house_name_list)):
            dic = {"小区名称": house_name_list[i], "户型": house_room_list[i], "面积": house_square_list[i],
                   "总价": tprice[i] + '万', "单价": price[i],
                   "楼层位置": house_floor_list[i], "建筑时间": house_time_list[i], "建筑类型": house_type_list[i],
                   "发布时间": house_time_list[i]}
            house_info_list.append(dic)

        avg = 0
        house_info_str = ""
        for i in range(len(house_info_list)):
            house_info_str += (str(house_info_list[i])[1:-1] + "\n" * 2)
            tmp = float(tprice[i])
            avg += tmp

        avg /= len(house_info_list)
        avg_str = self.place + "附近的平均二手房价为" + str(avg) + "万元"

        all_str = avg_str + "\n" * 2 + house_info_str
        print(all_str)

        if self.house_cmb.currentIndex() == 0:
            self.price_browser.clear()
            self.price_browser.append(avg_str)
        elif self.house_cmb.currentIndex() == 1:
            self.price_browser.clear()
            self.price_browser.append(house_info_str)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Buyhouse_UI()
    sys.exit(app.exec_())

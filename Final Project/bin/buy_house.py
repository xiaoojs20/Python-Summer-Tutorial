import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot
from bs4 import BeautifulSoup
from selenium import webdriver


class Buyhouse_UI(QWidget):
    price = ""

    def __init__(self):
        super().__init__()
        self.initUI()  # 界面绘制交给InitUi方法

    def initUI(self):
        self.place_label = QLabel(' 输入地段 ')
        self.place_label.setStyleSheet("color:rgb(0,0,0,255);font-size:20px;font-weight:bold;")
        self.placeEdit = QLineEdit("")
        self.placeEdit.setPlaceholderText('请输入地区名称')
        self.placeEdit.setFixedSize(290, 30)
        self.placeEdit.setStyleSheet("color:rgb(0,0,0,255);font-size:15px;font-weight:bold;")
        self.price_browser = QTextBrowser()
        self.price_browser.setFixedSize(290, 400)
        self.price_browser.setStyleSheet("color:rgb(0,0,0,255);font-size:15px;font-weight:bold;")
        self.house_cmb = QComboBox()
        self.house_cmb.setStyle(QStyleFactory.create('Fusion'))
        self.house_cmb.addItem('平均总价')
        self.house_cmb.addItem('详细信息')
        self.house_cmb.setFixedSize(120, 30)
        self.house_cmb.setStyleSheet("color:rgb(0,0,0,255);font-size:18px;font-weight:bold;")

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.place_label, 1, 0)
        grid.addWidget(self.placeEdit, 1, 1)
        grid.addWidget(self.house_cmb, 2, 0)
        grid.addWidget(self.price_browser, 2, 1)

        self.setLayout(grid)

        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        self.background_init()
        self.botton_init()
        self.resize(440, 900)
        self.setMinimumSize(440, 900)
        self.setMaximumSize(440, 900)
        self.center()
        self.setWindowTitle('链家查房价')
        self.setWindowIcon(QIcon('../resource/pic/buyhouse.png'))
        self.show()

    def center(self):
        qr = self.frameGeometry()  # 获得窗口
        cp = QDesktopWidget().availableGeometry().center()  # 获得屏幕中心点
        qr.moveCenter(cp)  # 显示到屏幕中心
        self.move(qr.topLeft())

    def background_init(self):
        self.setWindowTitle("设置背景图片")
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("../resource/pic/house_bg.png")))
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
            self.buy_house()
        else:
            pass

    def buy_house(self):
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

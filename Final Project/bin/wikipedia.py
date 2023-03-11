import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip, QPushButton, QTextBrowser,
                             QDesktopWidget, QLineEdit, QLabel, QGridLayout)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot
from bs4 import BeautifulSoup
from selenium import webdriver


class Wikipedia_UI(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()  # 界面绘制交给InitUi方法

    def initUI(self):
        self.input_word_label = QLabel(' 输入词语 ')
        self.input_word_label.setStyleSheet("color:rgb(255,255,255,255);font-size:20px;font-weight:bold;")
        self.input_word_Edit = QLineEdit("")
        self.input_word_Edit.setFixedSize(290, 30)
        self.input_word_Edit.setPlaceholderText('请输入检索词语')
        self.input_word_Edit.setStyleSheet("color:rgb(0,0,0,255);font-size:15px;font-weight:bold;")
        self.paraphrase_label = QLabel(' 词语解释 ')
        self.paraphrase_label.setStyleSheet("color:rgb(255,255,255,255);font-size:20px;font-weight:bold;")
        self.paraphrase_browser = QTextBrowser()
        self.paraphrase_browser.setFixedSize(290, 400)
        self.paraphrase_browser.setStyleSheet("color:rgb(0,0,0,255);font-size:15px;font-weight:bold;")

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.input_word_label, 1, 0)
        grid.addWidget(self.input_word_Edit, 1, 1)

        grid.addWidget(self.paraphrase_label, 2, 0)
        grid.addWidget(self.paraphrase_browser, 2, 1)

        self.setLayout(grid)

        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        self.background_init()
        self.botton_init()
        self.resize(440, 900)
        self.setMinimumSize(440, 900)
        self.setMaximumSize(440, 900)
        self.center()  # 界面居中
        self.setWindowTitle('百科全书')  # 设置窗口的标题
        self.setWindowIcon(QIcon('../resource/pic/baike.png'))
        self.show()  # 显示窗口

    def center(self):
        qr = self.frameGeometry()  # 获得窗口
        cp = QDesktopWidget().availableGeometry().center()  # 获得屏幕中心点
        qr.moveCenter(cp)  # 显示到屏幕中心
        self.move(qr.topLeft())

    def background_init(self):
        self.setWindowTitle("设置背景图片")
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("../resource/pic/cat.png")))
        self.setPalette(window_pale)

    def botton_init(self):
        botton_search = QPushButton('查看解释', self)
        botton_search.resize(100, 35)
        botton_search.setStyleSheet(
            "background-color:rgb(255,255,255);color:rgb(0,0,0,255);font-size:20px;font-weight:bold;")
        botton_search.move(320, 240)
        botton_search.clicked.connect(self.click_search)

    @pyqtSlot()
    def click_search(self):
        self.word = self.input_word_Edit.text().strip()  # 获取文本框内容
        if self.word:
            self.search_word()
        else:
            pass

    def search_word(self):

        url = "https://www.zdic.net/hans/" + self.word
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        driver = webdriver.Chrome(options=option)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        para_value = soup.select("span.gc_sy")

        if len(para_value) == 0:
            self.paraphrase_browser.append("没找到该词语")

        for i in range(len(para_value)):
            para_value[i] = para_value[i].text.strip()
        self.para = para_value[0]
        print(self.para)
        self.paraphrase_browser.clear()
        self.paraphrase_browser.append(self.para)

        driver.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Wikipedia_UI()
    sys.exit(app.exec_())

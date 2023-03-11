# translation
import sys
from bs4 import BeautifulSoup
from selenium import webdriver
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot, QSize


class Translate_UI(QWidget):
    translated_label = ""

    def __init__(self):
        super().__init__()
        self.initUI()  # 界面绘制交给InitUi方法

    def initUI(self):
        self.word_label = QLabel(' 输入文字 ')
        self.word_label.setStyleSheet("color:rgb(0,0,0,255);font-size:20px;font-weight:bold;")
        self.wordEdit = QTextEdit("")
        self.wordEdit.setFixedSize(290, 50)
        self.wordEdit.setPlaceholderText('请输入文字')
        self.wordEdit.setStyleSheet("color:rgb(0,0,0,255);font-size:15px;font-weight:bold;")
        self.t_browser = QTextBrowser()
        self.t_browser.setFixedSize(290, 400)
        self.t_browser.setStyleSheet("color:rgb(0,0,0,255);font-size:15px;font-weight:bold;")
        self.t_cmb = QComboBox()
        self.t_cmb.setStyle(QStyleFactory.create('Fusion'))
        self.t_cmb.addItem('中英转换')
        self.t_cmb.addItem('中日转换')
        self.t_cmb.addItem('中法转换')
        self.t_cmb.addItem('中俄转换')
        self.t_cmb.addItem('中德转换')
        self.t_cmb.setFixedSize(120, 30)
        self.t_cmb.setStyleSheet("color:rgb(0,0,0,255);font-size:18px;font-weight:bold;")

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.word_label, 1, 0)
        grid.addWidget(self.wordEdit, 1, 1)
        grid.addWidget(self.t_cmb, 2, 0)
        grid.addWidget(self.t_browser, 2, 1)
        self.setLayout(grid)

        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        self.background_init()
        self.botton_init()
        self.resize(440, 900)
        self.setMinimumSize(440, 900)
        self.setMaximumSize(440, 900)
        self.center()
        self.setWindowTitle('百度翻译')  # 设置窗口的标题
        self.setWindowIcon(QIcon('../resource/pic/translate.jpg'))
        self.show()

    def center(self):
        qr = self.frameGeometry()  # 获得窗口
        cp = QDesktopWidget().availableGeometry().center()  # 获得屏幕中心点
        qr.moveCenter(cp)  # 显示到屏幕中心
        self.move(qr.topLeft())

    def background_init(self):
        self.setWindowTitle("设置背景图片")
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(),
                             QtGui.QBrush(QtGui.QPixmap("../resource/pic/keyboard-free-stock-photo.png")))
        self.setPalette(window_pale)

    def botton_init(self):
        botton_translate = QPushButton('翻译', self)
        botton_translate.resize(100, 35)
        botton_translate.setStyleSheet(
            "background-color:rgb(255,255,255);color:rgb(0,0,0,255);font-size:20px;font-weight:bold;")
        botton_translate.move(320, 240)  # 移动窗口的位置
        botton_translate.clicked.connect(self.click_translate)

    def check_chinese(self, str):
        if u'\u4e00' <= str[0] <= u'\u9fff':
            return True
        else:
            return False

    @pyqtSlot()
    def click_translate(self):
        self.word = self.wordEdit.toPlainText().strip()  # 获取文本框内容
        self.isChinese = self.check_chinese(self.word)
        if self.word:
            self.translate()
        else:
            pass

    def translate(self):
        # 中英转换
        if self.t_cmb.currentIndex() == 0:
            if self.isChinese:
                cn = self.word.strip()
                url = "https://fanyi.baidu.com/#zh/en/" + cn

                option = webdriver.ChromeOptions()
                option.add_argument('headless')
                driver = webdriver.Chrome(options=option)
                driver.get(url)
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                en = soup.select("p.target-output span")
                en = en[0].text.strip()

                Translate_UI.translated_label = en
                print(en)
                self.t_browser.clear()
                self.t_browser.append(en)
                driver.close()
            else:
                en = self.word.strip()
                en = en.replace(" ", "%20")
                url = "https://fanyi.baidu.com/#en/zh/" + en
                option = webdriver.ChromeOptions()
                option.add_argument('headless')
                driver = webdriver.Chrome(options=option)
                driver.get(url)
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                cn = soup.select("p.target-output span")
                cn = cn[0].text.strip()

                Translate_UI.translated_label = cn
                print(cn)
                self.t_browser.clear()
                self.t_browser.append(cn)
                driver.close()
        # 中日转换
        elif self.t_cmb.currentIndex() == 1:
            if self.isChinese:
                cn = self.word.strip()
                url = "https://fanyi.baidu.com/#zh/jp/" + cn

                option = webdriver.ChromeOptions()
                option.add_argument('headless')
                driver = webdriver.Chrome(options=option)
                driver.get(url)
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                en = soup.select("p.target-output span")
                en = en[0].text.strip()

                Translate_UI.translated_label = en
                print(en)
                self.t_browser.clear()
                self.t_browser.append(en)
                driver.close()
            else:
                en = self.word.strip()
                en = en.replace(" ", "%20")
                url = "https://fanyi.baidu.com/#jp/zh/" + en
                option = webdriver.ChromeOptions()
                option.add_argument('headless')
                driver = webdriver.Chrome(options=option)
                driver.get(url)
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                cn = soup.select("p.target-output span")
                cn = cn[0].text.strip()

                Translate_UI.translated_label = cn
                print(cn)
                self.t_browser.clear()
                self.t_browser.append(cn)
                driver.close()

        # 中法转换
        elif self.t_cmb.currentIndex() == 2:
            if self.isChinese:
                cn = self.word.strip()
                url = "https://fanyi.baidu.com/#zh/fra/" + cn

                option = webdriver.ChromeOptions()
                option.add_argument('headless')
                driver = webdriver.Chrome(options=option)
                driver.get(url)
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                en = soup.select("p.target-output span")
                en = en[0].text.strip()

                Translate_UI.translated_label = en
                print(en)
                self.t_browser.clear()
                self.t_browser.append(en)
                driver.close()
            else:
                en = self.word.strip()
                en = en.replace(" ", "%20")
                url = "https://fanyi.baidu.com/#fra/zh/" + en
                option = webdriver.ChromeOptions()
                option.add_argument('headless')
                driver = webdriver.Chrome(options=option)
                driver.get(url)
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                cn = soup.select("p.target-output span")
                cn = cn[0].text.strip()

                Translate_UI.translated_label = cn
                print(cn)
                self.t_browser.clear()
                self.t_browser.append(cn)
                driver.close()

        # 中俄转换
        elif self.t_cmb.currentIndex() == 3:
            if self.isChinese:
                cn = self.word.strip()
                url = "https://fanyi.baidu.com/#zh/ru/" + cn

                option = webdriver.ChromeOptions()
                option.add_argument('headless')
                driver = webdriver.Chrome(options=option)
                driver.get(url)
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                en = soup.select("p.target-output span")
                en = en[0].text.strip()

                Translate_UI.translated_label = en
                print(en)
                self.t_browser.clear()
                self.t_browser.append(en)
                driver.close()
            else:
                en = self.word.strip()
                en = en.replace(" ", "%20")
                url = "https://fanyi.baidu.com/#ru/zh/" + en
                option = webdriver.ChromeOptions()
                option.add_argument('headless')
                driver = webdriver.Chrome(options=option)
                driver.get(url)
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                cn = soup.select("p.target-output span")
                cn = cn[0].text.strip()

                Translate_UI.translated_label = cn
                print(cn)
                self.t_browser.clear()
                self.t_browser.append(cn)
                driver.close()

        # 中德转换
        elif self.t_cmb.currentIndex() == 4:
            if self.isChinese:
                cn = self.word.strip()
                url = "https://fanyi.baidu.com/#zh/de/" + cn

                option = webdriver.ChromeOptions()
                option.add_argument('headless')
                driver = webdriver.Chrome(options=option)
                driver.get(url)
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                en = soup.select("p.target-output span")
                en = en[0].text.strip()

                Translate_UI.translated_label = en
                print(en)
                self.t_browser.clear()
                self.t_browser.append(en)
                driver.close()
            else:
                en = self.word.strip()
                en = en.replace(" ", "%20")
                url = "https://fanyi.baidu.com/#de/zh/" + en
                option = webdriver.ChromeOptions()
                option.add_argument('headless')
                driver = webdriver.Chrome(options=option)
                driver.get(url)
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                cn = soup.select("p.target-output span")
                cn = cn[0].text.strip()

                Translate_UI.translated_label = cn
                print(cn)
                self.t_browser.clear()
                self.t_browser.append(cn)
                driver.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Translate_UI()
    sys.exit(app.exec_())

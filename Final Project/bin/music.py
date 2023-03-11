# 音乐
import json
import os
import sys
import time
import random
from pygame import mixer
from bs4 import BeautifulSoup
from selenium import webdriver
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot


class Music_UI(QWidget):

    def __init__(self):
        super().__init__()
        self.song_formats = ['.mp3', '.m4a', '.flac', '.wav', '.ogg']
        self.like_song = []
        self.playing = True
        with open("../resource/json/like_music.json", encoding="utf-8") as fp:
            data = fp.read()
            if data:
                with open("../resource/json/like_music.json", encoding="utf-8") as fp:
                    self.like_song = json.load(fp)

            else:
                print("empty")
                self.like_song = []

        self.initUI()  # 界面绘制交给InitUi方法

    def initUI(self):
        self.music_name_label = QLabel(' 输入音乐 ')
        self.music_name_label.setStyleSheet("color:rgb(0,0,0,255);font-size:20px;font-weight:bold;")
        self.music_nameEdit = QTextEdit("")
        self.music_nameEdit.setFixedSize(290, 30)
        self.music_nameEdit.setPlaceholderText('请输入音乐名称')
        self.music_nameEdit.setStyleSheet("color:rgb(0,0,0,255);font-size:15px;font-weight:bold;")
        self.comment_label = QLabel(' 热爱音乐 ')
        self.comment_label.setStyleSheet("color:rgb(255,255,255,255);font-size:20px;font-weight:bold;")
        self.comment_browser = QTextBrowser()
        self.comment_browser.setFixedSize(290, 400)
        self.comment_browser.setStyleSheet("color:rgb(0,0,0,255);font-size:15px;font-weight:bold;")

        self.cmb = QComboBox()
        self.cmb.setStyle(QStyleFactory.create('Fusion'))
        self.cmb.addItem('顺序播放')
        self.cmb.addItem('单曲循环')
        self.cmb.addItem('随机播放')
        self.cmb.setFixedSize(120, 30)
        self.cmb.setStyleSheet("color:rgb(0,0,0,255);font-size:18px;font-weight:bold;")

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.music_name_label, 1, 0)
        grid.addWidget(self.music_nameEdit, 1, 1)
        grid.addWidget(self.cmb, 2, 0)
        grid.addWidget(self.comment_browser, 2, 1)
        self.setLayout(grid)

        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        self.background_init()
        self.botton_init()
        self.resize(440, 900)
        self.setMinimumSize(440, 900)
        self.setMaximumSize(440, 900)
        self.center()
        self.setWindowTitle('华为音乐')  # 设置窗口的标题
        self.setWindowIcon(QIcon('../resource/pic/music.jpg'))
        self.show()

    def center(self):
        qr = self.frameGeometry()  # 获得窗口
        cp = QDesktopWidget().availableGeometry().center()  # 获得屏幕中心点
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def background_init(self):
        self.setWindowTitle("设置背景图片")
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("../resource/pic/ipad-music-app.png")))
        self.setPalette(window_pale)

    def botton_init(self):
        botton_play = QPushButton('播放音乐', self)
        botton_play.resize(100, 35)
        botton_play.setStyleSheet(
            "background-color:rgb(255,255,255);color:rgb(0,0,0,255);font-size:20px;font-weight:bold;")
        botton_play.move(40, 240)
        botton_play.clicked.connect(self.click_play)

        botton_commment = QPushButton('查看热评', self)
        botton_commment.resize(100, 35)
        botton_commment.setStyleSheet(
            "background-color:rgb(255,255,255);color:rgb(0,0,0,255);font-size:20px;font-weight:bold;")
        botton_commment.move(170, 240)
        botton_commment.clicked.connect(self.click_comment)

        botton_like = QPushButton('喜欢/取消', self)
        botton_like.resize(100, 35)
        botton_like.setStyleSheet(
            "background-color:rgb(255,255,255);color:rgb(0,0,0,255);font-size:20px;font-weight:bold;")
        botton_like.move(300, 240)
        botton_like.clicked.connect(self.click_like)

        botton_newsong = QPushButton('新歌飙升', self)
        botton_newsong.resize(100, 35)
        botton_newsong.setStyleSheet(
            "background-color:rgb(255,255,255);color:rgb(0,0,0,255);font-size:20px;font-weight:bold;")
        botton_newsong.move(40, 290)
        botton_newsong.clicked.connect(self.click_newsong)

        botton_hitsong = QPushButton('热歌排行', self)
        botton_hitsong.resize(100, 35)
        botton_hitsong.setStyleSheet(
            "background-color:rgb(255,255,255);color:rgb(0,0,0,255);font-size:20px;font-weight:bold;")
        botton_hitsong.move(170, 290)  # 移动窗口的位置
        botton_hitsong.clicked.connect(self.click_hitsong)

        botton_showlike = QPushButton('我的喜欢', self)
        botton_showlike.resize(100, 35)
        botton_showlike.setStyleSheet(
            "background-color:rgb(255,255,255);color:rgb(0,0,0,255);font-size:20px;font-weight:bold;")
        botton_showlike.move(300, 290)
        botton_showlike.clicked.connect(self.click_showlike)

        botton_preview = QPushButton('◁', self)
        botton_preview.resize(35, 35)
        botton_preview.setStyleSheet(
            "background-color:rgb(255,255,255);color:rgb(0,0,0,255);font-size:20px;font-weight:bold;")
        botton_preview.move(40, 770)
        botton_preview.clicked.connect(self.click_preview)

        botton_pause = QPushButton('暂停/播放', self)
        botton_pause.resize(110, 35)
        botton_pause.setStyleSheet(
            "background-color:rgb(255,255,255);color:rgb(0,0,0,255);font-size:20px;font-weight:bold;")
        botton_pause.move(100, 770)
        botton_pause.clicked.connect(self.click_pause)

        botton_rewind = QPushButton('重新播放', self)
        botton_rewind.resize(110, 35)
        botton_rewind.setStyleSheet(
            "background-color:rgb(255,255,255);color:rgb(0,0,0,255);font-size:20px;font-weight:bold;")
        botton_rewind.move(230, 770)
        botton_rewind.clicked.connect(self.click_rewind)

        botton_next = QPushButton('▷', self)
        botton_next.resize(35, 35)
        botton_next.setStyleSheet(
            "background-color:rgb(255,255,255);color:rgb(0,0,0,255);font-size:20px;font-weight:bold;")
        botton_next.move(365, 770)
        botton_next.clicked.connect(self.click_next)

        botton_up = QPushButton('△', self)
        botton_up.resize(35, 35)
        botton_up.setStyleSheet(
            "background-color:rgb(255,255,255);color:rgb(0,0,0,255);font-size:20px;font-weight:bold;")
        botton_up.move(40, 650)
        botton_up.clicked.connect(self.click_up)

        botton_down = QPushButton('▽', self)
        botton_down.resize(35, 35)
        botton_down.setStyleSheet(
            "background-color:rgb(255,255,255);color:rgb(0,0,0,255);font-size:20px;font-weight:bold;")
        botton_down.move(40, 700)
        botton_down.clicked.connect(self.click_down)

    @pyqtSlot()
    def click_play(self):
        self.music_name = self.music_nameEdit.toPlainText().strip()
        if self.music_name:
            self.search_music()
        else:
            pass

    def search_music(self):
        print("播放音乐")
        for idx in range(len(self.song_formats)):
            file_name = "../resource/music/" + self.music_name + self.song_formats[idx]
            if os.path.exists(file_name):
                self.now_song = self.music_name
                break
        else:
            print("找不到该音乐")
            self.comment_browser.clear()
            self.comment_browser.append("找不到该音乐")

        if os.path.exists(file_name):
            mixer.init()
            mixer.music.load(file_name)
            mixer.music.play()

    @pyqtSlot()
    def click_comment(self):
        if self.now_song:
            self.music_name = self.now_song
            self.search_comment()
        elif self.music_nameEdit.toPlainText().strip():
            self.music_name = self.music_nameEdit.toPlainText().strip()
            self.search_comment()
        else:
            pass

    def search_comment(self):
        print("查看热评")
        url = "http://www.kuwo.cn/search/list?key=" + self.music_name
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        driver = webdriver.Chrome(options=option)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        id = soup.select("div.song_name.flex_c a")
        id = id[0]["href"]
        for i in range(len(id)):
            if id[i].isdigit():
                id = id[i:]
                break

        song_url = "http://www.kuwo.cn/play_detail/" + id
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        driver = webdriver.Chrome(options=option)
        driver.get(song_url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        all_comment = soup.select("section.all-comment")
        fc = all_comment[0]
        comment = fc.select("div.each-comment-content.text-selection")
        comment_str = ""
        for i in range(len(comment)):
            comment[i] = comment[i].text.strip()
            comment_str = comment_str + str(i + 1) + ": " + comment[i] + "\n" * 2
        print(comment_str)
        self.comment_browser.clear()
        self.comment_browser.append(comment_str)

    @pyqtSlot()
    def click_newsong(self):
        self.search_newsong()

    def search_newsong(self):
        newsong_url = "http://www.kuwo.cn/rankList"

        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        driver = webdriver.Chrome(options=option)
        driver.get(newsong_url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        song_names = soup.select("div.song_name.flex_c>a.name")
        new_songs = ""
        for idx in range(len(song_names)):
            song_names[idx] = song_names[idx].text.strip()
            new_songs += (str(idx + 1) + ": " + song_names[idx] + "\n")
        print(new_songs)
        self.comment_browser.clear()
        self.comment_browser.append(new_songs)

    @pyqtSlot()
    def click_hitsong(self):
        self.search_hitsong()

    def search_hitsong(self):
        hitsong_url = "https://y.qq.com/n/ryqq/toplist/26"

        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        driver = webdriver.Chrome(options=option)
        driver.get(hitsong_url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        song_names = soup.select("span.songlist__songname_txt>a")[1::2]
        hit_songs = ""
        for idx in range(len(song_names)):
            song_names[idx] = song_names[idx].text.strip()
            hit_songs += (str(idx + 1) + ": " + song_names[idx] + " " + "\n")
        print(hit_songs)
        self.comment_browser.clear()
        self.comment_browser.append(hit_songs)

    @pyqtSlot()
    def click_pause(self):
        self.pause_play()

    def pause_play(self):
        if self.now_song:
            if self.playing:
                print("暂停播放")
                self.playing = False
                mixer.music.pause()
            else:
                print("继续播放")
                self.playing = True
                mixer.music.unpause()
        else:
            print("6")
            pass

    @pyqtSlot()
    def click_like(self):
        if self.now_song:
            if self.now_song not in self.like_song:
                self.like_song.append(self.now_song)
            else:

                self.like_song.remove(self.now_song)
            with open("../resource/json/like_music.json", "w", encoding="utf-8") as fp:
                json.dump(self.like_song, fp)
        else:
            pass

    def click_showlike(self):
        likesongs = ""
        for idx in range(len(self.like_song)):
            likesongs += str(idx + 1) + ". " + self.like_song[idx] + "\n"
        print(likesongs)
        self.comment_browser.clear()
        self.comment_browser.append(likesongs)

    def click_rewind(self):
        if self.now_song:
            print("重新播放")
            mixer.music.rewind()
        else:
            pass

    def click_up(self):
        if self.now_song:
            print("调大音量")
            mixer.music.set_volume(mixer.music.get_volume() + 0.1)
        else:
            pass

    def click_down(self):
        if self.now_song:
            print("调小音量")
            mixer.music.set_volume(mixer.music.get_volume() - 0.1)
        else:
            pass

    def click_preview(self):
        if self.now_song in self.like_song:
            # 顺序播放和单曲循环都是按列表顺序
            if self.cmb.currentIndex() == 0 or self.cmb.currentIndex() == 1:
                song_idx = list(self.like_song).index(self.now_song) - 1
                if song_idx == -1:
                    song_idx = len(self.like_song) - 1
                print(song_idx)
                for format_idx in range(len(self.song_formats)):
                    file_name = "../resource/music/" + self.like_song[song_idx] + self.song_formats[format_idx]
                    if os.path.exists(file_name):
                        self.now_song = self.like_song[song_idx]
                        mixer.music.load(file_name)
                        if self.cmb.currentIndex() == 0:
                            mixer.music.play()
                            break
                        if self.cmb.currentIndex() == 1:
                            mixer.music.play(-1,0)
                            break

            # 随机播放是随机的
            elif self.cmb.currentIndex() == 2:
                song_idx = random.randint(0, len(self.like_song) - 1)
                # 生成的随机数等于原本的数就+1 相当于播放下一首
                if song_idx == list(self.like_song).index(self.now_song):
                    song_idx -= 1
                    if song_idx == -1:
                        song_idx = len(self.like_song) - 1
                print(song_idx)
                for format_idx in range(len(self.song_formats)):
                    file_name = "../resource/music/" + self.like_song[song_idx] + self.song_formats[format_idx]
                    if os.path.exists(file_name):
                        self.now_song = self.like_song[song_idx]
                        mixer.music.load(file_name)
                        mixer.music.play()
                        break
        # 歌未在我的喜欢里，自动播放歌单第一首
        else:
            for format_idx in range(len(self.song_formats)):
                file_name = "../resource/music/" + self.like_song[0] + self.song_formats[format_idx]
                if os.path.exists(file_name):
                    self.now_song = self.like_song[0]
                    mixer.music.load(file_name)
                    mixer.music.play()
                    break

    def click_next(self):
        if self.now_song in self.like_song:
            # 顺序播放和单曲循环的下一首都是按列表顺序
            if self.cmb.currentIndex() == 0 or self.cmb.currentIndex() == 1:
                song_idx = list(self.like_song).index(self.now_song) + 1
                if song_idx == len(self.like_song):
                    song_idx = 0
                print(song_idx)
                for format_idx in range(len(self.song_formats)):
                    file_name = "../resource/music/" + self.like_song[song_idx] + self.song_formats[format_idx]
                    if os.path.exists(file_name):
                        self.now_song = self.like_song[song_idx]
                        mixer.music.load(file_name)
                        if self.cmb.currentIndex() == 0:
                            mixer.music.play()
                            break
                        if self.cmb.currentIndex() == 1:
                            mixer.music.play(-1, 0)
                            break
            # 随机播放是随机的
            elif self.cmb.currentIndex() == 2:
                song_idx = random.randint(0,len(self.like_song)-1)
                # 生成的随机数等于原本的数就+1 相当于播放下一首
                if song_idx == list(self.like_song).index(self.now_song):
                    song_idx += 1
                    if song_idx == len(self.like_song):
                        song_idx = 0
                print(song_idx)
                for format_idx in range(len(self.song_formats)):
                    file_name = "../resource/music/" + self.like_song[song_idx] + self.song_formats[format_idx]
                    if os.path.exists(file_name):
                        self.now_song = self.like_song[song_idx]
                        mixer.music.load(file_name)
                        mixer.music.play()
                        break

        else:
            for format_idx in range(len(self.song_formats)):
                file_name = "../resource/music/" + self.like_song[0] + self.song_formats[format_idx]
                if os.path.exists(file_name):
                    self.now_song = self.like_song[0]
                    mixer.music.load(file_name)
                    mixer.music.play()
                    break


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Music_UI()
    sys.exit(app.exec_())

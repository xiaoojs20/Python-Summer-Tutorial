import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot
from bs4 import BeautifulSoup
from selenium import webdriver

# div.movie-brief-container
url = "https://search.douban.com/movie/subject_search?search_text=" + "失控玩家" +"&cat=1002"
option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(options=option)
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')
movie_info = soup.select("div.rating.sc-bwzfXH.hxNRHc")
# movie_id = movie_id[0]["href"]
print(movie_info)

# for idx in range(len(hit_movie_name)):
#     hit_movie_name[idx] = hit_movie_name[idx]["title"].strip()
#     hit_movie_name_str += (hit_movie_name[idx] + "\n")
# print(hit_movie_name_str)

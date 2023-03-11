# 天气预报

from bs4 import BeautifulSoup
from selenium import webdriver
from time import time

place = input("查询地方空气质量")
url = "https://weathernew.pae.baidu.com/weathernew/pc?query=" + place + "天气" + "&srcid=4982&city_name=" + place + "&province_name=" + place

driver = webdriver.Chrome()     # 打开 Chrome 浏览器
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')

pm25 = soup.select("span.weather-15day-pm25")
for i in range(len(pm25)):
    pm25[i] = pm25[i].text.strip()
week = soup.select("span.week")
for i in range(len(week)):
    week[i] = week[i].text.strip()
week = week[0:8]
dic = {}
for i in range(len(week)):
    dic[week[i]] = pm25[i]
print(dic)
driver.close()


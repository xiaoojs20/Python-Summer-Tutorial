from bs4 import BeautifulSoup
from selenium import webdriver
from time import time

mode = input("请输入模式：1-中译英，2-英译中")

if mode == '1':
    cn = input("请输入要翻译的中文")
    url = "https://fanyi.baidu.com/#zh/en/" + cn

    driver = webdriver.Chrome()
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    en = soup.select("p.target-output span")
    en = en[0].text.strip()
    print(en)
    driver.close()

elif mode == '2':
    en = input("请输入要翻译的英语")
    en = en.strip()
    en = en.replace(" ","%20")
    url = "https://fanyi.baidu.com/#en/zh/" + en
    driver = webdriver.Chrome()
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    cn = soup.select("p.target-output span")
    cn = cn[0].text.strip()
    print(cn)
    driver.close()

else:
    print("请输入正确数字")
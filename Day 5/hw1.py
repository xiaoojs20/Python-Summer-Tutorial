# 从豆瓣获取指定电影人信息（比如：张国立）

from bs4 import BeautifulSoup
import requests, time
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'}

while True:
    print("演员信息搜索引擎")
    botton = input("1-开始搜索 0-退出搜索")

    if botton == '1':
        name = input("请输入要查找的电影人")
        web = "https://movie.douban.com/celebrities/search?search_text=" + name

        response = requests.get(web, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        # div.sc-bxivhb jDZFxE
        grid_view = soup.select("div.content a")
        actor_web = grid_view[0]["href"]
        # print(actor_web)

        time.sleep(0.5)

        # 爬取演员个人信息
        response = requests.get(actor_web, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        actor_info_key = soup.select("div.info span")
        actor_info_key = actor_info_key[0:6]
        for i in range(6):
            actor_info_key[i] = actor_info_key[i].text

        value = soup.select("div.info li")
        value = value[0:6]
        actor_info_value = []
        for i in range(6):
            value[i] = value[i].text.strip()
            for j in range(len(value[i])):
                if value[i][j] == '\n':
                    tmp = value[i][j:len(value[i])].strip()
                    actor_info_value.append(tmp)
                else:
                    continue

        info_dic = {}

        for i in range(len(actor_info_value)):
            info_dic[actor_info_key[i]] = actor_info_value[i]

        pic = soup.select("div.nbg img")
        pic = pic[0].get("src")
        info_dic["头像"] = pic

        print(info_dic)
    elif botton == '0':
        break

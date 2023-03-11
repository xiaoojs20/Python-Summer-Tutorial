from bs4 import BeautifulSoup
import requests, time, json
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'}
All = []
url = "https://movie.douban.com/top250"

while True:
    print(url)
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    grid_view = soup.select("ol.grid_view>li")
    # print(grid_view)

    # 遍历一个页面里二十五个电影
    for idx in range(25):
        m2 = grid_view[idx]
        # print(m2)

        # 1、电影名称
        span_title = m2.select("span.title")
        title = span_title[0].text.strip()

        # 2、电影网址
        span_web = m2.select("div.hd a")
        web = span_web[0]['href']
        # print(span_web[0].text.strip())

        # 3、电影评分
        span_num = m2.select("span.rating_num")
        score = span_num[0].text.strip()

        # 4、点评人数
        span_people = m2.select("div.star span")
        people = span_people[3].text.strip()

        # 5、电影简介
        intro = m2.select("span.inq")
        if len(intro) > 0:
            intro = intro[0].text.strip()
        else:
            intro = "null"

        span_info = m2.select("div.bd p")
        str_info = span_info[0].text.strip()
        daoyan = ""
        begin = False

        now_pos = 0
        for i in range(len(str_info)):
            if str_info[i]==':':
                begin = True
            if str_info[i] == '主':
                break
            if begin == True:
                daoyan += str_info[i]
        daoyan = daoyan[2:].strip()

        # 找年份
        year = ""
        for i in range(len(str_info)):
            if str_info[i] in "0123456789":
                year = str_info[i:i+4]
                now_pos = i + 6
                break
        # 找国别
        begin = True
        country = ""
        for i in range(now_pos,len(str_info)):
            if str_info[i+1] == '/':
                begin = False
                now_pos = i + 1
                break
            if begin:
                country += str_info[i]
        country = country.strip()

        # 找类型
        begin = True
        movie_type = ""
        for i in range(now_pos + 2,len(str_info)):
            if begin:
                movie_type += str_info[i]
        movie_type = movie_type.strip()

        # 1个字典（包括标题、导演s、年份、评分、人数、类型s、国别s、网址、简介)

        dic = {"标题":title,"导演":daoyan,"年份":year,"评分":score,"人数":people,"类型": movie_type ,"国别":country,"网址":web,"简介":intro}
        print(dic)
        All.append(dic)

    next = soup.select("span.next link")
    time.sleep(1)
    if len(next) > 0:
        url = 'https://movie.douban.com/top250'+next[0]['href']
    else:
        break

for movie in All:
    print(movie)

    # 所有爬取结果以json文件的形式存储在硬盘中
    with open("movies.json", 'w') as fp:
        json.dump(All, fp)

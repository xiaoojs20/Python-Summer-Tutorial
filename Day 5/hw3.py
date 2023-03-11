# 从豆瓣获取某电影人与其他电影人的合作关系图

import requests
import time
from bs4 import BeautifulSoup
from draw_graph import draw_graph


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84'}
global actor_tuple, movie_list

def search_person_by_name(name):
    web = "https://movie.douban.com/celebrities/search?search_text=" + name

    response = requests.get(web, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    grid_view = soup.select("div.content a")
    actor_web = grid_view[0]["href"]
    global id, actor_tuple
    for i in range(len(actor_web)):
        if actor_web[i] in "0123456789":
            id = actor_web[i:-1]
            break
    actor_tuple = (name, id, web) # 演员元组
    # print(actor_tuple)
    return

def search_movie_by_person(tuple): # 遍历 + 翻页
    global movie_list,title_list,movie_id_list

    movie_web = "https://movie.douban.com/celebrity/" + tuple[1] + "/movies"

    while True:
        response = requests.get(movie_web, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        grid_view = soup.select("div.grid_view>ul>li")

        for idx in range(len(grid_view)):
            m = grid_view[idx]
            # print(m)

            span_title = m.select("h6")
            title = span_title[0].text.strip()  # 电影名称

            span_id = m.select("h6 a")
            movie_id = span_id[0]['href']# 查询电影id

            for i in range(len(title)):
                if title[i] == '(' or i == "（":
                    title = title[0:i].strip()
                    title_list.append(title)
                    break
            for i in range(len(movie_id)):
                if movie_id[i].isdigit():
                    movie_id = movie_id[i:-1]
                    movie_id_list.append(movie_id)
                    break
            movie_web = "https://movie.douban.com/subject/" + movie_id + "/"
            movie_dic = {"电影名称": title, "id": movie_id, "网址":movie_web}
            movie_list.append(movie_dic)

        time.sleep(1)

        next = soup.select("span.next link")
        if len(next) > 0:
            movie_web = "https://movie.douban.com/celebrity/" + tuple[1] + "/movies" + next[0]['href']
        else:
            break

        print(movie_web)
    # print(movie_list)
    # print(len(movie_list))
    return

def search_persons_by_movie(movie_dic):
    global partner, num_dict
    a_movie_web = "https://movie.douban.com/subject/" + movie_dic["id"] + "/celebrities"
    response = requests.get(a_movie_web, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    info = soup.select("div.article div.list-wrapper")
    if len(info) > 1:
        actors_info = info[1]
        actors_info = actors_info.select("span.name")

        for i in range(len(actors_info)):
            actors_info[i] = actors_info[i].text.strip()
            actors_info[i] = actors_info[i].split(" ")[0]
        # 删除空字符串
        for ele in actors_info[::-1]:
            if ele.isspace() or len(ele) == 0:
                actors_info.remove(ele)
        print(actors_info)

        for i in range(len(actors_info)):
            if actors_info[i] != actor_tuple[0]:
                # 把演员合作信息写进partner列表
                if len(partner) == 0:
                    tmp = [actor_tuple[0], actors_info[i], 1]
                    partner.append(tmp)
                    continue
                else:
                    pass

                for idx in range(len(partner)):
                    if actors_info[i] == partner[idx][1]:
                        partner[idx][2] += 1
                        break
                else:
                    tmp = [actor_tuple[0], actors_info[i], 1]
                    partner.append(tmp)
        num_dict[partner[0][0]] = len(movie_list)
        for idx in range(len(partner)):
            num_dict[partner[idx][1]] = partner[idx][2]

        # print(partner)    # 输出：演员元组列表
        # print(num_dict)
    else:
        print("没有导演")
        movie_list.remove(movie_dic)
        return

global movie_list, title_list, movie_id_list
movie_list = []
title_list = []
movie_id_list = []
global partner, num_dict
partner = []
num_dict = {}

while True:
    print("演员合作关系图")
    botton = input("1-开始搜索 0-退出搜索")

    if botton == '1':
        name = input("请输入要查找的电影人")
        search_person_by_name(name)
        # # 进入出演的电影网站
        search_movie_by_person(actor_tuple)
        # 寻找电影的参演演员
        # search_persons_by_movie(movie_list[2])

        for dic in movie_list:
            time.sleep(1)
            search_persons_by_movie(dic)

        print(partner)    # 输出：演员元组列表
        print(num_dict)
        draw_graph(partner, num_dict, "姜文轩", tp='spring', max_node=50)
        break

    elif botton == '0':
        break


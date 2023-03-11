# from urllib.request import urlopen
#
# # if has Chinese, apply decode()
# html = urlopen(
#     "https://mofanpy.com/static/scraping/basic-structure.html"
# ).read().decode('utf-8')
# print(html)


# import requests
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'}
# url = "https://www.baidu.com/"
# try:
#
#     response = requests.get(url, headers=headers)
#     # 返回网页文本（字符串）
#     # print(f"网页文本: {response.text}")
#     # print(f"返回网页文本的字节串： {response.content}")
#     # print(f"响应状态码:{response.status_code}")
#     # print(f"响应头： {response.headers}")
#     # print(f"请求头： {response.request.headers}")
#     # 如果状态不是200，引发HTTPError异常
#     # response.raise_for_status()
#     # ss = response.content.decode()
#     # print(ss)
#     with open("baidu.html","w",encoding='utf-8') as f:
#         f.write(response.text)
#
# except Exception as e:
#     print("爬取失败", e)



# print(soup,type(soup))

# a_list = soup.select("a")
# for a in a_list:
#     print(a)
# print(len(a_list),type(a_list))



# id_list = soup.select("#db-global-nav")
# print(len(id_list))
# print(id_list)


# list_1_a = soup.select("div.nav-secondary a")
# for i in list_1_a:
#     print(i.text)
# print(len(list_1_a))


# .grid_view .info>. .hd .title
# list_title = soup.select(".hd .title")
#
# for li in list_title:
#     print(li.text)
# print(len(list_title))
# list_title[2]

# for i in range((len(list_title))):
#     if '/' in list_title[i]:
#         list_title.remove(list_title[i])
# print(list_title)
#
# from selenium import webdriver
# c=webdriver.Chrome(executable_path=r'./chromedriver.exe') #获取chrome浏览器的驱动，并启动Chrome浏览器
# c.get('https://www.baidu.com')#打开百度

# #coding = utf-8
# from selenium import webdriver
# import time
# browser = webdriver.Chrome() #谷歌
#
# browser.get("http://www.baidu.com")
# browser.find_element_by_id("kw").send_keys("豆瓣电影")
# #通过id = kw定位百度输入框，通过键盘方法send_keys()向输入框中输入selenium。
# browser.find_element_by_id("su").click()
# #通过id=su定位搜索按钮，并向按钮发送单击事件click()
#
# time.sleep(3)
#
# browser.quit()



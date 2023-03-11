# 从链家获取某区域的二手房信息（比如清华大学）
from time import time
from bs4 import BeautifulSoup
from selenium import webdriver


place = input("请输入房子的位置")
url = "https://bj.lianjia.com/ershoufang/rs" + place + "/"

driver = webdriver.Chrome()     # 打开 Chrome 浏览器
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')

house_name_list = []
house_place_list = []
house_room_list = []
house_type_list = []
house_square_list = []
house_floor_list = []
house_time_list = []
house_info_list = []

house_name = soup.select("div.leftContent>ul.sellListContent")
h = house_name[0]
all_house_name = h.select("div.positionInfo a")
researched_house_name = []
for i in range(len(all_house_name)):
    researched_house_name.append(all_house_name[i].text.strip())

for i in range(len(researched_house_name)):
    if i%2 == 0:
        house_name_list.append(researched_house_name[i])
    else:
        house_place_list.append(researched_house_name[i])

house_info = h.select("div.houseInfo")
for i in range(len(house_info)):
    house_info[i] = house_info[i].text.strip()
    infos = house_info[i].split('|')
    house_room_list.append(infos[0].strip())
    house_square_list.append(infos[1].strip())
    house_floor_list.append(infos[4].strip())
    house_time_list.append(infos[5].strip())
    house_type_list.append(infos[6].strip())

price = h.select("div.unitPrice span")
for i in range(len(price)):
    price[i] = price[i].text.strip()

tprice = h.select("div.totalPrice span")
for i in range(len(tprice)):
    tprice[i] = tprice[i].text.strip()
for i in range(len(house_name_list)):
    dic = {"小区名称":house_name_list[i],"户型":house_room_list[i],"面积":house_square_list[i],"总价":tprice[i]+'万', "单价":price[i] ,
           "楼层位置":house_floor_list[i], "建筑时间":house_time_list[i],"建筑类型":house_type_list[i],"发布时间":house_time_list[i]}
    house_info_list.append(dic)

avg = 0
for i in range(len(house_info_list)):
    print(house_info_list[i])
    tmp = float(tprice[i])
    avg += tmp
avg /= len(house_info_list)
print(f'{place}附近二手房平均总价为{avg}万元')


driver.close()
driver.quit()





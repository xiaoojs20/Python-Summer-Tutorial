# 编写1个程序，实现老王和tesla的交易行动，tesla价格为45万。相关信息均存为json文件。需求如下：
# a)	目录结构为
# .
# ├── account
# │   ├── laowang.json
# │   └── tesla_company.json
# └── bin
#       └── start.py

import os, json

# 初始化老王和特斯拉
lw = {"balance":2000000, "tesla":5}
tc = {"price":200000, "amount":200,"income":99999999}
global laowang, tesla_company
laowang = {}
tesla_company = {}
if not os.path.exists("../account/laowang.json"):
    laowang = lw
    with open("../account/laowang.json", 'w') as fp:
        json.dump(lw, fp)
else:
    with open("../account/laowang.json") as fp:
        laowang = json.load(fp)

if not os.path.exists("../account/tesla_company.json"):
    tesla_company = tc
    with open("../account/tesla_company.json", 'w') as fp:
        json.dump(tc, fp)
else:
    with open("../account/tesla_company.json") as fp:
        tesla_company = json.load(fp)


def renew_laowang(func):
    def inner(*args, **kwargs):
        with open("../account/laowang.json") as fp:
            global laowang
            laowang = json.load(fp)
        print("最新资料显示:")
        ret = func(*args, **kwargs)
        return ret
    return inner


def renew_tesla_company(func):
    def inner(*args, **kwargs):
        with open("../account/tesla_company.json") as fp:
            global tesla_company
            tesla_company = json.load(fp)
        print("最新资料显示:")
        ret = func(*args, **kwargs)
        return ret

    return inner

# 交互开始
print(" ———- ICBC Bank ————-")
while True:
    botton = input("请输入: 1-账户信息 2-公司信息 3-购买汽车 4-退出")
    # 选择1 账户信息 显示老王的当前账户余额，拥有的Tesla数量，使用装饰器，显示最新的账户信息。
    if botton == '1':
        @renew_laowang
        def check_laowang():
            print(f'老王,你的账户余额为{laowang["balance"]},拥有的特斯拉数量为{laowang["tesla"]}')
        check_laowang()

    # 选择2 公司信息 显示Tesla公司的单价，剩余数量，总收入，使用装饰器，显示最新的账户信息。
    elif botton == '2':
        @renew_tesla_company
        def check_tesla_company():
            print(f'特斯拉公司,你的单价为{tesla_company["price"]},剩余数量为{tesla_company["amount"]},总收入为{tesla_company["income"]}')


        check_tesla_company()


    # 选择3 购买，输入拟购买的汽车数量，判断剩余数量是否够，判断用户余额是否够，
    # 如果够，则 老王和Tesla公司的汽车数量、账户余额等信息发生变化，使用装饰器，在购买前获取最新的文件信息，在购买后，将最新信息更新到文件。
    elif botton == '3':
        number = input("请输入你要买几辆特斯拉汽车")
        number = int(number)
        if number > tesla_company["amount"]:
            print("特斯拉公司剩余汽车数量不足")
        if number*tesla_company["price"] > laowang["balance"]:
            print("老王,你的余额不足")

        # 具备购买条件
        laowang["balance"] -= number*tesla_company["price"]
        laowang["tesla"] += 1
        tesla_company["amount"] -= 1
        tesla_company["income"] += number*tesla_company["price"]

        with open("../account/laowang.json", 'w') as fp:
            json.dump(laowang, fp)
        with open("../account/tesla_company.json", 'w') as fp:
            json.dump(tesla_company, fp)
    # 选择4,退出程序
    elif botton == '4':
        exit()


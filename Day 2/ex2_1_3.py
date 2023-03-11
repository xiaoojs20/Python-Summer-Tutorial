# 作业：购物车
goods = []
users = []
buy_goods = {"电脑": 0, "鼠标": 0, "书籍": 0, "空调": 0}
user=0
with open("goods.txt",'r',encoding='utf-8') as f:
    lns=f.readlines()
    for ln in lns:
        vs=ln.split(" ")
        tmp=int(vs[1])
        goods.append({"name":vs[0],"price":tmp})
    # print(goods)

with open("users.txt",'r',encoding='utf-8') as f:
    lns=f.readlines()
    for ln in lns:
        vs=ln.split(" ")
        tmp=float(vs[3])
        users.append({"name":vs[0],"password":vs[1],"age":vs[2],"balance":tmp})
    # print(users)

#  2、输入用户名密码后，检查用户密码是否正确，不正确重复登录，3次失败，则退出程序。
for i in range(3):
    user_name = input("please input your name\n")
    pass_word = input("please input your password!\n")
    if user_name=="zhangsan" and pass_word=="zhangsan":
        print("zhangsan, start successfully!")
        user=0
        break
    elif user_name=="lisi" and pass_word=="lisi":
        print("lisi, start successfully!")
        user=1
        break
    elif user_name=="wangwu" and pass_word=="wangwu":
        print("wangwu, start successfully!")
        user=2
        break
    else:
        print("your password is unmatched!")

else:
    print("you are failed to login")
    exit()

#  3、用户密码核实后，支持用户选择以下操作代码：（查看商品 (g)、查看余额 (u)、购买商品(b)）

while True:
    key = input("按g查看商品、按u查看余额、按b购买商品、按z退出程序\n").strip()
    # 3.1、输入g，则查看所有商品信息。
    if key =='g' or key =='G':
        for i in range(len(goods)):
            print(f'{goods[i]["name"]}价格为RMB {goods[i]["price"]}')
    # 3.2、输入u，则查看用户余额信息。
    if key =='u' or key=='U':
        print(f'{users[user]["name"]},your balance is {users[user]["balance"]}')

    # 3.3、输入b，则进入购买买流程：
    # 3.3.1、允许用户根据商品编号购买商品。
    # 3.3.2、用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒。
    sum_price=0
    if key=='b' or key=='B':
        while True:
            sth=input("please input something your want to buy\ndn-电脑 sb-鼠标 sj-书籍 kt-空调 z-退出购买\n")
            if sth=='z':
                break
            num_sth = input("How many do you want to buy?\n")
            if sth=='dn':

                if users[user]["balance"]>=1999*int(num_sth):
                    users[user]["balance"]-=1999*int(num_sth)
                    sum_price += 1999 * int(num_sth)
                    buy_goods["电脑"]+=int(num_sth)
                else:
                    print("sorry, your balance is insufficient!")
            elif sth=='sb':

                if users[user]["balance"]>=10*int(num_sth):
                    users[user]["balance"]-=10*int(num_sth)
                    sum_price += 10 * int(num_sth)
                    buy_goods["鼠标"] += int(num_sth)
                else:
                    print("sorry, your balance is insufficient!")
            elif sth=='sj':

                if users[user]["balance"]>=50*int(num_sth):
                    users[user]["balance"]-=50*int(num_sth)
                    sum_price += 50 * int(num_sth)
                    buy_goods["书籍"] += int(num_sth)
                else:
                    print("sorry, your balance is insufficient!")

            elif sth=='kt':

                if users[user]["balance"]>=2000*int(num_sth):
                    users[user]["balance"]-=2000*int(num_sth)
                    sum_price += 2000 * int(num_sth)
                    buy_goods["空调"] += int(num_sth)
                else:
                    print("sorry, your balance is insufficient!")

    #  4、可随时退出，退出时，打印已购买商品和余额，并更新文件信息。
    if key=='z'or key=='Z':
        print(buy_goods)
        for key in buy_goods.keys():
            if buy_goods[key]>0:
                print(f'{key}买了{buy_goods[key]}件')
        print(f'{users[user]["name"]},余额为{users[user]["balance"]}')
        # print(goods)

        with open("users.txt", 'w', encoding='utf-8') as f:
            for i in range(len(users)):
                for key in users[i].keys():
                    f.write(str(users[i][key]))
                    f.write(" ")
                f.write("\n")
            # print(users)
        exit()
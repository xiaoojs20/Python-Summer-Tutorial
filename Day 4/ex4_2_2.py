# 课堂练习：用户登录认证程序：
# 从json文件里读用户和密码（以及其他信息）信息。
# 文件 -> json -> 内存dict
# 需要考虑异常判断，如果json文件不存在怎么办？ 自己定义一个dict， dict -> json -> file， 再去读文件。
import os,json
_users = [{"name": "zhangsan", "password": "zhangsan","lock":False},
         {"name": "lisi", "password": "lisi","lock":False},
         {"name": "wangwu", "password": "wangwu","lock":False}]
users = []

def read_file():
    if not os.path.exists("info.json"):
        print("error")
        with open('info.json', 'w') as fp:
            json.dump(_users, fp)

    with open("info.json") as f:
        data = json.load(f)
        global users
        users = data
def input_name():
    global now_i
    name = input("请输入用户名")
    name = str(name).strip()
    now_i = 0

    for i in range(len(users)):
        if name == users[i]["name"]:
            now_i = i
            break
    else:
        print("该用户没有注册")
        exit()

def input_password():
    global input_pwd
    if input_pwd == 3:
        users[now_i]["lock"] = True
        with open('info.json', 'w') as fp:
            json.dump(users, fp)

    if users[now_i]["lock"]:
        print("用户已经被锁定")
        exit()

    else:
        pwd = input("请输入密码")
        if pwd == users[now_i]["password"]:
            print("登陆成功")
            exit()
        else:
            print("密码错误请重试")
            input_pwd += 1

try:
    read_file()
except Exception as e:
    print(e)

# def unlock():
#     users = _users
#     print(users)

# 输入用户
input_name()
# 输入密码：
global input_pwd
input_pwd = 0
while True:
    input_password()





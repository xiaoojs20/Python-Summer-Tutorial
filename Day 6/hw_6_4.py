# 4.编写程序, 如下有三点要求：
# 	自定义用户信息数据结构， 写入文件, 然后读取出内容, 利用json模块进行数据的序列化和反序列化
# 	定义用户类，定义方法db，例如 执行obj.db可以拿到用户数据结构
# 	在该类中实现登录、退出方法, 登录成功将状态(status)修改为True,
# 退出将状态修改为False(退出要判断是否处于登录状态).密码输入错误三次将设置锁定时间(下次登录如果和当前时间比较大于30秒即不允许登录)

import json
import time


class info_sys:
    status = False
    is_locked = False

    def __init__(self, name, sex, password):
        self.info = {"name": name, "sex": sex, "password": password}
        with open("info.json", "w") as f1:
            json.dump(self.info, f1)

    def db(self):
        with open("info.json") as f2:
            self.get_info = json.load(f2)
        print(self.get_info)

    def login(self):
        this_time = time.time()
        with open("time.json") as fp:
            lock_time = json.load(fp)
        if this_time - lock_time > 30:
            for i in range(3):
                pwd = input("Please input your password: ")
                if pwd == self.get_info["password"]:
                    print("Login successfully")
                    info_sys.status = True
                    break
                else:
                    print("Your password is wrong")
            else:
                lock_time = time.time()
                with open("time.json", "w") as fp:
                    json.dump(lock_time, fp)
        else:
            print("Your account is locked")

    def exit(self):
        if info_sys.status:
            info_sys.status = False
            print("Exit successfully")
        else:
            print("You haven't logged in yet")


p1 = info_sys("zhangsan", "male", "123456")
p1.db()
p1.login()
time.sleep(3)
p1.exit()

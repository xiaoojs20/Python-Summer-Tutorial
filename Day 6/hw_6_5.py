# 5.	定义MySQL类，要求：
# 	对象有id、host、port三个属性
# 	定义工具create_id，在实例化时为每个对象随机生成id，保证id唯一
# 	提供两种实例化方式，方式一：用户传入host和port 方式二：从配置文件中读取host和port进行实例化
# 	为对象定制方法，save和get_obj_by_id，save能自动将对象序列化到文件中，文件路径为配置文件中DB_PATH,文件名为id号，
#   保存之前验证对象是否已经存在，若存在则抛出异常，;get_obj_by_id方法用来从文件中反序列化出对象
import os
import json
import random

HOST = '127.0.0.1'
PORT = 3306


class MySQL:
    def __init__(self, host, port):
        self.id = MySQL.create_id()
        self.host = host
        self.port = port
        self.info = {"id": self.id, "host": self.host, "port": self.port}

    @classmethod
    def from_conf(cls):
        print(cls)
        return cls(HOST, PORT)

    @staticmethod
    def create_id():
        while True:
            tmp = str(random.randint(1, 999999))
            tmp = tmp.zfill(6)
            filename = "DB_PATH/" + tmp + ".json"
            if not os.path.exists(filename):
                return tmp

    def save(self):
        filename = "DB_PATH/" + self.id + ".json"
        with open(filename, "w") as fp:
            json.dump(self.info, fp)
        print("用户已存档")

    def get_obj_by_id(self, id):
        filename = "DB_PATH/" + id + ".json"
        if not os.path.exists(filename):
            raise IOError("找不到此ID")
        else:
            with open(filename) as fp:
                data = json.load(fp)
                print(data)

    def __str__(self):
        return "conn: %s:%s" % (self.host, self.port)


sql1 = MySQL.from_conf()
sql1.save()
sql2 = MySQL('127.0.0.2',3308)
sql2.save()
print(sql1.id)
print(sql1.host)
print(sql1.port)
print(sql2.id)
print(sql2.host)
print(sql2.port)
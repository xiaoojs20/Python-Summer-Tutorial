import os
import random
import hashlib
import time


class MySQL:
    login_status = False
    login_conn_num = 0

    def __init__(self, host, port, schema):
        self.id = MySQL.create_id()
        self.host = host
        self.port = port
        self.schema = schema

    @staticmethod
    def create_id():
        m = hashlib.md5(str(time.time()).encode('utf-8'))
        return m.hexdigest()

    @classmethod
    def create_sql(cls, host, port, schema):
        return cls(host, port, schema)

    def get_id(self):
        return self.id

    def get_host(self):
        return self.host

    def get_port(self):
        return self.host

    def get_schema(self):
        return self.schema

    def login(self):
        if not MySQL.login_status:
            MySQL.login_status = True
            MySQL.login_conn_num += 1
            print("sql 成功登录")
        else:
            print("sql 已经登录")

    def logout(self):
        if MySQL.login_status:
            MySQL.login_conn_num -= 1
        else:
            print("sql 未登录")
        if MySQL.login_conn_num == 0:
            MySQL.login_status = False
            print("sql 退出登录")

    def __del__(self):
        self.logout()


sql = MySQL('127.0.0.1', 3306, "w")
sql.login()
sql.login()
print([sql.get_id(), sql.get_host(), sql.get_port()])
sql.logout()

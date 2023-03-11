# import json
# obj = dict(name='小明', age=20)
# new_obj=json.loads(obj)
# # s = json.dumps(obj, ensure_ascii=True)
# print(new_obj)
import time
period = input("请输入用户有效期(单位:天)")
t0 = time.time()
t1 = t0 + int(period)*24*3600
expire_date = time.strftime("%Y-%m-%d", time.localtime(t1))
print(expire_date)
print(type(expire_date))
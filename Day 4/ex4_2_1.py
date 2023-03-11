import time,datetime

# 1
# while True:
#     # print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#
#     t_time = time.time()
#     local_time = time.localtime(t_time)
#     str_time = time.strftime('%Y-%m-%d %X',local_time)
#
#     time.sleep(1)
#     print(str_time)

# 2
# t1=time.time()
# t2=time.time()+365*24*3600
#
# print(f'1年后的时刻是{time.strftime("%Y-%m-%d %X", time.localtime(t2))}，与现在相比，时间差为{t2-t1}秒')
#
#
# local_time = time.localtime()
# str_time = time.strftime('%Y-%m-%d %X', local_time)
# print(str_time)
# print(time.strftime('%Y-%m-%d %X',time.localtime(time.time()+365*24*3600)))

# 3
# 编写一个函数：
#      （1）生成1个给定长度n的自然数列表li = [1,…,n]
#        （2） 等待1秒。
#        （3）返回1个元组，(函数用时,占用cpu时间,li)

# def timer(n):
#     t1 = time.time()
#     t2 = time.process_time()
#     li=[i for i in range(1,n+1)]
#     time.sleep(1)
#     t3 = time.time()
#     t4 = time.process_time()
#     return (t3-t1,t4-t2,li)
# print(timer(5))


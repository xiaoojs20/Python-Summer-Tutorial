# [1]	编写函数：输入一个列表或元组，输出的奇数位对应的元素，并返回一个新的列表，注意异常处理（如果传入的参数不是列表或元组，则报异常）
# def oddpos(list):
#     odd = []
#     if type(list) not in [type([]), type(())]:
#         print("error")
#         raise TypeError("传入的参数不是列表或元组")
#     for i in range(len(list)):
#         if i % 2 != 0:
#             odd.append(list[i])
#     print(odd)
#     return odd
#
#
# try:
#     oddpos([0, 1, 2, 3, 4, 5])
#     oddpos(0)
# except Exception as e:
#     print(e)
# else:
#     print("无异常")

# [2]	编写函数：检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空格。若有，返回true，否则返回false，
#       注意异常处理（如果传入的参数不是字符串、列表或元组，则报异常）
# def has_space(obj):
#     if type(obj) not in [type([]), type(()),type("str")]:
#         print("error")
#         raise TypeError("传入的参数不是字符串、列表或元组")
#     for i in range(len(obj)):
#         if str(obj[i]).isspace():
#             return True
#     else:
#         return False
#
#
# try:
#     print(has_space([1," ",2]))
# except Exception as e:
#     print(e)
# else:
#     print("no error")

# [3]	编写函数：输入一个整数n，返回一个列表，该列表是斐波那契数列的前n项，注意异常处理（如果传入的参数不是正整数，则报异常）
# def fib(n):
#     if type(n) != type(1) or n < 1:
#         print("error")
#         raise TypeError("传入的参数不是正整数")
#     fibs=[]
#     now=1
#     then=1
#     for i in range(n):
#         fibs.append(now)
#         now,then=then,now+then
#     print(fibs)
#
#
# try:
#     fib(50)
#     fib(-50)
# except Exception as e:
#     print(e)
# else:
#     print("no error")

# [4]	编写函数, 可以接收任意多个数, 返回的是一个元组. 元组的第一个值为所有参数的平均值, 第二个值是大于平均值的所有参数构成的列表，
#       注意异常处理（如果传入的参数不是数字，则报异常）
# def calculate(*args):
#     for ele in args:
#         if type(ele) != type(1) and type(ele) != type(1.0):
#             print("error")
#             raise TypeError("传入的参数不是数字")
#     val=0
#     bigger=[]
#     for i in args:
#         val += i
#     val = val/len(args)
#     for i in args:
#         if i > val:
#             bigger.append(i)
#     print(val,bigger)
#     return (val,bigger)
#
#
# try:
#     calculate(1,2,3,4)
#     calculate("str")
# except Exception as e:
#     print(e)
# else:
#     print("no error")


# [5]	编写函数，传入n个数，返回字典：{‘max’:最大值,’min’:最小值}，注意异常处理（如果传入的参数不是数字，则报异常）
# def maxandmin(*args):
#     for ele in args:
#         if type(ele) != type(1) and type(ele) != type(1.0):
#             print("error")
#             raise TypeError("传入的参数不是数字")
#
#     dict={"max":max(args),"min":min(args)}
#     print(dict)
#     return(dict)
#
#
# try:
#     maxandmin(1,2,3,4,5,6)
#     maxandmin("str")
# except Exception as e:
#     print(e)
# else:
#     print("no error")


# [6]	编写函数, 接收字符串参数, 返回一个元组, 元组的第一个值为字符串中大写字母的个数, 第二个值为小写字母个数，
#       注意异常处理（传入参数不是字符串，则报异常）
# def checkletters(string):
#     if type(string) != type("str"):
#         print("error")
#         raise TypeError("传入的参数不是字符串")
#     capital=0
#     lowercase=0
#     for i in range(len(string)):
#         if string[i].isupper():
#             capital += 1
#         if string[i].islower():
#             lowercase += 1
#     print (f'{string}:capital = {capital}, lowercase = {lowercase}')
#     return (capital, lowercase)
#
#
# try:
#     checkletters("a a a BB")
#     checkletters([1, 2, 3])
# except Exception as e:
#     print(e)
# else:
#     print("no error")


# [7]	编写函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空内容，
# 同[2]

# [8]	编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），要求# with open("info.txt","r",encoding="utf-8") as f:
# #     lns=f.readlines()
# #     for ln in lns:
# #         vs=ln.split(" ")
# #     myname = vs[0]
# #     mypassword = vs[1]
# #
# # login_status = False
# # def login(func):
# #     def inner(*args, **kwargs):
# #         global login_status
# #         if not login_status:
# #             print("come to login")
# #             name = input("please input your name\n")
# #             password = input("please input your password\n")
# #             if name == myname and password == mypassword:
# #                 login_status = True
# #         ret = func(*args, **kwargs)
# #         return ret
# #     return inner
# #
# # @login
# # def func1():
# #     print("func1")
# # @login
# # def func2():
# #     print("func2")
# # @login
# # def func3():
# #     print("func3")
# # @login
# # def func4():
# #     print("func4")
# # func1()
# # func2()
# # func3()
# # func4()登录成功一次，后续的函数都无需再输入用户名和密码；\


# [9]	编写装饰器，计算某个函数的程序执行用时（结束时间-开始时间）；
# import time
#
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         print(f'time: {end-start}s')
#         ret = func(*args, **kwargs)
#         return ret
#     return wrapper
#
# @timer
# def T():
#     time.sleep(1)
#
#T()


# [10]	如下，每个小字典的name对应股票名字，shares对应多少股，price对应股票的价格
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
# # 	使用内置函数计算购买每支股票的总价
# # 	用filter过滤出单价大于100的股票
sum = []
for idx in range(len(portfolio)):
    sum.append(portfolio[idx]["shares"] * portfolio[idx]["price"])
print(sum)

expensive = list(filter(lambda x: x["price"] > 100, portfolio))
print(expensive)

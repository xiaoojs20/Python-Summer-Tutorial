# 利用装饰器， 添加函数的开始时间，和结束时间
# import time
#
#
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         print(f'The start time: {start}s')
#         print(f'The end time: {end}s')
#         print(f'The cost time: {end - start}s')
#         ret = func(*args, **kwargs)
#         return ret
#     return wrapper
#
#
# @timer
# def spend_time(n):
#     time.sleep(n)
#     return "task1"
#
# print(spend_time(1))

# 利用装饰器， 实现函数调用前的登录验证（只需要登录1次）。
# myname = 'xjs'
# mypassword = '123456'
#
# login_status = False
# def login(func):
#     def inner(*args, **kwargs):
#         global login_status
#         if not login_status:
#             print("come to login")
#             name = input("please input your name\n")
#             password = input("please input your password\n")
#             if name == myname and password == mypassword:
#                 print("login successfully")
#                 login_status = True
#         ret = func(*args, **kwargs)
#         return ret
#     return inner
#
# @login
# def func1():
#     print("run func1")
# @login
# def func2():
#     print("run func2")
# @login
# def func3():
#     print("run func3")
# @login
# def func4():
#     print("run func4")
# func1()
# func2()
# func3()
# func4()


# # 利用函数生成器， 编写一个函数，得到素数的生成器。
# def get_primes(value):
#     all_primes = []
#     for i in range(2, value):
#         is_prime = True
#         for k in all_primes:
#             if i % k == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             all_primes.append(i)
#             yield i
# n_count = 0
# b = get_primes(10000000000000)
# for i in b:
#     if i > 100:
#         break
#     print(i)


# 利用函数生成器， 编写一个函数，监测某文件中是否有某字符串。
# 第一版粗糙
# def has_str(string):
#     with open("test.txt", "r", encoding="utf-8") as f:
#         lns = f.readlines()
#         strlns=str(lns)
#         print(strlns)
#     has_string = False
#     if string in strlns:
#         has_string = True
#     if has_string:
#         yield ("has it!")
#     else:
#         yield ("not has it")
#
# for i in has_str("abcde"):
#     print(i)
# for i in has_str("abcd"):
#     print(i)
#
# 第二次ref
def get_file_info(file_name):
    with open(file_name,"r",encoding="utf-8") as f:
        for lns in f:
            yield lns

def jude_str_in_file(file_name,find_str):
    file_inter = get_file_info(file_name)
    for lns in file_inter:
        if lns.count(find_str):
            return True
        return False

print(jude_str_in_file("test.txt","abc"))






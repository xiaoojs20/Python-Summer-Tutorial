# 输出未来1年内的所有周日所对应日期字符串的列表，比如：[‘2021-09-05’, ‘2021-09-12’…]。
# import time
# t1=time.time()
# t2=time.time()+3*24*3600
#
# Sundays = []
# for i in range(365):
#     t3 = t1 + i*24*3600
#     if (t3-t2)%(7*24*3600)==0:
#         Sundays.append(time.strftime("%Y-%m-%d", time.localtime(t3)))
# print(Sundays)

# 用两种方式来判断文件是否相同：(1)直接内存对比，(2)通过hashlib的方式。
# 1
# def is_equ(f1,f2):
#     with open(f1,"r") as f1:
#         lns1 = f1.readlines()
#     with open(f2,"r") as f2:
#         lns2 = f2.readlines()
#
#     if lns1 == lns2:
#         return True
#     else:
#         return False
#
# print(is_equ('1.txt','2.txt'))

# 2 通过hashlib的方式判断文件相等
# import hashlib
#
# def is_equ(f1, f2):
#     m1 = hashlib.md5()
#     m2 = hashlib.md5()
#     with open(f1,"rb") as f1:
#         m1.update(f1.read(1024))
#         hash1 = m1.digest()
#         print(hash1)
#     with open(f2, "rb") as f2:
#         m2.update(f2.read(1024))
#         hash2 = m2.digest()
#         print(hash2)
#
#     if hash1 == hash2:
#         return True
#     else:
#         return False
# print(is_equ('1.txt', '2.txt'))

# 用户输入目录名称，以列表形式显示该目录下的所有文件与文件夹信息。
# import os
# dir_name = input("请输入目录名称")
# dir_info = []
# files = os.listdir(dir_name)
# # os.chdir(files)
# for i in files:
#     if os.path.isfile(i):
#         dir_info.append((i,"file"))
#     else:
#         dir_info.append((i, "dir"))
# print(files)
# print(dir_info)


# 写一个6位随机验证码程序（使用random模块)，要求验证码中至少包含一个数字、一个小写字母、一个大写字母.
# import random,string
# while True:
#     is_legal = [False, False, False]
#     ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 6))
#     for i in range(6):
#         if ran_str[i].islower():
#             is_legal[0] = True
#         elif ran_str[i].isupper():
#             is_legal[1] = True
#         elif ran_str[i].isdigit():
#             is_legal[2] = True
#         else:
#             continue
#     if not (False in is_legal):
#         break
#
#
# print(ran_str)




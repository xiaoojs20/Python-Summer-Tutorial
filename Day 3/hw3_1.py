# 写函数，接收n个数字，求这些参数数字的和
# def sum(*args):
#     sum_vals =0
#     for i in args:
#         sum_vals += i
#     # print(sum_vals)
#     return sum_vals
# sum(5,5,6,6)


# 编写一个函数cacluate, 可以接收任意多个数,返回的是一个元组，元组的第一个值为所有参数的平均值, 第二个值是大于平均值的所有数.
# def calculate(*args):
#     val=0
#     bigger=[]
#     for i in args:
#         val += i
#     val = val/len(args)
#     for i in args:
#         if i > val:
#             bigger.append(i)
#     print(val,bigger)
#     tp=(val,bigger)
#     return tp
# calculate(5,5,6,6,25,99)


# 找出传入的列表或元组的奇数位对应的元素，并返回一个新的列表
# def oddpos(*args):
#     odd=[]
#     for i in range(len(args)):
#         if i%2!=0:
#             odd.append(args[i])
#     print(odd)
#     return odd
# oddpos(0,1,2,3,4,5)

# 写一个函数，判断用户传入的列表长度是否大于2，如果大于2，只保留前两个，并将新内容返回给调用者
# def only2(list):
#     if len(list)<=2:
#         print(list)
#         return list
#     elif len(list)>2:
#         print(list[0:2])
#         return list[0:2]
# only2([1,2,3,4])
# only2([1])


# 写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果
# def statistic(string):
#     letter=0
#     number=0
#     space=0
#     other=0
#     for i in range(len(string)):
#         if string[i].isalpha():
#             letter += 1
#         elif string[i].isdigit():
#             number += 1
#         elif string[i].isspace():
#             space += 1
#         else:
#             other += 1
#     print(f'letter = {letter} number = {number} space = {space} other = {other}')
# str = "123456 abc !!"
# statistic(str)

# 写一个函数，判断用户传入的对象（字符串、列表、元组）的元素是否为空
# def is_none(xobj):
#     if len(xobj)==0:
#         return True
#     else:
#         return False
# str1=""
# str2=" "
# list1=[]
# list2=[1,22]
# tuple1=()
# tuple2=(2,4)
# print(is_none(str1))
# print(is_none(str2))
# print(is_none(list1))
# print(is_none(list2))
# print(is_none(tuple1))
# print(is_none(tuple2))

# 编写函数, 接收一个列表(包含30个1~100之间的随机整形数)和一个整形数k, 返回一个新列表.
# 函数需求:
# 将列表下标k之前对应(不包含k)的元素逆序;
# 将下标k及之后的元素逆序;
# 例如：输入两个参数：[1,2,3,4,5] 2， 返回结果：  [2,1,5,4,3]
# 注意：异常处理：
# （1）输入非列表
# （2）k不在范围之内

# import random
#
#
# def old2new(list, num):
#     if type(list)!=type([]):
#         print("error")
#         raise TypeError("输入非列表")
#     if num>=len(list):
#         print("error")
#         raise IndexError("下标k不在范围之内")
#     front_list = []
#     end_list = []
#     new_list = []
#     for i in range(num):
#         front_list.append(list[i])
#     front_list.reverse()
#     for i in range(num, len(list)):
#         end_list.append(list[i])
#     end_list.reverse()
#     new_list = front_list + end_list
#     print(new_list)
#     return new_list
#
# # 验证
# old_list = []
# for idx in range(100):
#     i = random.randint(1, 100)
#     old_list.append(i)
#
# try:
#     old2new(old_list, 5)
#     old2new([1,2,3,4,5],2)
# except Exception as e:
#     print(e)
# else:
#     print("无异常")





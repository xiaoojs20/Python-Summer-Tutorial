# 7-1 递归 二分查找
def search(a_li, item):
    n = len(a_li)
    if n > 0:
        mid = n//2
        if a_li[mid] == item:
            return True
        elif a_li[mid] > item:
            return search(a_li[:mid], item)
        else:
            return search(a_li[mid+1:], item)
    else:
        return False

li = [0, 5, 8, 10, 65, 99, 100]
print(search(li, 99))
print(search(li, -1))


# 7-2
# cal_dict = {'+': lambda x, y: x + y, '-': lambda x, y: x - y,
#             '*': lambda x, y: x * y, '/': lambda x, y: x / y}
#
#
# def cal(flag, x, y):
#     func = cal_dict.get(flag, None)
#     if func:
#         return func(x, y)
#     return None
#
#
# print(cal('+', 100, 10))
# print(cal('*', 100, 10))
# print(cal('-', 100, 10))

# 7-3

# 方法一：调用字典
# area_dict = {'rect': lambda x, y: x * y, 'circle': lambda x: 3.1415926 * x * x,
#             'square': lambda x: x * x}
#
#
# def area(flag, *args):
#     func = area_dict.get(flag, None)
#     if func:
#         return func(*args)
#     return None
#
#
# print(area('rect', 100, 10))
# print(area('circle', 10))
# print(area('square', 10))

# 方法二：嵌套函数



# 7-4
# def x2():
#     li = [1, 2, 3, 4, 5]
#     x=list(map(lambda x: x ** 2, li))
#     return x
# print(x2())


# 7-5
# def ab():
#     li = [1, 2, -3, -4, 5]
#     ab=list(map(lambda x: abs(x), li))
#     return ab
# print(ab())

# 7-6 偶数项
# def even():
#     li = [0, 1, "s", "k", True, False]
#     e_num = list(filter(lambda x: True if x % 2 == 0 else False, [i for i in range(len(li))]))
#     e_list = [li[i] for i in e_num]
#     return e_list
#
#
# print(even())


# 7-7
# def sumval():
#     from functools import reduce
#     li = [0, 1, 2, 3, 4, 5, 6]
#     x=reduce(lambda x, y: x + y, li)
#     return x
# print(sumval())

# 7-8
# def maxval():
#     from functools import reduce
#     li = [0, 1, 2, 30, 4, 5, 6]
#     x = reduce(lambda x, y: x if x >= y else y, li)
#     return x
#
#
# print(maxval())

# 7-9
# dic = [{"name":"p1","salary":200},{"name":"p2","salary":2000},{"name":"p3","salary":1500}]
#
# # 7-9-1 加500工资
#
# 方法一：写一个函数里包含map
# def add_salary(num):
#     now_dic=list(map(lambda x:{"name":x["name"],"salary":x["salary"]+500},dic))
#     print(now_dic)
# print(dic)
# add_salary(500)


# 方法二：先写一个函数再用map
# def add_sal(val):
#     val["salary"] += 500
#     return val
#
#
# print(list(map(add_sal, dic)))

# 7-9-2 工资大于一千的人
# def high_name():
#     high_num=list(filter(lambda x:x["salary"]>1000,dic))
#     names = [x["name"] for x in high_num]
#     return names
# #简化版
# def high_name():
#     return ([x["name"] for x in list(filter(lambda x: x["salary"] > 1000, dic))])
#
# print(high_name())

# 7-9-3 工资最高人名字
# from functools import reduce
#
# # def highest_name():
# #     highest_num = reduce(lambda x, y: x if dic[x]["salary"] > dic[y]["salary"] else y, [i for i in range(len(dic))])
# #     highest_name = dic[highest_num]["name"]
# #     return highest_name
#
#
# # 简化版可读性较差
# def highest_name():
#     return dic[reduce(lambda x, y: x if dic[x]["salary"] > dic[y]["salary"] else y, [i for i in range(len(dic))])]["name"]
#
#
# print(highest_name())


# 7-9-4 最高工资
# from functools import reduce
# def highest_salary():
#     return reduce(lambda x, y: x if x >= y else y, [dic[i]["salary"] for i in range(len(dic))])
#
# print(highest_salary())

# 7-9-5
# from functools import reduce
# def avg_salary():
#     return reduce(lambda x, y: x + y, [dic[i]["salary"] for i in range(len(dic))]) / len(dic)
#
# print(avg_salary())

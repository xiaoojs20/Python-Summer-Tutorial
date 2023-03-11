# def foo(*args, **kwargs):
#     print(args)
#     print(kwargs)
# foo(1, 2, 3, d=5, c=4)
# # foo(1,2,3, key = 1, 4,5,6,cc = 2)
#
# def foo(x, *args, y=2):
#     print(x)
#     print(y)
#     print(args)
# foo(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, y=2) # 调用函数
# #*args与位置参数和默认参数混用:*args要放到位置参数后面，默认参数要放最后。

# 打包与解包
# def bar(x,y,z):
#     print(x)
#     print(y)
#     print(z)
# bar(*(1,2,3))# <==> 等价于 bar(1,2,3)
# dic={'x':1, 'y':2,'z':3}
# print(dic)
# print(*dic)
# # print(**dic) #***********************************
# bar(**dic)

# def foo(x, y, z):
#     print(x, y, z)
#
#
# tup = 1, 2, 3 #自动变成元组
# foo(1, 2, 3)
# foo(*(1, 2, 3))  # <==> foo(1, 2, 3) <==> foo(*tup)
# print(*tup, sep='<>')  # <==>print(1, 2, 3)
# # 两种方式是等价的。。。
# print(1, 2, 3, sep='<>')  # <==>print(1, 2, 3)
# foo(*tup)


# def foo(*args, **kwargs):
#     print(args)
#     print(kwargs)
# foo(1, 2, 3, a = 1, b = 2, c= 'c')
# foo(1, 2, a = 1, b = 2, c= 'c', d = 12, c = 'aaa') # keyword argument repeated: c

# def foo(x, y = 1, *args):
# # def foo(x, *args, y=1):
#     print(x)
#     print(y)
#     print(args)
# # foo(1, 2, 3, 4, 5, 6, 7, 8, y = 12) #foo() got multiple values for argument 'y'
# foo(1, 2, 3, 4, 5, 6, 7, 8)
# # foo(1, 2, 3, 4, 5, 6, 7, 8, y = 22) # foo() got multiple values for argument 'y'
# # foo(1, 2, 3, 4, 5, 6, 7, 8, y = 22, z = 15) foo() got multiple values for argument 'y'
# # foo(1, y = 22, 2, 3, 4, 5, 6, 7, 8) # positional argument follows keyword argument

# def foo(x, y = 1, *args, **kwargs):
#     print(x)
#     print(y)
#     print(args)
#     print(kwargs)
# foo(1, x1 = 10, y = 20, z1 = 30)

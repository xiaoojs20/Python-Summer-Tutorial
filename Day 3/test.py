# def function_name(para1, para2, para3):
#     print(para1, para2, para3)
#     return ":".join([str(para1), str(para2), str(para3)])
#
# a = function_name(1, 2, 3)
# print(a)
#
# # 调用方法1：
# b = function_name(para1=11,para2=22,para3=21)
#
# # 调用方法2：
# dict = {'para1':11, 'para2':22, 'para3':1}
# c = function_name(**dict)
# print(c)

# 定义先后顺序：位置参数 > 默认参数 > 不定数组*args  > **kwargs
# def create_person(name, age = 18, *args, **kwargs):
#     print(name)
#     print(*args)
#     print(age)
#     print(kwargs)
# # 两种正确的调用方式
# create_person('张三', 1, 2,3, country = '中国', age = 22)
# create_person('张三', 1, 2,3, age = 22, country = '中国')
# # 2.用法有问题！
# create_person('张三', 1, 4, 5, 6, age = 22, country = '中国')

# print(globals())
# i = 1
# print(globals())

# def fact(n):
#     if n==1:
#         return 1
#     return n * fact(n - 1)
#
# print(fact(10))

# print (list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# def foo():
#     a = 1
#     def bar():
#         a = a + 1
#         return a
#     return bar
# c =foo()
# c()

# flist = []
# for i in range(4):
#     print(id(i))
#     def foo(x):
#         print(id(i))
#         print(x + i)
#     flist.append(foo)
#
# print("this:", id(i))
# i = 2
# for f in flist:
#     f(2)

# origin = [0, 0]  # 坐标系统原点
# legal_x = [0, 50]  # x轴方向的合法坐标
# legal_y = [0, 50]  # y轴方向的合法坐标
# def create(pos=origin):
#     def player(direction,step):   # 这里应该首先判断参数direction,step的合法性，比如direction不能斜着走，step不能为负等
#                                     # 然后还要对新生成的x，y坐标的合法性进行判断处理，这里主要是想介绍闭包，就不详细写了。
#         new_x = pos[0] + direction[0]*step
#         new_y = pos[1] + direction[1]*step
#         pos[0] = new_x
#         pos[1] = new_y    #注意！此处不能写成 pos = [new_x, new_y]
#         return pos
#     return player
# player = create()  # 创建棋子player，起点为原点
# print(player([1,0],10))  # 向x轴正方向移动10步
# print(player([0,1],20))  # 向y轴正方向移动20步
# print(player([-1,0],10))  # 向x轴负方向移动10步

# class A:
#     pass # pass ⽤于⼀个块必须存在，但是你⼜不想写任何语句的时候，作为占位符
#
#
# A.b = 1 # 为类型 A 动态添加了静态公有成员变量 b
# print(A.b)
# a = A() # 实例化 A
# print(A.b)
# a.b = 3 # 为对象 a 添加了公有成员 b
# print(a.b)
# print(A.b)
# del a.b # del 可以删除⼀个变量，这⾥删掉了 a 的成员 b
# print(a.b)

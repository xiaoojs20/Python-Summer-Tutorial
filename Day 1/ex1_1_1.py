# 利用for循环和range输出：
# for循环从大到小输出1 - 100
# for i in range(100, 0, -1):
#     print(i)

# for循环从小到到输出100 - 1
# for i in range(1, 101):
#     print(i)

# while循环从大到小输出1 - 100
# i=100
# while i>0:
#     print(i)
#     i-=1

# while循环从小到到输出100 – 1
# i=1
# while i<=100:
#     print(i)
#     i+=1

# 利用while循环输出：
# 使用 while 循环实现输出 1,2,3,4,5, 7,8,9, 11,12
# for i in range(1,13):
#     if i!=6 and i!=10:
#         print(i)

# 使用while 循环输出100-50，从大到小，如100，99，98…，到50时再从0循环输出到50，然后结束
# i=100
# while i>=50:
#     print(i)
#     i-=1
# i=0
# while i<=50:
#     print(i)
#     i+=1

# 使用 while 循环实现输出 1-100 内的所有奇数
# i=1
# while i<=100:
#     if i%2!=0:
#         print(i)
#     i+=1

# 使用 while 循环实现输出 1-100 内的所有偶数
# i=1
# while i<=100:
#     if i%2==0:
#         print(i)
#     i+=1

# 使用while循环实现输出2-3+4-5+6…+100 的和
# i=2
# sum_val=0
#
# while i<=100:
#     if i%2==0:
#         sum_val+=i
#         i+=1
#     elif i%2!=0:
#         sum_val-=i
#         i+=1
# print(sum_val)

print("hello")
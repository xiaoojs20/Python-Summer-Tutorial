#  计算求100以内的质数和。
# sum_val=0
# for i in range(2,100):
#     j=2
#     flag=1
#     while j<i:
#         if i%j!=0:
#             j+=1
#             continue
#         elif i%j==0:
#             flag=0
#             break
#
#     if flag==1:
#         sum_val+=i
# print(sum_val)




# 利用for循环和range输出9 * 9乘法表

# for i in range(1,10):
#     for j in range(1,10):
#         if i<=j:
#             print(f'{i}*{j}={i*j}')


# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

# num=1
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if(i!=j and i!=k and j!=k):
#                 print(num,i*100+j*10+k)
#                 num+=1

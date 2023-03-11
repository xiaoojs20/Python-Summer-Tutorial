# 猜年龄游戏。
# 首先预设1个年龄。
# 用户输入猜测的年龄，如果大了，则提示“大”，如果小了，则提示“小”，如果相同，则提示“猜对了”。
# 允许用户最多猜测3次，3次均猜不中，则提示：“3次猜错，游戏失败！”

# real_age=24
# flag=0
#
# for i in range(3):
#         guess = input("please input your guess")
#         guess = int(guess)
#         if guess<real_age:
#             print("小")
#         elif guess>real_age:
#             print("大")
#         elif guess==real_age:
#             print("猜对了")
#             flag=1
#             break
# if flag==0:
#     print("猜错了")



# 猜4位数字游戏。
# 1、输入一个4位数字a（不能重复）
# 2、猜一个数b，程序自动答复：mAnB
# m:数字和位次全对的数量。
# n:只有数字对但位不对个数的数量。
# m+n <= 4
# 3、4A，代表完全猜出来了。

# a=1234
# m=0
# n=0
# b=input("please input b")
# b=int(b)
#
# if b%10==4:
#     m+=1
# if b%100>=30 and b%100<=39:
#     m+=1
# if b%1000>=200 and b%1000<=299:
#     m+=1
# if b>=1000 and b<=1999:
#     m+=1
#
# if b%10==1 or (b%100>=10 and b%100<=19) or (b%1000>=100 and b%1000<=199) or (b>=1000 and b<=1999):
#     n+=1
# if b%10==2 or (b%100>=20 and b%100<=29) or (b%1000>=200 and b%1000<=299) or (b>=2000 and b<=2999):
#     n+=1
# if b%10==3 or (b%100>=30 and b%100<=39) or (b%1000>=300 and b%1000<=399) or (b>=3000 and b<=3999):
#     n+=1
# if b%10==4 or (b%100>=40 and b%100<=49) or (b%1000>=400 and b%1000<=499) or (b>=4000 and b<=4999):
#     n+=1
#
# str=f'{m}A{n}B'
# print(str)




# 实现用户输入用户名和密码，并登录验证测试：
# 当用户名为 seven 且 密码为 123 时,显示登陆成功,否则显示登陆失败!
# 失败时，允许重复输入三次。
# 失败3次后，则提醒出错，程序运行退出。
# flag=1
# for i in range(3):
#     name=input("please input your name")
#     password=input("please input your password")
#     if name=='seven' and password=='123':
#         print("登陆成功")
#         flag=0
#         break
#     else:
#         print("登陆失败")
#
# if flag==1:
#     print("出错")

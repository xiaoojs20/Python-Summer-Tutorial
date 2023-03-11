# 编程计算：1+2+…+n，n为一个从键盘输入的数字。
# n=input("请输入一个数字")
# a=int(n)
# i=0
# sum_val=0
#
# while i<=a:
#     sum_val+=i
#     i+=1
#
# print(sum_val)

# 假设一年期定期利率为3.25%，计算一下需要过多少年，一万元的一年定期存款连本带息能翻番？
# year=0
# money=10000
# while money<20000:
#     money=1.0325*money
#     year+=1
# print(year)

#  一球从100米高度自由落下，每次落地后反跳回原高度的一半；求它在第10次落地时，共经过多少米？第10次反弹多高？

# i=0
# length=100.0
# high=100.0
# while i<10:
#     high=high/2.0
#     length += high * 2
#     i+=1
# length-=high*2 #减去最后一次
# print(length)
# print(high)


# 编程实现：从键盘接收一百分制成绩（0~100），要求输出其对应的成绩等级A~E。
# 其中，90分以上为'A'，80~89分为'B'，70~79分为'C'，60~69分为'D'，60分以下为'E'，若不是0-100之间，则报错并要求再次输入。
# score=input("input your score")
# score=int(score)
# if score<=100 and score>=90:
#     print("A")
# elif score<=89 and score>=80:
#     print("B")
# elif score <= 79 and score >= 70:
#     print("C")
# elif score<=69 and score>=60:
#     print("D")
# elif score<=59 and score>=0:
#     print("E")
# else:
#     print("error")

#  输入一年份，判断该年份是否是闰年并输出结果。
# 注：凡符合下面两个条件之一的年份是闰年。 （1） 能被4整除但不能被100整除。 （2） 能被400整除。
# year=input("please input a year")
# year=int(year)
# if year%4==0 and year%100!=0 :
#     print("this year is a leap year")
# elif year%400==0:
#     print("this year is a leap year")
# else:
#     print("this year is not a leap year")


# 制作趣味模板程序
# 需求：根据用户输入的名字、地点、爱好，进行任意显示，如：敬爱可爱的xxx，最喜欢在xxx地方YYY
# name=input("please input your name")
# address=input("please input your address")
# hobby=input("please input your hobby")
#
# str=f'敬爱可爱的{name}，最喜欢在{address}{hobby}'
# print(str)


# 使用while,完成以下图形的输出
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# i=1
# j=0
# while i<=5:
#     while j<=i:
#         if j<i:
#             print("* ", end='')
#             j+=1
#         if j==i:
#             print('\n', end='')
#             i+=1
#             j=0
#             break
# i-=2
# while i>=1:
#     while j<=i:
#         if j<i:
#             print("* ", end='')
#             j+=1
#         if j==i:
#             print('\n', end='')
#             i-=1
#             j=0
#             break

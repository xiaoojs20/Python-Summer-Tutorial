# 双色球（假设一共八个球，6个红球，球号1-32、2个蓝球，球号1-16）
# 确保用户不能重复选择，不能超出范围
# 用户输入有误时有相应的错误提示
# 最后展示用户选择的双色球的号码

wrong=0
red=input("请输入红球号码，并用空格隔开")
blue=input("请输入蓝球号码，并用空格隔开")
red=red.split(' ')
blue=blue.split(' ')

for i in range(1,33):
    i=str(i)
    if red.count(i)>1:
        print("不能重复选择红球")
        wrong=1
        break

for i in range(1,17):
    i = str(i)
    if blue.count(i)>1:
        print("不能重复选择蓝球")
        wrong = 1
        break

for i in range(len(red)):
    red[i] = red[i].strip()
    tmp = int(red[i])
    if tmp<1 or tmp>32:
        print("选红球不能超出范围")
        wrong = 1
        break

for i in range(len(blue)):
    blue[i]=blue[i].strip()
    tmp = int(blue[i])
    if tmp<1 or tmp>16:
        print("选蓝球不能超出范围")
        wrong = 1
        break

if len(red)<6:
    print("红球少选")
    wrong = 1
if len(red)>6:
    print("红球多选")
    wrong = 1
if len(blue)<2:
    print("蓝球少选")
    wrong = 1
if len(blue)>6:
    print("蓝球多选")
    wrong=1

if wrong==0:
    print(red+blue)
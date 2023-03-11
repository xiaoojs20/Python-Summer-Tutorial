# 在不改变列表数据结构的情况下找最大值li = [1,3,2,7,6,23,41,243,33,85,56]
# li = [1,3,2,7,6,23,41,243,33,85,56]
# max_val=max(li)
# print(max_val)


# 在不改变列表中数据排列结构的前提下，找出以下列表中最接近最大值和最小值的平均值的数
# li = [-100,1,3,2,7,6,120,121,140,23,411,99,243,33,85,56]
# max_val=max(li)
# min_val=min(li)
# val=(max_val+min_val)/2
# min_dis=abs(li[0]-val)
#
# for idx in range(len(li)):
#     dis=abs(li[idx]-val)
#     if dis<min_dis:
#         min_dis=dis
#         close=li[idx]
# print(val)
# print(close)


# 列表test = ['alex','egon','yuan','wusir','666']中，编程实现：
# 把666替换成999
# 获取"yuan"的索引
# 假设不知道前面有几个元素，分片得到最后的三个元素
# test = ['alex','egon','yuan','wusir','666']
# test[test.index('666')]='999'
# print(test.index('yuan'))
# print(test[-3:])

# 求100以内不能被3整除的所有数，并把这些数字放在列表里，并求出这些数字的总和和平均数。
# li=[]
# for i in range(100):
#     if i%3!=0:
#         li.append(i)
# print(li)
# sum_val=0
# avg=0
# for idx in range(len(li)):
#     sum_val+=li[idx]
# avg=sum_val/len(li)
# print(avg)


# 查找列表中元素，移除每个元素的空格，并查找以a或A开头并且以c结尾的所有元素。
li = ["alec", " aric", "Alex", "Tony", "rain"]
tu = ("alec", " aric", "Alex", "Tony", "rain")
dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}

for idx in range(len(li)):
    li[idx]=li[idx].strip()

for idx in range(len(li)):
    if (li[idx].startswith('a') or li[idx].startswith('A')) and li[idx].endswith('c'):
        print(li[idx])

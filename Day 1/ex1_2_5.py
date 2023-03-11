# 有两个列表
l1 = [11,22,33]
l2 = [22,33,44]
l3=[]
s1=set()
s2=set()
s3=set()
for i in range(len(l1)):
    s1.add(l1[i])
for i in range(len(l2)):
    s2.add(l2[i])

# 或者直接采用列表转集合
s1=set(l1)
s2=set(l2)

# 功能要求：
# 获取内容相同的元素列表
s3=s1 & s2
for key in s3:
    l3.append(key)
l3=list(s3) # 或者直接转换
print(l3)

# 获取l1中有，l2中没有的元素列表
# s3=s1-s2
# for key in s3:
#     l3.append(key)
# print(l3)

# 获取l2中有，l1中没有的元素列表
# s3=s2-s1
# for key in s3:
#     l3.append(key)
# print(l3)

# 获取l1和l2中内容都不同的元素
# s3=s1^s2
# for key in s3:
#     l3.append(key)
# print(l3)

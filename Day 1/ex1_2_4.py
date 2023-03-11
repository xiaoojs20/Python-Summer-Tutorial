dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
# 请循环输出所有的key
# for key in dic.keys():
#     print(key)

# 请循环输出所有的value
# for value in dic.values():
#     print(value)

# 请循环输出所有的key和value
# for key, value in dic.items():
#     print(key, value)

# 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
# dic["k4"]="v4"
# print(dic)

# 请在修改字典中“k1”对应的值为“alex”，输出修改后的字典
# dic["k1"]="alex"
# print(dic)

# 请在k3对应的值中追加一个元素44，输出修改后的字典
# dic["k3"].append(44)
# print(dic)

# 请在k3对应的值的第1个位置插入个元素18，输出修改后的字典
# dic["k3"].insert(1,18)
# print(dic)


# 元素分类
# 有如下值列表[11,22,33,44,55,66,77,88,99,90]，将所有大于66的值保存至字典的第一个key中，将小于66的值保存至第二个key的值中。
# 即：{‘k1’:大于66的所有值列表, ‘k2’:小于66的所有值列表}
# list=[11,22,33,44,55,66,77,88,99,90]
# dict={"k1":[],"k2":[]}
#
# for key in range(len(list)):
#     if list[key]>66:
#         dict["k1"].append(list[key])
#     elif list[key]<66:
#         dict["k2"].append(list[key])
# print(dict)
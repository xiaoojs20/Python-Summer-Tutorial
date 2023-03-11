# 课堂练习（1）- 生成人员列表的几种方法

# # 直接法
#
# person_list = [{"name":"张三","age":19,"country":"中国",},
#                {"name":"李四","age": 29, "country": "中国",},
#                {"name": "王五", "age": 9, "country": "中国",}]
# print(person_list)
#
# # 方式2：函数法
# def create_person(name, age, country):
#     return {"name":name, "age":age, "country": country}
# person_list =[]
# person_list.append(create_person(name = "张三", age = 18, country='中国'))
# person_list.append(create_person(age = 29, name = "李四", country = '中国'))
# person_list.append(create_person(name = "王五", country = '美国', age = 9))
# print(person_list)
#
# # person_list.append(create_person("张三", age = 18, country='中国'))
# # person_list.append(create_person(age = 29, "李四", country = '中国'))


# def create_person(*args, **kwargs):
#     print(args)
#     print(kwargs)
#     if kwargs.get('cc', None):
#         print("this person has cc!!!", kwargs['name'])
#     else:
#         print("this person not has cc!!!", kwargs['name'])
#     return kwargs
#     # return {}
#     # return {"name":name, "age":age, "country": country}
# person_list =[]
# person_list.append({"name" : "张三", "age" : 18, "country":'中国', "red" : True})
# person_list.append(create_person(age = 29, name = "李四", country = '中国'))
# person_list.append(create_person(name = "王五", country = '美国', age = 9, cc = 'tt'))
# print(person_list)

# # 定义先后顺序：位置参数 > 默认参数 > 不定数组*args  > **kwargs
# def create_person(name, age = 18, *args, **kwargs):
#     print(name)
#     print(*args)
#     print(age)
#     print(kwargs)
# # 两种正确的调用方式
# create_person('张三',country = '中国', age = 22)
# create_person('张三', age = 22, country = '中国')
# # 2.用法有问题！
# # create_person('张三', 1, 4, 5, 6, age = 22, country = '中国')

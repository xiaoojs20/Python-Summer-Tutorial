# 自己封装1个MyDict，支持以下操作：
# 	支持for … in
# 	 [] 操作， 访问key-value 值，类似于：dic[key] = value
# 	通过.操作，访问key-value 值，类似于：dic.key = value
# 	要求: key只能是字符串（字符串的字符构成只能是下划线、数字或字母）
# 	支持get 操作， 输入 key， 返回 value…
# 	支持len() 操作
import re

class MyDict:
    def __init__(self, dic):
        self.dic = dic
        self.pos = 0
        self.keys = list(dic.keys())
        self.values = list(dic.values())
        self.key = list(self.keys)[self.pos]
        self.value = list(self.values)[self.pos]
        for idx in range(len(self.keys)):
            if not re.match('^[A-Za-z0-9_-]*$', self.keys[idx]):
                raise ValueError("key只能是字符串（字符串的字符构成只能是下划线、数字或字母）")

    def __iter__(self):
        # return [list(self.keys)[self.pos], list(self.values)[self.pos]]
        return self

    def __next__(self):
        if self.pos >= len(self.keys):
            raise StopIteration("迭代结束")
        key = list(self.keys)[self.pos]
        value = list(self.values)[self.pos]
        self.pos += 1
        return key, value

    def __setitem__(self, key, value):
        if re.match('^[A-Za-z0-9_-]*$', key):
            self.dic[key] = value
        else:
            raise ValueError("key只能是字符串（字符串的字符构成只能是下划线、数字或字母）")

    def __getitem__(self, item):
        return self.dic[item]

    def __delitem__(self, key):
        del self.dic[key]

    def __getattr__(self, key):
        return self.dic[key]

    def __get__(self, key):
        return self.dic[key]

    def __set__(self, key, value):
        if re.match('^[A-Za-z0-9_-]*$', key):
            self.dic[key] = value
        else:
            raise ValueError("key只能是字符串（字符串的字符构成只能是下划线、数字或字母）")

    def __delete__(self, key):
        self.dic.pop(key)

    def get(self,key):
        return self.dic[key]

    def __len__(self):
        return len(self.dic)


dic1 = MyDict({"name": "张三", "sex": "男", "age": 18})
for ele in dic1:
    print(ele)
print(dic1["name"])
print(dic1.age)
print(dic1.sex)
print(dic1.get("sex"))
print(len(dic1))

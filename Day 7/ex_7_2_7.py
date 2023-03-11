# 1
class MyIntList:
    def __init__(self, li):
        self.li = li
        self.pos = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.pos >= len(self.li):
            raise StopIteration("迭代结束")
        value = self.li[self.pos]
        self.pos += 1
        return value


li = MyIntList([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

flag = 0
for ele in li:
    if flag % 2 == 0:
        print(ele)
        flag += 1
    else:
        flag += 1


# 2
class MyPrime:
    def __init__(self, max_num):
        self.p = [2]
        self.max_num = max_num
        self.pos = 0
        for i in range(2, self.max_num):
            for temp in range(2, i):
                if i % temp == 0:
                    break
                elif temp == i - 1:
                    self.p.append(i)

    def __iter__(self):
        return self

    def __next__(self):
        if self.pos >= len(self.p):
            raise StopIteration("迭代结束")
        value = self.p[self.pos]
        self.pos += 1
        return value


li = MyPrime(100)
for ele in li:
    print(ele)


# 3
class MyFile:
    def __init__(self, file_name, str_name):
        self.file_name = file_name
        self.str_name = str_name
        self.pos = 0
        self.text = ""
        with open(file_name,"r") as fp:
            self.text_list = fp.readlines()
        for idx in range(len(self.text_list)):
            self.text += self.text_list[idx]
        print(self.text)

    def __iter__(self):
        return self

    def __next__(self):
        # 包含子字符串
        if self.str_name in self.text:
            idx = self.text.find(self.str_name)
            if self.pos >= idx+len(self.str_name):
                raise StopIteration("迭代结束")
            value = self.text[self.pos]
            self.pos += 1
            return value
        else:
            print("buzai")
            if self.pos >= len(self.text):
                raise StopIteration("迭代结束")
            value = self.text[self.pos]
            self.pos += 1
            return value


f1 = MyFile("myfile.txt","123")
for ele in f1:
    print(ele)
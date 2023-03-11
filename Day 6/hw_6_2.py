# 2.	用面向对象的形式编写一个老师角色, 并实现以下功能, 获取老师列表,
# 创建老师、删除老师、创建成功之后通过 json序列化保存到文件里，并在下一次重启程序时能读取到创建的老师信息

import json
import os
if not os.path.exists("teacher.json"):
    teachers = []
    with open("teacher.json", "w") as fp:
        json.dump(teachers, fp)

class teacher:
    teachers = []

    def __init__(self, name, sex, subject):
        self.name = name
        self.sex = sex
        self.subject = subject
        with open("teacher.json") as fp:
            teacher.teachers = json.load(fp)
        teacher.teachers.append({"姓名": self.name, "性别": self.sex, "科目": self.subject})
        print(f'{self.name}成为清华大学的{self.subject}老师')
        with open("teacher.json", "w") as fp:
            json.dump(teacher.teachers, fp)

    def delete(self):
        teacher.teachers.remove({"姓名": self.name, "性别": self.sex, "科目": self.subject})
        print(f'{self.name}被清华大学辞退')
        with open("teacher.json", "w") as fp:
            json.dump(teacher.teachers, fp)


if __name__ == "__main__":
    t1 = teacher("小明", "男", "OOP")
    t2 = teacher("李四", "女", "python")
    t2.delete()
    t3 = teacher("王五", "男", "DSA")
    print(teacher.teachers)



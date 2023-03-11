# 1.	编写程序, 编写一个学生类, 要求有一个计数器的属性, 统计总共实例化了多少个学生

class student:
    stu_num = 0

    def __init__(self, name, sex, id):
        self.name = name
        self.sex = sex
        self.id = id
        student.stu_num += 1
        print(f'{self.name}考入清华大学，学校共有{student.stu_num}名学生')

    def __del__(self):
        student.stu_num -= 1
        print(f'{self.name}被退学，学校共有{student.stu_num}名学生')


stu1 = student("张三", "男", "01")
stu2 = student("李四", "女", "02")
del stu2
stu3 = student("王五", "男", "03")





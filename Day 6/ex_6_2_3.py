# 选课系统
# 1、编写一个学生类， 姓名，性别，学号，课程成绩(字典)、已选修课程[列表]。
# 2、编写一个教师类， 姓名，性别，拥有的课程[列表]。
# 主要方法：
# 1、学生：(1)选修某课程，(2)查看自己某个课程的成绩。
# 2、教师:  (1) 成为某课程的教师，(2) 退出某个课程

class student():
    def __init__(self, name, sex, id, score, learned_subject):
        self.name = name
        self.sex = sex
        self.id = id
        self.score = score
        self.learned_subject = learned_subject

        subject_str = ""
        for idx in range(len(self.learned_subject)):
            subject_str += self.learned_subject[idx]
            if idx != (len(self.learned_subject) - 1):
                subject_str += '、'
        print(f"{self.name}一共学了{subject_str}")

    def learn(self, subject):
        self.learned_subject.append(subject)

        subject_str = ""
        for idx in range(len(self.learned_subject)):
            subject_str += self.learned_subject[idx]
            if idx != (len(self.learned_subject) - 1):
                subject_str += '、'
        print(f"{self.name}新学了{subject}，一共学了{subject_str}")

    def search(self, subject):

        print(f'{subject}成绩为{self.score[subject]}')


class teacher():
    def __init__(self, name, sex, subject):
        self.name = name
        self.sex = sex
        self.teaching_subject = subject
        subject_str = ""
        for idx in range(len(self.teaching_subject)):
            subject_str += self.teaching_subject[idx]
            if idx != (len(self.teaching_subject) - 1):
                subject_str += '、'
        print(f"{self.name}一共教了{subject_str}")

    def teach(self, subject):
        self.teaching_subject.append(subject)
        subject_str = ""
        for idx in range(len(self.teaching_subject)):
            subject_str += self.teaching_subject[idx]
            if idx != (len(self.teaching_subject) - 1):
                subject_str += '、'
        print(f"{self.name}新教了{subject}，一共教了{subject_str}")

    def secede(self, subject):
        self.teaching_subject.remove(subject)
        subject_str = ""
        for idx in range(len(self.teaching_subject)):
            subject_str += self.teaching_subject[idx]
            if idx != (len(self.teaching_subject) - 1):
                subject_str += '、'
        print(f"{self.name}不教{subject}了，一共教了{subject_str}")


xiaoming = student("小明", "男", "2020010563", {"微积分": 99, "线性代数": 98, "程序设计": 97, "电路原理": 100},
                   ["微积分", "线性代数", "程序设计", "电路原理"])
xiaoming.learn("python")
xiaoming.search("微积分")
daming = teacher("大明", "男", ["程序设计", "单片机基础", "python"])
daming.teach("Java")
daming.secede("python")
class Person:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex


class Student(Person):
    def __init__(self, name, sex, id, score, learned_course):
        super().__init__(name, sex)
        self.id = id
        self.score = score
        self.learned_course = learned_course

        subject_str = ""
        for idx in range(len(self.learned_course)):
            subject_str += self.learned_course[idx].name
            if idx != (len(self.learned_course) - 1):
                subject_str += '、'
        print(f"{self.name}一共学了{subject_str}")

    def learn(self, course):
        self.learned_course.append(course)
        course.stu_list.append(self.name)
        subject_str = ""
        for idx in range(len(self.learned_course)):
            subject_str += self.learned_course[idx].name
            if idx != (len(self.learned_course) - 1):
                subject_str += '、'
        print(f"{self.name}新学了{course.name}，一共学了{subject_str}")

    def search(self, course):
        print(f'{course.name}成绩为{self.score[course]}')


class Teacher(Person):
    def __init__(self, name, sex, course):
        super().__init__(name, sex)
        self.teaching_subject = course
        subject_str = ""
        for idx in range(len(self.teaching_subject)):
            subject_str += self.teaching_subject[idx].name
            if idx != (len(self.teaching_subject) - 1):
                subject_str += '、'
        print(f"{self.name}一共教了{subject_str}")

    def teach(self, course):
        self.teaching_subject.append(course)
        course.tea_list.append(self.name)
        subject_str = ""
        for idx in range(len(self.teaching_subject)):
            subject_str += self.teaching_subject[idx].name
            if idx != (len(self.teaching_subject) - 1):
                subject_str += '、'
        print(f"{self.name}新教了{course.name}，一共教了{subject_str}")

    def secede(self, course):
        self.teaching_subject.remove(course)
        course.tea_list.remove(self.name)

        subject_str = ""
        for idx in range(len(self.teaching_subject)):
            subject_str += self.teaching_subject[idx].name
            if idx != (len(self.teaching_subject) - 1):
                subject_str += '、'
        print(f"{self.name}不教{course.name}了，一共教了{subject_str}")

    def set_score(self, student, course, score):
        student.score[course.name] = score
        print(f'{self.name}给学生{student.name}的{course.name}打了{score}分')


class Course:
    def __init__(self, subject_name, stu_list, tea_list):
        self.name = subject_name
        self.stu_list = stu_list
        self.tea_list = tea_list


Python = Course("python", [], [])
Java = Course("Java", [], [])
DSA = Course("DSA", [], [])
OOP = Course("OOP", [], [])

xiaoming = Student("小明", "男", "2020010563", {Python:100, Java: 98, DSA: 97},
                   [Python, Java, DSA])
xiaoming.learn(Python)
xiaoming.search(Python)
daming = Teacher("大明", "男", [Python, DSA])
daming.teach(Java)
daming.secede(Java)
daming.set_score(xiaoming,Python,99)
print(Python.stu_list)

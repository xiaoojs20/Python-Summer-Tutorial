class Person:
    def __init__(self, id, name, age, weight):
        self.id = id
        self.name = name
        self.age = age
        self.weight = weight
        self.func_lock = True
        self.pwd = "123456"

    def run(self):
        print(f"{self.name} is running")

    def say(self):
        print(f'{self.name} is saying')

    def __getattribute__(self, *args, **kwargs):
        if args[0] in ["age", "weight"]:
            raise TypeError("不能被访问")
        return object.__getattribute__(self, *args, **kwargs)

    def __getattribute__(self, *args, **kwargs):
        if args[0] in ["run", "say"] and self.func_lock:
            pwd = input("请输入密码进行验证")
            if pwd == self.pwd:
                print("验证成功")
                self.func_lock = False
            else:
                print("验证失败")
                raise TypeError("不能被访问")
        return object.__getattribute__(self, *args, **kwargs)

p1 = Person("0001", "小明", 18, 65)
print(p1.name)
# print(p1.age)
p1.say()
p1.run()
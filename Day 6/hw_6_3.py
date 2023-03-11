# 3.	编写程序, A 继承了 B, 俩个类都实现了 handle 方法, 在 A 中的 handle 方法中调用 B 的 handle 方法

class B:
    def __init__(self):
        print("B init")
    def handle(self):
        print("B handle")

class A(B):
    def __init__(self):
        print("A init")
    def handle(self):
        super().handle()

a = A()
a.handle()
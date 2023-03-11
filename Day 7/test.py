class A:
    def __init__(self, a):
        self.a = a
        print("A")


class B(A):
    def __init__(self, b, a):
        self.b = b
        print("B")
        super().__init__(a)


class C:
    def __init__(self, c):
        self.c = c
        print("C")


class D(B, C):
    def __init__(self, a, b, c, d):
        print("D")
        self.d = d
        super().__init__(a, b)

d = D(1, 2, 3 ,4)

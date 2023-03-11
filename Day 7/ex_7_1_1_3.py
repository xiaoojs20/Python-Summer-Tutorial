class IntList(list):
    def __init__(self, item, tag=False):
        super().__init__(item)
        self.tag = tag

    def append(self, obj):
        if not isinstance(obj, int):
            raise TypeError('must be int')
        super().append(obj)

    @property
    def mid(self):
        index = len(self) // 2
        return self[index]

    def clear(self):
        if not self.tag:
            raise PermissionError
        super().clear()


l = IntList([1, 2, 3, 4])
print(l)
l.append(5)
print(l)
# l.append('11')
print(l.mid)
l.insert(0, -123)
print(l)
# l.clear()
# print(l)

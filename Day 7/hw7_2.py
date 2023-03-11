class MyBTree:
    def __init__(self, root):
        self.__root = root
        self.node_list = []
        self.now_node = self.__root
        self.visited = []

    def add_node(self, node):
        self.node_list.append(node)
        print(f'add {node.name}')

    def find_node(self, node, style="wfs"):
        if style == "wfs":
            self.__find_node_wfs(node)
        elif style == "dfs":
            self.__find_node_dfs(node)
        else:
            raise ValueError("请选择正确的搜索方法")

    def __find_node_wfs(self, node):
        if not self.__root:
            print("空树")
        else:
            node_queue = [self.__root]
            while True:
                if node_queue[0].left:
                    node_queue.append(node_queue[0].left)
                if node_queue[0].right:
                    node_queue.append(node_queue[0].right)
                print(node_queue[0].name)
                node_queue.remove(node_queue[0])
                if len(node_queue) == 0:
                    print("can find it")
                    break
                if node_queue[0] == node:
                    print(node_queue[0].name)
                    break

    def __find_node_dfs(self, node):
        if not self.__root:
            print("空树")
        else:
            if self.now_node is not None and self.now_node not in self.visited:
                print(self.now_node.name)
                self.visited.append(self.now_node)
            if self.now_node.name == "I":
                return

            if self.now_node.left is not None and self.now_node.left not in self.visited:
                self.now_node = self.now_node.left
                self.__find_node_dfs(self.now_node)
            elif self.now_node.right is not None and self.now_node.right not in self.visited:
                self.now_node = self.now_node.right
                self.__find_node_dfs(self.now_node)
            else:
                self.now_node = self.now_node.parent
                self.__find_node_dfs(self.now_node)


class MyBNode:
    def __init__(self, name, value, parent, left, right):
        self.__value = value
        self.__parent = parent
        self.__left = left
        self.__right = right

        if not isinstance(name, str):
            raise ValueError('name must be a string!')
        self.name = name

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        for idx in range(len(val)):
            if (not isinstance(val[idx], int)) and (not isinstance(val[idx], float)):
                raise ValueError("value must be an int/float")
        else:
            self.__value = val

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, val):
        self.__parent = val

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, val):
        self.__left = val

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, val):
        self.__right = val


A = MyBNode("A", 0, None, None, None)
B = MyBNode("B", 0, A, None, None)
C = MyBNode("C", 0, A, None, None)
D = MyBNode("D", 0, B, None, None)
E = MyBNode("E", 0, B, None, None)
F = MyBNode("F", 0, C, None, None)
H = MyBNode("H", 0, C, None, None)
I = MyBNode("I", 0, E, None, None)
A.left = B
A.right = C
B.left = D
B.right = E
C.left = F
C.right = H
E.right = I

tree = MyBTree(A)
tree.add_node(B)
tree.add_node(C)
tree.add_node(D)
tree.add_node(E)
tree.add_node(F)
tree.add_node(H)
tree.add_node(I)

tree.find_node(H, "wfs")
tree.find_node(I, "dfs")

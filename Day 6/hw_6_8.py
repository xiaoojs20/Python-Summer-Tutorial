# 8.	自定义类，实现二叉树（BNode、BTree），支持的功能：
# 	给定一个树，定位某一个节点。
# 	给定某一个节点，找上级节点，形成一个列表[从上级节点，一直到根节点]
# 	从给定的节点找子节点，返回一个列表[左节点、右节点]
# 	判断某一个节点是否另外一个节点的下级节点。

class BTree:
    def __init__(self, tree):
        self.tree = tree

    def find_parent(self,node):
        self.end = False
        while True:
            for i in range(len(self.tree)):
                if self.tree[i][node] == 1:
                    print(f"{node}的上级节点是{i}")
                    node = i
                    self.end = True
                    break
            else:
                break

    def find_son(self,node):
        son = []
        for i in range(len(self.tree)):
            if self.tree[node][i] == 1:
                son.append(i)
        if len(son) == 0:
            print(f'{node}没有子节点')
        if len(son) == 1:
            print(f'{node}的子节点只有{son[0]}')
        else:
            print(f'{node}的子节点为{son}')
        return son


a_tree =[[0,1,1,0,0,0,0,0],[0,0,0,1,1,0,0,0],[0,0,0,0,0,1,1,0],[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

t = BTree(a_tree)
t.find_parent(7)
t.find_son(1)

class Node:#创建节点
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def __repr__(self):
        return f'{self.data}'

class TreeNode(object):#创建树
    def __init__(self):
        self.root = None

    def insert(self, x):#创建方法
        node = Node(x)

        if self.root is None:
            self.root = node

        else:
            temp = [self.root]
            while True:
                a = temp.pop(0)
                if a.left is None:
                    a.left = node
                    return
                elif a.right is None:
                    a.right = node
                    return
                else:
                    temp.append(a.left)
                    temp.append(a.right)
    def get_parent(self,item):#找到父节点
        if self.root.data == item:
            return None
        temp = [self.root]
        while temp:
            p = temp.pop(0)
            if p.left.data == item:
                return p
            if p.right.data == item:
                return p
            if p.left:
                temp.append(p.left)
            if p.right:
                temp.append(p.right)
        return None

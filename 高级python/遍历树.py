from pprint import pformat
from queue import Queue

class Node:  # 创建节点
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.value)
        return pformat({"%s" % (self.value): (self.left, self.right)}, indent=1)


class Bst:  # 创建 树 BinarySearhTree

    def __init__(self):
        self.root = None  # 定义根节点

    def __str__(self):
        return str(self.root)
    def PreOrderTraverse(self, node):  # 前序
        if node is None:
            return None
        print(node.value)
        self.PreOrderTraverse(node.left)
        self.PreOrderTraverse(node.right)

    def PreOrderTraverse1(self, node):  # 前序 递归方法
        stack = [node]
        while len(stack) > 0:
            print(node.value)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            node = stack.pop()

    def inorderstack(self, node):  # 中序
        stack = []
        while node or len(stack) > 0:
            while node:
                stack.append(node)
                node = node.left
            if len(stack) > 0:
                node = stack.pop()
                print(node.value)
                node = node.right
    def post_order_stack(self,node):#后序
        if node is None:
            return False
        stack1 = []
        stack2 = []
        stack1.append(node)
        while stack1:#找出后序遍历的逆序存放在stack2
            node = stack1.pop()
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
            stack2.append(node)
        while stack2:#倒着输出stack2
            print(stack2.pop().value,end=' ')
    def c_order(self,node):#层序遍历 数组
        if self.root is None:
            raise IndexError('空树')
        else:
            a = [node]
            while a:
                node = a.pop(0)
                print(node.value)
                if node.left:
                    a.append(node.left)
                if node.right:
                    a.append(node.right)
    def c2_order(self,node):#层次遍历 队列
        if self.root is None:
            raise IndexError('空树')
        else:
            a = Queue()
            a.put(node)
            while a:
                node = a.get()
                print(node.value)
                if node.left:
                    a.put(node.left)
                if node.right:
                    a.put(node.right)




    def remove(self, value):
        node = self.seach(value)
        if node is not None:
            if node.left is None and node.right is None:
                self.__reassign_nodes(node, None)
            elif node.left is None:
                self.__reassign_nodes(node, node.right)
            elif node.right is None:
                self.__reassign_nodes(node, node.left)
            else:
                temp = self.getmax(node.left)
                self.remove(temp.value)
                node.value = temp.value

    def __reassign_nodes(self, node, new_node):
        if new_node is not None:
            new_node.parent = node.parent
        if node.parent is not None:
            if self.isright(node):
                node.parent.right = new_node
            else:
                node.parent.left = new_node
        else:
            self.root = new_node

    def seach(self, value):
        if self.isempty():
            raise IndexError('kong')
        else:
            temp = self.root
            while value != temp.value:
                if value < temp.value:
                    temp = temp.left
                else:
                    temp = temp.right
        return temp

    def getmax(self, node):
        if node is None:
            node = self.root
        if not self.isempty():
            while node.right is not None:
                node = node.right
        return node

    def getmin(self, node):
        if self.isempty():
            raise IndexError('kong')
        if not self.isempty():
            while node.left is not None:
                node = node.left

    def isright(self, node):
        if node.parent.right == node:
            return True
        return False

    def isleft(self, node):
        if node.parent.left == node:
            return True
        return False

    def isempty(self):
        if self.root is None:
            return True
        return False

    def insert(self, value):
        node = Node(value, None)
        if self.isempty():
            self.root = node
        else:
            temp = self.root
            while True:
                if value < temp.value:
                    if temp.left is None:
                        temp.left = node
                        break
                    else:
                        temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = node
                        break
                    else:
                        temp = temp.right
            node.parent = temp




b = Bst()
b.insert(8)
b.insert(3)
b.insert(1)
b.insert(6)
b.insert(10)
# b.remove(2)
# b.PreOrderTraverse1(b.root)
# b.post_order_stack(b.root)
# b.c_order(b.root)
b.c2_order(b.root)
# print(b)




from pprint import pformat
class Node:#创建节点
    def __init__(self,value,parent):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None


    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.value)
        return pformat({"%s" % (self.value): (self.left, self.right)}, indent=1)
class Bst:#创建 树 BinarySearhTree

    def __init__(self):
        self.root = None
       #定义根节点
    def __str__(self):
        return str(self.root)
    def remove(self, value):
        node =self.seach(value)
        if self.root is None:
            raise   IndexError('空树')
        else:
            if node.left is None and node.right is None:
                self.__reassign_nodes(node,None)
            elif node.left is None:
                self.__reassign_nodes(node,node.right)
            elif node.right is None:
                self.__reassign_nodes(node,node.left)
            else:
                temp = self.getmax(node.left)
                self.remove(temp)
                node.value = temp.value



    def __reassign_nodes(self,node,new_node):
        if node.parent is not Node:
            new_node.parent = node.parent
        if node is not Node:
            if self.isleft(node):
                node.parent.left = new_node
            if self.isright(node):
                node.parent.right =new_node



        
    def seach(self, value):
        if self.root is None:
            raise IndexError('空树')
        else:
            temp = self.root
            while temp:
                if value < temp.value:
                    temp = temp.left
                else:
                    temp = temp.right
            return temp



    def getmax(self, node):
        if node is None:
            node = self.root
        if not self.isempty():
            while node.right:
                node = node.right
            return node


    def getmin(self, node):
        if node is None:
            node = self.root
        if not self.isempty():
            while node.left:
                node = node.left
            return node



    def isright(self, node):
        if node == node.parent.right:
            return True
        return False



    def isleft(self, node):
        if node == node.parent.left:
            return True
        return False


    def isempty(self):
        if self.root is None:
            return True
        return False


    def insert(self,value):
        node  = Node(value)
        if self.root is None:
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




    def PreOrderTraverse(self, node):#前序
        if  node is None:
            return None
        print(node.value)
        self.PreOrderTraverse(node.left)
        self.PreOrderTraverse(node.right)
    def PreOrderTraverse1(self,node):#前序 递归方法
        stack = [node]
        while len(stack) > 0 :
            print(node.value)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            node = stack.pop()
    def inorderstack(self,node):#中序
        stack = []
        while node or len(stack) > 0:
            while node:
                stack.append(node)
                node = node.left
            if len(stack) > 0:
                node =stack.pop()
                print(node.value)
                node = node.right











b = Bst()
b.insert(8)
b.insert(3)
b.insert(1)
b.insert(6)
b.insert(10)
# b.remove(2)
b.PreOrderTraverse1(b.root)
print(b)




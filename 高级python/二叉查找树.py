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
        self.root = None #定义根节点
    def __str__(self):
        return str(self.root)
    def is_empty(self):
        return True if self.root is None else False
    def insert(self,value): #创建方法
        node = Node(value,None)# 创建新节点
        if self.root is None: #判断树是否为空
            self.root = node
        else:
            parent_node = self.root #从根节点查找
            while True:#循环查找
                if value < parent_node.value:#如果插入值小于父节点的值
                    if parent_node.left is None:#如果左节点为空
                        parent_node.left = node#左结点赋值
                        break#退出循环
                    else:
                        parent_node = parent_node.left#父节点下移
                elif value >= parent_node.value:#如果插入值大于等于父节点的值
                    if parent_node.right is None:#如果右节点为空
                        parent_node.right = node#右节点赋值
                        break#退出循环
                    else:
                        parent_node = parent_node.right#父节点下移

    def insert_list(self,list):
        for i in list:
            self.insert(i)
        return self
    def search(self,value): #查找值在二叉树的位置
        if self.root is None:
            return '空树'
        else:
            node = self.root
            while node and node.value != value:
                if value < node.value:
                    node = node.left
                elif value > node.value:
                    node = node.right
            print(node)
            return node
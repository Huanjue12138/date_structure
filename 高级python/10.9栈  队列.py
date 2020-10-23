# class Stack:
#     def __init__(self,data):
#         self.stack = []
#         self.size = 0
#     def push(self,data):
#         self.stack.append(data)
#         self.size += 1
#     def pop(self):
#         if self.stack:
#             temp = self.stack.pop()
#             self.size -= 1
#             return temp
#         else:
#             raise IndexError('6666')
#
#     def peek(self): # 返回栈顶
#         if self.stack:
#             return self.stack[-1]
#     def is_empty(self): #判断列表是否为空
#         return not bool(self.stack)
#     def size(self): #返回列表有效数据
#         return self.size
#     def __str__(self):
#         return str(self.stack)
# a = Stack(10)
# a.push(1)
# a.push(1)
# a.push(1)
# a.push(1)
# a.push(1)
# a.push(1)
# a.pop()
# print(a)





class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.size = 0
    def __repr__(self):
        return f'{self.data}'

class linksatck:
    def __init__(self):
        self .top = None
        self.size = 0
    def push(self,data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self .size += 1

    def pop(self):
        if self.top is None :
            raise Exception('空栈')
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp
        self.size -= 1
    def __repr__(self):
        temp = self.top
        result = ''
        while temp:
            result += f'{temp}-->'
            temp = temp.next
        return result + '-->end'

ll = linksatck()
ll.push(1)
ll.push(1)
ll.push(1)
ll.push(1)
ll.push(1)
ll.push(1)
ll.pop()
print(ll)


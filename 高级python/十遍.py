# class Node :
#     def __init__(self,data,next=None):
#         self.data = data
#         self.next = None
#
#     def __repr__(self):
#         return 'node({})'.format(self.data)
# class linklist :
#     def __init__(self):
#         self.head = None
#
#     def add_head(self, data):
#         node1 = Node(data)
#         if self.head :
#            node1.next = self.head
#         self.head=node1
#
#
#
#     def add_last(self,data):
#         node = Node(data)
#
#         if self.head:
#             temp = self.head
#             while temp.next:
#                 temp = temp.next
#             temp.next = node
#         else :
#             self.add_head()
#     def __repr__(self):
#         star = self.head
#         str = ''
#         while star:
#             str += '{}-->'.format(star)
#             star = star.next
#         return str + 'end'
#
#     def add_i (self,i,data):
#         node = Node(data)
#
#         if self.head :
#             temp = self.head
#             if i ==1 :
#                 self.head = node
#             else:
#                 j = 1
#                 pre = temp
#                 while j < i :
#                     pre = temp.next
#                     temp = pre.next
#                 node = pre
#                 node.next = temp
#     def add_list(self,object:list):
#         self.head = Node(object[0])
#         temp = self.head
#         for i in object[1:] :
#             node = Node(i)
#             temp.next = node
#             temp = temp.next
#     def del_star(self):
#         temp = self.head
#         if  self.head is None :
#             return '链表为空'
#         else :
#             self.head = temp.next
#
#     def del_last(self):
#         temp = self.head
#         if self.head:
#             if self.head.next is None:
#                 self.head = None
#             while  temp.next.next:
#                 temp = temp.next
#             temp.next = None
#         else :
#             return '链表为空'
# object = [0,1,2,3,4,5,6]
# ll = linklist()
# ll.add_list(object)
# # ll.add_head(1)
# # ll.add_head(2)
# # ll.add_head(3)
# # ll.add_head(4)
# # ll.add_head(5)
# # ll.add_last(6)
# # ll.del_star()
# ll.del_last()
# print(ll)
#
#
class Node : #建立节点
    def __init__(self,data,next=None):
        self.data = data
        self.next = None
    def __repr__(self):
        return'node({})'.format(self.data)


class linklist : #建立链表
    def __init__(self):
         self.head = None #第一个节点默认为空

    def add_star(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
        self.head = new_node

    def add_last(self,data):
        node1 = Node(data)
        if self.head:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node1
        else:
            self.add_star(data)
    def __repr__(self):
        star = self.head
        str = ''
        while star:
            star = star.next
            str += '{}-->'.format(star)
        return str+'end'
    def add_i(self,i,data):
        node1 = Node(data)
        if self.head :
            if i == 1:
                self.head.next = node1
            else:

                temp2 = self.head
                temp1 = temp2
                j = 1
                while j < i :
                    temp1 = temp2.next
                    temp2 = temp1.next
                temp1.next = node1
                node1.next = temp2
    def del_star(self,data):
        if self.head:
            self.head.next = self.head
        else:
            return '空链表'
    def del_last(self):
        if  self.head:
            temp = self.head
            while temp.next.next:
                temp = temp.next
            temp.next = None
        else:
            return '空链表'
    def add_list(self,object:list):

        self.head = Node(object[0])
        temp = self.head
        for i in object[1:]:
            node1 = Node(i)
            temp.next = node1
            temp = temp.next
ll = linklist()
# object = [0,1,2,3,4,5]
# ll.add_list(object)
ll.add_last(1)
print(ll)







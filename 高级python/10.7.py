class Node :
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return "Node({})".format(self.data)

class linklist :
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    def get (self,index):
        current = self.head
        for _ in range(1, index):
            current = current.next
        return current

    def insert(self,index,data):
        new_node = Node(data)
        if index<0 or index > self.size:
            raise Exception('索引越界')
        if self.size == 0:#链表为空
            self.head = new_node
            self.tail = new_node
            self.size += 1
        elif index == 0:#头部插入

            new_node.next = self.head
            self.head = new_node
            self.size += 1
        elif index == self.size:#尾部插入

            self.tail.next = new_node
            self.tail = new_node
            self.size += 1
        else:#自定义插入

            perv = self.get(index-1)
            new_node.next = perv.next
            perv.next = new_node
            self.size += 1

    def __repr__(self):
            start = self.head
            str1 = ''
            while start:
                str1 += f"{start} -> "
                start =start.next
            return str1 + 'end'

    def remove(self,index):
        if index < 0 or index >= self.size:
            raise Exception('索引越界')
        if index == 0 :
            # remove_node = self.head
            self.head = self.head.next
            # remove_node.next = None

        elif index == self.size:#删除末尾
            prev = self.get(index-1)
            prev.next = None
            self.tail = prev
        else:               #删除中间
            perv = self.get(index - 1)
            curr = perv.next.next
            perv.next = curr
        self.size -= 1


    def overturn(self):#反转列表
        if self.size > 0 :
            curr = self.head
            per = None
            while curr:
                node = curr.next
                curr.next =per
                per = curr
                curr = node
            self.head = per




ll = linklist()
ll.insert(0,1)
ll.insert(1,2)
ll.insert(2,3)
ll.insert(3,4)
ll.insert(4,5)
# ll.remove(4)
# print(ll.size)
ll.overturn()
print(ll)

class Node:

    def __init__(self, data):
        self.data = data

        self.next = None

    def __repr__(self):
        return f"Node({self.data})"

class LinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index):
        #需要找到链表头
        curr = self.head
        #已知次数适合使用for循环
        for _ in range(1, index):
            curr = curr.next
        return curr

    def insert(self, index, data):
        new_node = Node(data)
        if index < 0 or index > self.size:
            raise Exception("索引越界")
        else:
            #当链表为空
            if self.size == 0 :
                self.head = new_node
                self.tail = new_node
            #在头部插入
            elif  index == 0 :
                new_node.next = self.head
                self.head = new_node
            #在尾部插入
            elif index == self.size:
                self.tail.next = new_node
                self.tail = new_node
            #在中间插入
            else:
                prev = self.get(index-1)
                new_node.next = prev.next
                prev.next = new_node
            self.size += 1

    def remove(self, index):
        if index <0 or index >= self.size:
            raise Exception('索引越界')
        #删除头部
        if index == 0:
            remove_node = self.head
            self.head = self.head.next
            remove_node.next = None
        #删除尾部
        elif index ==  self.size - 1 :
            prev = self.get(index -1)
            remove_node = prev.next
            prev.next = None
            self.tail = prev
        else:
            prev = self.get(index -1 )
            remove_node = prev.next
            prev.next = prev.next.next
        self.size -=1
        return remove_node

        #输出链表
    def __repr__(self):
        cursor = self.head
        result = ""
        while cursor:
            result += f"{cursor} -> "
            cursor = cursor.next
        return result + "end"
#
#
# ll = LinkList()
# ll.insert(0,1)
# ll.insert(1,2)
# ll.insert(2,3)
# ll.insert(3,4)
# ll.remove(2)
#
# print(ll)
class Node :
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"Node({self.data})"

class linklist :
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    def get(self, index):
                #需要找到链表头
        curr = self.head
                #已知次数适合使用for循环
        for _ in range(1, index):
                    curr = curr.next
        return curr

    def insert(self,index,data):
        new_node = Node(data)
        if index < 0 or index > self.size:
            raise  Exception('索引越界') #判断索引是否越界
        if self.size == 0:#链表为空
            self.head = new_node
            self.tail = new_node
        elif index == 0:                 #增加头结点

            new_node.next = self.head
            self.head = new_node
        elif index == self.size:    #增加尾节点
            self.tail.next = new_node
            new_node = self.tail.next
            self.tail = new_node

        else :
            perv = self.get(index-1)
            new_node.next = perv.next
            perv.next = new_node
        self.size += 1
    def remove(self,index):
        if index < 0 or index >= self.size:
            raise Exception('索引越界')
        if index ==0:
            self.head = self.head.next
        elif index == self.size:
            perv = self.get(index-1)
            perv.next = None
        else:
            perv = self.get(index-1)
            curr = perv.next.next
            perv.next = curr
        self.size -= 1
    def __repr__(self):
        node = self.head
        result = ''
        while node :
            result = result + f' Node({node.data})'
            node = node.next
        return  result + ' end'

    def overturn(self):  # 反转列表

        if self.size > 0 :
                curr = self.head
                per = None
                while curr:
                    node = curr.next
                    curr.next =per
                    per = curr
                    curr = node
                self.head = per

    def deget(self, index): # 查询倒数
        self.overturn()
        return self.get(index)

ll = linklist()
ll.insert(0,1)
ll.insert(1,2)
ll.insert(2,3)
ll.insert(3,4)
ll.insert(4,5)
# ll.remove(4)


print(ll.deget(2))
























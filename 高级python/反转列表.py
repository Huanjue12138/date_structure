class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return'node({})'.format(self.data)


class linklist:
    def __init__(self):
        self.head = None   #指向头结点即该链表第一个节点

    def insert_head(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
        self.head = new_node

    def append(self, data):
        node = Node(data)
        if self.head:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
        else:
            self.insert_head()

    def __repr__(self):
        star = self.head
        str = ''
        while star:
            str += '{} -->'.format(star)
            star = star.next
        return str + 'End'

    def insert_i(self, i, data):
        if self.head is None :
            self.insert_head()
        elif i==1 :
            self.insert_head()
        else :
            temp = self.head
            j=1
            pre = temp
            while j<i :
                pre = temp
                temp = temp.next
                j+=1
            node = Node(data)
            pre.next = node
            node.next = temp
    def list_link (self,object:list) :
        self.head = Node(object[0])
        temp = self.head
        for i in object[1:] :
            node = Node(i)
            temp.next = node
            temp = temp.next
    def del_head(self):
        temp = self.head
        if self.head:
            self.head = temp.next
        temp.next = None
    def del_last(self):
        temp = self.head
        if self.head :
            if self.head.next is None:
                self.head = None
            else :
                while temp.next.next:
                    temp = temp.next
                temp.next = None
        else:
            return '链表为空'
    def fanzhuan (self):  #链表反转

        curr = self.head
        perv = None
        while curr:
            node = curr.next
            curr.next = perv
            perv = curr
            curr = node
        self.head = perv
    def __getitem__(self, index): #查询
        current = self.head
        if current is None :
            return '空链表'

        else:
            for _ in range(1,index) :
                if current.next is None:
                    return '查询不在链表内'
                current = current.next
            return current
    def __set__(self,index,data):  #更改
        current = self.head
        if current is None:
            return '空链表'
        else:
            for _ in range(1,index):
                if current.next is None:
                    return '不在链表内'
                current = current.next
            current.data = data




ll = linklist()
ll.insert_head(1)
ll.insert_head(2)
ll.insert_head(3)
ll.insert_head(4)
ll.fanzhuan()
print(ll.__set__(3,4))


print(ll)
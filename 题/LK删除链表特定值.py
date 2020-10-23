class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f'Node({self.data})'
class linklist:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
    def pop_val(self,val):
        temp = self.head
        per = self.head
        while temp.next.data != val:
            temp = temp.next
        else:
            per = temp
            temp = temp.next
            per.next = temp.next




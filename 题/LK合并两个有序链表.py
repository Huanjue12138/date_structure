class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        while l1 or l2 :
            while l2.val < l1.val :
                  curr.next = ListNode(l2.val)
                  curr = curr.next
            else :
                curr.next = ListNode(l1.val)
                curr = curr.next
            if l1 == None:
                curr.next = l2
                break
            if l2 == None:
                curr.next = l1
                break
    def mergetwolists2 (self,l1,l2):
        dummy = ListNode(0)
        curr = dummy
        while l1 and l2:
            if l1 > l2:
                curr.next = ListNode(l2.val)
                curr = curr.next
            else:
                curr.next = ListNode(l1.val)
                curr = curr.next
        if l1 == None:
            curr.next = l2
        if l2 == None:
            curr.next = l1

class Stack_node:
    def __init__(self):
        self.top = None
        self.size = 0
    def push(self,data):
        node =  ListNode(data)
        if self.top is None:
            self.top = node
        else :
            node.next = self.top
            self.top = node
    def pop(self):
        if self.top is None:
            raise IndexError('空栈')
        else:
            self.top = self.top.next

class stack_list:
    def __init__(self):
        self.stack = []
        self.size = 0
    def push(self,data):
        if self.size == 0:
            self.stack[0] = data
        else:
            self.stack.append(data)



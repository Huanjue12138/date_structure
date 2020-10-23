class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f'Node({self.data})'
def is__H(head):
    solw = head
    fast = head
    while fast and fast.next :
        fast = fast.next.next
        solw = solw.next
        if fast == solw:
            return True
    return False
if __name__=='__main__':
     node1 =Node(1)
     node2 =Node(2)
     node3 =Node(3)
     node4 =Node(4)
     node5 =Node(5)
     node6 =Node(6)
     node7 =Node(7)

     node1.next = node2
     node2.next = node3
     node3.next = node4
     node4.next = node5
     node5.next = node6
     node6.next = node7
     node7.next = node5
def  H(head):
    solw = head
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        solw = solw.next
        if fast == solw:
            break
    solw = head
    while fast != solw:
        solw = solw.next
        fast = fast.next
    return solw

print(H(node1))
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        dummy = None
        dummy.next = head
        per = head
        while per.next and per.next.next:
            solw = per
            fast = per.next
            per.next = fast.next
            fast.next = solw
            per.next = fast
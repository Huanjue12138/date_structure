class LNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# 判断链表是否有环,并返回入环节点
# 判断是否有环，用快指针和慢指针，当两个指针相遇时，说明有环
    def exit_loop(LList):
        p1 = p2 = LList
        # 当链表为空或者只有一个节点时，跳出循环，返回False
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                return True
        return False

    # 如果链表有环，返回入环节点
    # 当确定有环后，慢指针重新回到头节点，快指针停留在相遇处，然后两个指针每次移动1个节点，最终他们在入环节点处相遇
    def find_entry_of_loop(pHead):
        if not pHead:
            return None
        slow = pHead
        fast = pHead

        while slow.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            # 当两个指针相遇时，说明有环，循环结束
            if fast == slow:
                break

        # 快指针停留在相遇处，慢指针回到起点
        if not fast or not fast.next:
            return None
        slow = pHead

        # 两个指针每次向前移动1，当再次相遇时，相遇点即为入环节点
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
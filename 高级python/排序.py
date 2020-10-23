# from rangdomlist import randomlist
#
#
#
# #冒泡排序
# def mp(nums):
#     for i in range(len(nums)-1):
#         print('第%s轮结果'%i,nums)
#         for j in range(len(nums)-1-i):
#             if nums[j] > nums[j+1]:
#                 nums[j],nums[j+1] = nums[j+1],nums[j]
#     return nums
#
#
# #选择排序
# def xp(nums):
#     for i in range(1,len(nums)):
#         print('第%s轮结果' % i, nums)
#         for j in range(i+1,len(nums)):
#             if nums[i] > nums[j]:
#                 nums[i],nums[j] = nums[j],nums[i]
#     return nums
#
# b = randomlist.slist(20)
# a = [5,4,3,2,1]
# print(mp(a))
# print(xp(b))
#
# def cp(nums):
#     if len(nums) <= 1:
#         return nums
#     for right in range(1,len(nums)):
#         taget = nums[right]
#         for left in range(right):
#             if nums[left] > taget:
#                nums[left+1:right+1] = nums[left:right]
#                nums[left] = taget
#                break
#     return nums

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f'node{self.data}-->'
class Nodelist:
    def __init__(self):
        self.head = None
        self.size = None
        self.total = None
    def px(self,head):
        dummy = Node(0)
        per = dummy
        curr = self.head
        while curr is not None:
            temp = curr
            while per.next is not None and per.next.data < curr.data:
                per = per.next
            curr.next = per.next
            per.next = curr
            curr = temp
            per = dummy
        return dummy.next

Node(5).next = Node(4)
Node(4).next = Node(8)
Node(8).next = Node(1)
Node(1).next = Node(7)

n = Nodelist()
print(n.px(Node(5)))









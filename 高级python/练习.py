# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
# 说明：
#
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
# 示例：
#
# 输入：
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# 输出：[1,2,2,3,5,6]
# class Solution(object):
    # def merge(self, nums1,m, nums2,n):#最简单的方法合并后排序
    #     nums1[:] = sorted(nums1[:m] + nums2)
    #     return nums1
    # def merge(self, nums1,m, nums2,n):#双指针
    #     nums1_copy = nums1[:m]
    #     p1 = 0
    #     p2 = 0
    #     nums1[:] = []
    #     while p1 < m and p2 < n:
    #         if nums1_copy[p1] < nums2[p2] :
    #             nums1.append(nums1_copy[p1])
    #             p1 += 1
    #         else:
    #
    #             nums1.append(nums2[p2])
    #             p2 += 1
    #     if p1 < m:
    #         nums1[p1+p2:] = nums1_copy[p1:]
    #     if p2 < n:
    #         nums1[p1+p2:] = nums2[p2:]
    #     return nums1
# s = Solution()
# nums1 = [1,2,3,0,0,0]
# nums2 = [2,5,6]
# print(s.merge(nums1,3,nums2,3))

#数组实现二叉查找树
# class List_tree:
#     def __init__(self, size):
#         self.tree = [None] * size  # 没有元素的都为None
#
#
#     def __len__(self):
#         return len(self.tree)
#
#
#     def __str__(self):
#         return str(self.tree)
#     #查找
#     def isExist(self,v,root=0):   #目标元素大于父亲 往右边找 小于父亲往左边找
#         while self.tree[root]!=None:
#             if self.tree[root]==v:
#                 return True
#             if self.tree[root]>v:
#                 root=root*2+1
#             else:
#                 root = root*2+2
#         return False
#     #删除
#     def _findMin(self, root=0):  # 找最左边的
#         if self.tree[root * 2 + 1] == None:
#             return root
#         return self._findMin(root * 2 + 1)

# class List:
#     def overturn(self,nums):
#         nums = nums[::-1]
#         return nums
# l = List()
# a = [1,2,3,4]
# print(l.overturn(a))
# b = []
# b = sorted(a)
# b.append(1)
# b.append(a[-2])
# b.append(a[-3])
# print(b)

# 题给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍
def liangshuzhihe(nums,target):
    head = 0
    end = len(nums)-1
    while head  < end:
        sum = nums[head] + nums[end]
        if sum ==target:
            print(head,end)
            head += 1
            end -= 1
        else :
            if sum < target:
                head += 1
            elif sum > target:
                end -= 1
def liang2(nums,target):
    count = len(nums)
    for i in range(count):
        for j in range(i+1,count):
            if nums[i] + nums[j] == target:
                return [i,j]
    return
def liang3(nums,targe):
    a = {}
    for i in range(len(nums)):
        c = targe - nums[i]
        if c in a :
            return
        else:
            a[nums[i]] = i









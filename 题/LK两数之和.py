# 1 题给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/two-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# class Solution(object):#暴力破解  时间复杂度 O(n^2)
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         count = len(nums)
#         for i in range(count):
#             for j in range(i+1,count):
#                 if nums[i] + nums[j] == target:
#                     return [i,j]
#         return []  #为什么要返回[]
# class Solution(object):# 有序列表
#     def twosum(self,nums,target):#对撞指针
#         head = 0
#         end = len(nums)-1
#         while head < end:
#             sum = nums[head] + nums[end]
#             if sum == target:
#                 print(head,end)
#                 head += 1
#                 end -= 1
#             else:
#                 if sum < target:
#                     head += 1
#                 else :
#                     end -= 1
# def twosum(self,nums,p):#字典存放
#     c = {}
#     for i in range(len(nums)):
#         temp = p - nums[i]
#         if temp in c:
#             print([i,c[temp]])
#         else :
#             c[nums[i]] = i
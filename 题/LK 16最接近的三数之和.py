# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
# 示例：
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。

class Solution(object):
    def threeSumClosest(self, nums, target):
        a = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                for o in range(len(nums)):
                    if i != j != o:
                        b = nums[i]+nums[j]+nums[o]




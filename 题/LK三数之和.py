#15 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/3sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# class Solution(object):
#     def threeSum(self, nums):
#         for i in nums:
#             for j in nums:
#                 for o in nums:
#                     if i + j + o == 0 and i != j != o:
#                         print(i, j, o)
# nums = [-1, 0, 1, 2, -1, -4]
# s = Solution()
# s.threeSum(nums)

class Solution(object):

    def threeSum(self, nums):
        res = []
        for i in range(len(nums)-1):
            if i >0 and nums[i] ==nums[i+1]:
                continue
            left = i + 1
            right = len(nums)-1
            while left < right:
                if nums(left) + nums(right) + nums[i] == 0:
                    res += [[nums[i],nums[left],nums[right]]]
                    left += 1
                    right -= 1
                elif nums(left) + nums(right) + nums[i] < a:
                    left += 1
                else:
                    right += 1
            while nums[left] == nums[left+1]:
                left += 1
            while nums[right] == nums[right+1]:
                right += 1
nums = [-1, 0, 1, 2, -1, -4]
s = Solution()
s.threeSum(nums)



class Solution(object):
    def removeElement(self, nums, val):
        solw = 0
        fast = 1
        while fast < len(nums):
            if nums[fast] != nums[solw]:
                solw += 1
                nums[solw] = nums[fast]
                fast += 1
            else:
                fast += 1
        return solw +1

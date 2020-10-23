class Solution(object):
    def moveZeroes(self, nums):

        solw = 0
        fast = 0
        if nums is None:
            raise IndexError('666')
        while fast < len(nums):
            if nums[fast] == 0:
                fast += 1
            else:
                nums[solw] = nums[fast]
                solw += 1
                fast += 1
        for i in range(solw,len(nums)):
            nums[i] = 0
        return nums
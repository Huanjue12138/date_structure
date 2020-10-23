class Solution(object):
    def removeDuplicates(self, nums):
        slow = 0
        fast = 1
        if nums is not None:
            while fast < len(nums):
                if nums[fast] == nums[slow]:
                    slow += 1
                    fast += 1

            new_num = []
            for i in range(slow):
                new_num[i] = nums[i]

            nums = new_num
        else:
            raise IndexError('空列表')
        return nums

    def removeDuplicates1(self, nums):
        fast = 1
        solw = 0
        while fast < len(nums) :
            if nums[solw] != nums[fast]:
                solw += 1
                nums[solw] = nums[fast]
                fast += 1
            else:
                fast += 1
        return solw + 1






























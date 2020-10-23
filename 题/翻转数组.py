#用对撞指针
def rever(nums):
    solw = 0
    fast = len(nums) - 1
    if len(nums) == 0:
        raise IndexError('kong')
    else:
        while solw < fast:
            nums[solw], nums[fast] = nums[fast], nums[solw]
            solw += 1
            fast -= 1
    return nums
a = [1,2,3,4,5,6,7,8,9]
print(rever(a))
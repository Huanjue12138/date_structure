# 给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。
#
# 示例 1:
#
# 输入: [2,2,3,4]
# 输出: 3
# 解释:
# 有效的组合是:
# 2,3,4 (使用第一个 2)
# 2,3,4 (使用第二个 2)
# 2,2,3
def tirangle(nums):
    nums = sorted(nums)
    right = len(nums)-1
    count = 0
    for i in range(len(nums)-2):
        left = i + 1
        if nums[i] + nums[left] > nums[right] and nums[right] + nums[left] > nums[i] and nums[i] + nums[right] > nums[i]:
            count += 1


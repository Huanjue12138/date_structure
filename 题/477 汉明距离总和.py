# 两个整数的 汉明距离 指的是这两个数字的二进制数对应位不同的数量。
#
# 计算一个数组中，任意两个数之间汉明距离的总和。
#
# 示例:
#
# 输入: 4, 14, 2
#
# 输出: 6
#
# 解释: 在二进制表示中，4表示为0100，14表示为1110，2表示为0010。（这样表示是为了体现后四位之间关系）
# 所以答案为：
# HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
#
def totalHammingDistance(self, nums):
    return sum((b.count('0') * b.count('1')) for b in zip(*map('{:032b}'.format, nums)))

class Solution:#双重循环
    def totalHammingDistance(self, nums: List[int]) -> int:
        # 计算每两个数的汉明距离
        def distance(a,b):
            c=a^b
            count=0
            while c:
                c&=c-1
                count+=1
            return count

        n=len(nums)
        res=0
        for i in range(n-1):
            for j in range(i+1,n):
                res+=distance(nums[i],nums[j])
        return res

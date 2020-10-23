# 5 最长回文子串 :给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
# 示例 1：输入: "babad"输出: "bab"注意: "aba" 也是一个有效答案。
# 示例 2：输入: "cbbd"  输出: "bb"
def Hw(a):
    solw = 0
    fast = 1
    b = ''
    c = ''
    while fast < len(a):
        if a[solw-1] == a[fast]:
            b += a[solw -1] + a[solw] + a[fast]
        elif a[solw] == a[fast]:
            c += a[solw] + a[fast]
        if len(b) < len(c):
            d = c
            c = ''
        elif len(c) < len(b):
            d = b
            b = ''
        solw += 1
        fast += 1
    return d
a = 'babad'
# 输出结果 'aba'
print(Hw(a))

# 2 颜色分类:给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
#
# 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
#
# 注意:
# 不能使用代码库中的排序函数来解决这道题。
#
# 示例:
#
# 输入: [2,0,2,1,1,0]
# 输出: [0,0,1,1,2,2]
def YF(nums):
    a = []
    b = []
    c = []
    for i in nums:
        if i == 0:
            a.append(i)
        if i == 1:
            b.append(i)
        if i == 2:
            c.append(i)
    return a + b + c
a = [2,0,2,1,1,0]
print(YF(a))
#结果 [0, 0, 1, 1, 2, 2]

# 3 合并辗转相除法 和 更相减损法 !!!!没思路

# __init__.py 控制着包的导入行为。假如 __init__.py 为空，那么仅仅导入包是什么都做不了的
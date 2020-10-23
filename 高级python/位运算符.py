# def count(n):
#     o = 0
#     while n!= 0:
#         n = n & (n-1)
#         o += 1
#     print(o)
# n = int('000000001011', 2)
# # count(n)
#
# from typing import List
#
#
# def justone(nums:List[int]):
#     res = 0
#     for i in nums:
#         res = res ^ i
#     return res
# n = [1,2,3,4,5,6]
# justone(n)


def hammingDistance(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    return bin(x^y).count('1')
hammingDistance(1,4)

# a =1
# b =4
# # a = a<<1
# # print(a)
# count = 0
# while a != b:
#     a = a << 1
#     count += 1
# print(count)
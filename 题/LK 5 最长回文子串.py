# 5 最长回文子串 :给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
# 示例 1：输入: "babad"输出: "bab"注意: "aba" 也是一个有效答案。
# 示例 2：输入: "cbbd"  输出: "bb"
def centerSpread(strs, left, right):
    i = left
    j = right
    lenth = len(strs)
    while i > 0 and j < lenth:
        if strs[i] == strs[j]:
            i -= 1
            j += 1
        else:
            break
    return strs[i+1:j]
def Hw(strs):
    length = len(strs)
    if length < 2:
        return strs
    maxlen = 1
    res = strs[0]
    for i in range(length-1):
        odd = centerSpread(strs,i,i)
        even = centerSpread(strs,i,i+1)
        maxstr = odd if len(odd) > len(even)else even
        if len(maxstr) > maxlen:
            maxlen = len(maxstr)
            res = maxstr
    return res
def hw2(strs):
    for i in range(len(strs),-1,-1):
        for j in range(len(strs)-i-1):
            sub_str = strs[j,i+j]
            if sub_str == sub_str[::-1]:
                return sub_str

class Solution:
    def longestPalindrome(self, s: str) -> str:
        for length in range(len(s), -1, -1):
            for index in range(0, len(s) - length + 1):
                sub_string = s[index:length + index]
                if sub_string == sub_string[::-1]:
                    return sub_string





a = 'dabadaaabbbaaa'
# 输出结果 'aba'
print(hw2(a))



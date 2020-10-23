# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
# 说明：
#
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
# 示例：
#
# 输入：
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3

# 输出：[1,2,2,3,5,6]
class Solution(object):
    def merge(self, nums1,m, nums2,n):#最简单的方法合并后排序
        nums1[:] = sorted(nums1[:m] + nums2)
        return nums1
    # def merge(self, nums1,m, nums2,n):#双指针
    #     nums1_copy = nums1[:m]
    #     p1 = 0
    #     p2 = 0
    #     nums1[:] = []
    #     while p1 < m and p2 < n:
    #         if nums1_copy[p1] < nums2[p2] :
    #             nums1.append(nums1_copy[p1])
    #             p1 += 1
    #         else:
    #
    #             nums1.append(nums2[p2])
    #             p2 += 1
    #     if p1 < m:
    #         nums1[p1+p2:] = nums1_copy[p1:]
    #     if p2 < n:
    #         nums1[p1+p2:] = nums2[p2:]
    #     return nums1
    def merge2(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
            elif nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            


s = Solution()
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
print(s.merge(nums1,3,nums2,3))
# def quick_sort(alist, first, last):
#     """快速排序"""
#
#
#     if first >= last:
#         return
#     else:
# # n = len(alist)
#         mid_value = alist[first]
#     low = first
#     high = last
#     while low < high:
# # high 左移
#         while low < high and alist[high] >= mid_value:
#             high -= 1
#         else:
#             alist[low],alist[high] = alist[high],alist[low]
# # low += 1 # 加上后high和low会在中间位置处错过
# # low 右移
#         while low < high and alist[low] < mid_value:
#             low += 1
#         else:
#             alist[high],alist[low] = alist[low],alist[high]
# # high -= 1 # 加上后high和low会在中间位置处错过
# # 从循环退出时，low == high
#     else:
#         alist[low] = mid_value
# # 对low左边的列表执行快速排序
#     quick_sort(alist, first, low - 1)
# # 对low右边的列表排序
#     quick_sort(alist, low + 1, last)
# # if __name__ == "__main__":
# #     li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# #     print(li)
# #     n = len(li)
# #     quick_sort(li, first=0, last=n - 1)
# #     print(li)
#
# def quicksort(nums, start, end):
#     if len(nums) < 2 :
#         return nums
#     mid = start
#     left = start
#     right = end
#     while left <= right:
#         while nums[left] > nums[mid] :
#             nums[left], nums[right] = nums[right], nums[left]
#         else:
#             left += 1
#         while nums[right] < nums[mid]:
#             nums[left], nums[right] = nums[right], nums[left]
#         else:
#             right -= 1
#         nums[left],nums[mid] = nums[mid],nums[left]
#     quicksort(nums,start,left-1)
#     quick_sort(nums,left,end)
#
# def quicksort1(nums,start,end):
#     if start >= end:
#         return
#     else:
#         pivo = nums[start]
#     solw = start
#     fast = end
#     while solw < fast:
#         while solw < fast and nums[solw] < pivo:
#             solw += 1
#         else:
#             nums[solw],nums[fast] = nums[fast],nums[solw]
#         while solw < fast and nums[fast] > pivo:
#             fast -= 1
#         else:
#             nums[solw],nums[fast] = nums[fast],nums[solw]
#     else:
#         nums[solw] = pivo
#     quicksort1(nums,start,solw-1)
#     quicksort1(nums,solw+1,end)
#
# if __name__ == '__main__':
#     a = [7, 2, 5, 4, 6, 1, 9]
#     quicksort1(a,0,6)
#     print(a)


def countsort(nums):
    max = 0
    for i in nums:
        if i > max:
            max = i
    a = [0 for i in range(max+1)]
    b = []
    for i in nums:
        a[i] += 1
    for i in a :
        while a[i] > 0:
            b.append(i)
            a[i] -= 1




if __name__ == '__main__':
    a = [1,1,2,2,5,6,6,7,9,9,9]
    countsort(a)
    print(a)


class trilnode:
    def __init__(self):
        self.data = {}
        self.is_word = False
    def __repr__(self):
        return str(self.data)
class tril:
    def __init__(self):
        self.root = trilnode()
    def insert(self,val):
        node = self.root
        for char in val:
            child = node.data.get(char)
            if child is None:
                node.data[char] = trilnode
            node = node.data[char]
        node.is_word = True

















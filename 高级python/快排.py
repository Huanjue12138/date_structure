def swap(ilist, p, q):
    return ilist[p],ilist[q] == ilist[q],ilist[p]

def partition(ilist,start,end):
    pivot = ilist[start]
    p = start + 1
    q = end
    while p <= q :
        while p <= q and ilist[p] < pivot:
            p += 1
        while p <= q and ilist[q] >pivot:
            q -= 1
        if p < q:
            swap(ilist,p,q)
    swap(ilist,start,q)
    return q
def partition1(nums,start,end):
    left = start + 1
    right = end
    while left<= right:
        while left<= right and nums[left]<nums[start]:
            left += 1
        while left<= right and nums[right]>=nums[start]:
            right -= 1
        if left<right:
            nums[left],nums[right] = nums[right],nums[left]
    nums[start],nums[right] = nums[right],nums[start]
    return right

def quickSort(nums,start,end):
    if start>=end:
        return
    mid = partition(nums,start,end)
    partition(nums, start, mid-1)
    partition(nums, mid+1,end)
    return nums




def quicksort(array):
    if len(array) < 2 :
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


def quick_sort(alist, start, end):
    """快速排序"""


# 递归的退出条件
    if start >= end:
        return
# 设定起始元素为要寻找的基准元素
    mid = alist[start]
# left为序列左边的由左向右移动的游标
    left = start
# right为序列右边的由右向左移动的游标
    right = end
    # while left < right:
# 如果left与right未重合，right指向的元素不比基准元素小，则right向左移动
    while left < right and alist[right] >= mid:
        right -= 1
# 将right指向的元素放到left的位置上
        alist[left] = alist[right]
# 如果left与right未重合，left指向的元素比基准元素小，则left向右移动
    while left < right and alist[left] < mid:
        left += 1
# 将left指向的元素放到right的位置上
        alist[right] = alist[left]
# 退出循环后，left与right重合，此时所指位置为基准元素的正确位置
# 将基准元素放到该位置
    alist[left] = mid
# 对基准元素左边的子序列进行快速排序
    quick_sort(alist, start, left - 1)
# 对基准元素右边的子序列进行快速排序
    quick_sort(alist, left + 1, end)
if __name__ == '__main__':
    lis = [8, 5, 7, 4, 2, 9, 12]
    quick_sort(lis, 0, 6)
    print(lis)






from typing import List


def merge(left, right):#传统
    a = []
    while left and right:
        if left[0] > right[0]:
            a.append(right.pop(0))
        else:
            a.append(left.pop(0))
    while left:
        a.append(left.pop(0))
    while right:
        a.append(right.pop(0))
    return a


def  mergesort(nums:List[int]):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left,right = nums[0:mid],nums[mid:]
    return merge(mergesort(left),mergesort(right))

def merge1(left,right):#双指针
    solw = 0
    fast = 0
    a = []
    while solw < len(left) and fast <len(right) :
        if left[solw] < right[fast]:
            a.append(left[solw])
            solw += 1
        else:
            a.append(right[fast])
            fast += 1
    a.extend(left[solw:])
    a.extend(right[fast:])
    return a

if __name__ == '__main__':
    a = [1,5,6,4,9,3,7,2,8]
    print(mergesort(a))
def partition(nums,start,end):
    pivot = nums[start]
    mark = start
    for i in range(start+1,end+1):
        if nums[i] <pivot :
            mark += 1
            nums[mark],nums[i] = nums[i],nums[start]
    nums[start] = nums[mark]
    nums[mark] = pivot
    return mark
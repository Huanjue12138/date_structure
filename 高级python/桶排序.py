def bucksort(nums):
    max_val = max(nums)
    min_val = min(nums)
    d = max_val - min_val
    #初始化桶
    bucket_num = len(nums) #桶数
    count_list = [] # 放置桶的空间
    for i in range(bucket_num):# 造桶
        count_list.append([])
    #往桶里填数据
    for i in range(len(nums)):
        num = int((nums[i]-min_val)*(bucket_num-1)/d)
        bucket = count_list[num]
        bucket.append(nums[i])
    #桶内排序
    for i in range(len(count_list)):
        count_list[i].sort()
    sort = []
    #输出数据
    for sub in count_list:
        for item in sub:
            sort.append((item))
    return sort
if __name__ == '__main__':
    a = [4.5,0.84,3.25,2.18,0.5]
    print(bucksort(a))
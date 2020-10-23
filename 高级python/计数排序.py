# coding = utf-8
import random
import sys

# 选择排序
list = []


# 随机生成列表
def generate():
    n = int(input("请输入本次排序数字个数："))
    while n > 0:
        list.append(random.randint(0, 10))
        n -= 1
    print("生成的数字列表如下：%s" % list)


# 计数排序
def countSort(markList):
    max = 0
    for value in markList:#遍历
        if value > max:
            max = value#找到最大数值
    countList = [0 for i in range(max + 1)] #依靠最大数值建数组
    printList = [] #准备空数组存放输出值
    for value in markList:# 遍历
        countList[value] += 1 #计数
    for i in range(len(countList)): #遍历计数列表
        while countList[i] > 0:# 输出I 次 数值
            printList.append(i)#结果添加到 输出列表
            countList[i] -= 1


def main():
    global list


generate()
list = countSort(list)
print("计数排序后数字列表如下：%s" % list)
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.stderr.write("退出\n")
        sys.exit(0)
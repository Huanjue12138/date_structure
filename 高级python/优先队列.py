class Dtree():
    def __init__(self):
        self.list = []
        self.size = 0

    def insert(self,data):
        self.list.append(data)
        index = len(self.list) - 1
        parent = self.getparent(index)
        while parent is not None and self.list[parent] < self.list[index]:
            self.swap(parent,index)
            index = parent
            parent = self.getparent(index)

    def getparent(self, index):
        if index == 0 or index > len(self.list) - 1:
            return None
        else:
            return (index - 1) >> 1

    def swap(self, indexa, indexb):  # 交换值
        self.list[indexa], self.list[indexb] = self.list[indexb], self.list[indexa]
    def xs(self):
        child_index = self.size-1
        parent_index = (child_index - 1)>>1
        new = self.list[child_index]
        while child_index > 0 and new >self.list[parent_index]:
            self.list[child_index] =self.list[parent_index]
            child_index = parent_index
            parent_index = (child_index - 1)>>1
        self.list[child_index] = new
    def enqueue(self,value):
        self.list.append(value)
        self.size += 1
        self.xs()
    def dequeue(self):
        if self.size <= 0:
            raise Exception("队列为空")
        remove_data = self.list[0]
        self.list[0] = self.list[-1]
        del self.list[-1]
        self.size -= 1
        self.dequeue()
        return remove_data

    def heapify_down(self):  # 向下堆化
        index = 0
        maxIndex = index
        while True:
            if 2 * index + 1 < self.size and self.list[2 * index + 1] > self.list[maxIndex]:
                maxIndex = 2 * index + 1
            if 2 * index + 2 < self.size and self.list[2 * index + 2] > self.list[maxIndex]:
                maxIndex = 2 * index + 2
            if maxIndex == index:
                break
            self.swap(index, maxIndex)
            index = maxIndex
class dui():
    def __init__(self):
        self.datalist = []
    def getparent(self,index):
        if index == 0 or index > len(self.datalist)-1:
            return None
        else:
            return (index - 1) >> 1
    def swap(self,indexa,indexb):
        self.datalist[indexa],self.datalist[indexb] = self.datalist[indexb] , self.datalist[indexa]
    def insert(self,data):
        self.datalist.append(data)
        index = len(self.datalist) - 1
        parent = self.getparent(index)
        while parent is not None and self.datalist[parent] < self.datalist[index]:
            self.swap(parent,index)
            index = parent
            parent = self.getparent(index)

    def D_pop(self):#删除
        pop_node = self.datalist[0]
        self.datalist[0] = self.datalist[-1]
        del self.datalist[-1]
        self.heapify(0)
        return pop_node

    def heapify(self, index):
        max_index = index
        total_index = len(self.datalist) - 1
        while True:
            if 2*index +1 <= total_index and self.datalist[2*index +1] > self.datalist[max_index]:
                max_index = 2*index + 1
            if 2*index +2 <= total_index and self.datalist[2*index +2] > self.datalist[max_index]:
                max_index = 2*index + 2
            if index == max_index:
                break
            self.swap(index,max_index)
            index = max_index




d = dui()
d.insert(5)
d.insert(3)
d.insert(6)
d.insert(9)
d.D_pop()
print(d.datalist)



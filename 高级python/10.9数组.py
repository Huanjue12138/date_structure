class Array:
    def __init__(self,capacity):
        self.array = [None] * capacity
        self.size = 0
    def insert(self,index,elment):
        if index < 0 :
            raise IndexError('索引越界')
        if self.size >= len(self.array) or index >= len(self.array) :
            self.addcapacity()
        for i in range(self.size-1,index-1,-1):
                self.array[i+1] = self.array[i]
        self.array[index] = elment
        self.size += 1

    def remove(self, index):
        if index < 0 :
            raise IndexError('索引越界')
        for i in range(index-1, len(self.array)):
            self.array[i] = self.array[i + 1]
        self.size -= 1

    def output(self):
        for i in  range(self.size):
            if i is not None:
                print(self.array[i],end='->')


    def addcapacity(self):
        new_array = [None] * len(self.array) * 2
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
    

# if __name__ == '_main_':
array = Array(4)
array.insert(0,1)
array.insert(1,2)
array.insert(2,3)
array.insert(3,4)
# array.insert(2,2)
array.remove(2)
# print(array.size)
print(array.array)

# SyntaxError: invalid syntax
#                ^
#     if nums[i] = val:
# Line 10  (Solution.py)




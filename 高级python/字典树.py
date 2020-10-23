class Trienode:
    def __init__(self):
        self.data = {}
        self.is_word = False

    def __repr__(self):
        return str(self.data)


class Trie:
    def __init__(self):
        self.root = Trienode()

    def insert(self, word):
        node = self.root
        for char in word:
            child = node.data.get(char)
            if child is None:
                node.data[char] = Trienode()
            node = node.data[char]
        node.is_word = True

    def insert1(self, word):
        node = self.root  # 插入节点时从根节点开始判断，根节点是一个空字典

        for char in word:
            child = node.data.get(char)
            if child is None:  # 判断当前节点有没有该元素，如果没有就增加节点
                node.data[char] = Trienode()  # 本级字典添加新的字典
            node = node.data[char]  # 判断节点下移

        node.is_word = True  # 最底层的node

    def seach(self, word):#查找
        node = self.root
        for char in word:
            node = node.data.get(char)
            if not node:
                return False
        return node.is_word

    def startwith(self, word):
        node = self.root
        for char in word:
            node = node.data.get(char)
            if not node:
                return False
        return True


if __name__ == '__main__':
    t = Trie()
    t.insert('helloword')
    t.insert('helloaaaa')
    t.insert('hellobbbb')
    t.insert('hellocccc')
    print(t.root.data)


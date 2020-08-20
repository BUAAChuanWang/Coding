'''
实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

示例:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");
trie.search("app");     // 返回 true
'''


class Trie(object):
    # https://leetcode.com/problems/implement-trie-prefix-tree/discuss/58834/AC-Python-Solution
    # 评论区好解法！
    def __init__(self):
        self.end = False
        self.c = {}  # c就是children，里面每个都是Trie结构体类型的变量

    def insert(self, word):
        node = self
        for w in word:
            if w not in node.c:
                node.c[w] = Trie()
            node = node.c[w]
        node.end = True

    #  单独多写一个获得某个前缀的最后一个node的函数
    def prefixnode(self, word):
        node = self
        for w in word:
            if w not in node.c:
                return None
            node = node.c[w]
        return node

    def search(self, word):
        node = self.prefixnode(word)
        if not node:
            return False
        else:
            return True if node.end else False

    def startsWith(self, prefix):
        node = self.prefixnode(prefix)
        return bool(node)
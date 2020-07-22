# https://leetcode-cn.com/problems/design-hashset/
class Node:
    def __init__(self, val, nex=None):
        self.val = val
        self.next = nex


class Bucket:
    def __init__(self):
        self.head = Node(0)

    def contains(self, key):
        cur = self.head.next
        while cur:
            if cur.val == key:
                return True
            cur = cur.next
        return False

    def insert(self, key):
        if self.contains(key):
            return
        cur = Node(key)
        cur.next = self.head.next
        self.head.next = cur

    def remove(self, key):
        pre, cur = self.head, self.head.next
        while cur:
            if cur.val == key:
                pre.next = cur.next
                break
            pre, cur = pre.next, cur.next


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashkey = 2069
        self.hashset = [Bucket() for _ in range(self.hashkey)]

    def add(self, key: int) -> None:
        self.hashset[key % self.hashkey].insert(key)

    def remove(self, key: int) -> None:
        self.hashset[key % self.hashkey].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        res = self.hashset[key % self.hashkey].contains(key)
        return res

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
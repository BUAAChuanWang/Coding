# https://leetcode-cn.com/problems/lru-cache/
class DueListNode:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashlist = {}
        self.head = DueListNode(0, 0)
        self.tail = DueListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, key):
        node = self.hashlist[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        self.hashlist.pop(key)
        node.next = None
        node.prev = None
        # print("remove", "key=",key,self.hashlist)

    def add(self, key, node):
        self.hashlist[key] = node
        # print("add","key=",key,self.hashlist)
        tmp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = tmp
        tmp.prev = node

    def get(self, key: int) -> int:
        if key in self.hashlist:
            node = self.hashlist[key]
            self.remove(key)
            self.add(key, node)
            # print("get","key=",key,self.hashlist[key].v)
            return self.hashlist[key].v
        else:
            # print("get","key=",key,"-1")
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashlist:
            self.remove(key)
        node = DueListNode(key, value)
        self.add(key, node)
        if len(self.hashlist) > self.capacity:
            last = self.tail.prev.k
            self.remove(last)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
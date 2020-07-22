'''
请你为 最不经常使用（LFU）缓存算法设计并实现数据结构。它应该支持以下操作：get 和 put。
get(key) - 如果键存在于缓存中，则获取键的值（总是正数），否则返回 -1。
put(key, value) - 如果键已存在，则变更其值；如果键不存在，请插入键值对。当缓存达到其容量时，则应该在插入新项之前，使最不经常使用的项无效。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除最久未使用的键。
「项的使用次数」就是自插入该项以来对其调用 get 和 put 函数的次数之和。使用次数会在对应项被移除后置为 0 。

进阶：
你是否可以在 O(1) 时间复杂度内执行两项操作？

示例：
LFUCache cache = new LFUCache( 2 /* capacity (缓存容量) */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回 1
cache.put(3, 3);    // 去除 key 2
cache.get(2);       // 返回 -1 (未找到key 2)
cache.get(3);       // 返回 3
cache.put(4, 4);    // 去除 key 1
cache.get(1);       // 返回 -1 (未找到 key 1)
cache.get(3);       // 返回 3
cache.get(4);       // 返回 4
'''


# https://leetcode-cn.com/problems/lfu-cache/solution/lfuhuan-cun-by-leetcode-solution/ 思路来源 代码自己写的
# 双哈希+双链表实现：一个哈希hashmap跟LRU一样，记录key的，key:Node
# 另一个哈希是frequency是按按频率存放双向链表的 freq:List。
class DueNode:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.count = 0
        self.next = None
        self.prev = None


# 双链表的功能与LRU一模一样
class DueList:
    def __init__(self):
        self.length = 0
        self.head = DueNode(None, None)
        self.tail = DueNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def pop(self):
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        self.length -= 1

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.length -= 1

    def push(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        self.length += 1


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.frequency = collections.defaultdict(DueList)
        self.min_freq = float("inf")  # 记录最小频率的

    # 每次get都要对存在的节点的count+1， 然后把count之前的值从frequency中删除同时判断删除后是否为空，如果为空就从frequency字典中删除这个双链表同时min_freq+1
    def get(self, key: int) -> int:
        if self.capacity == 0: return -1
        if key in self.hashmap:
            node = self.hashmap[key]
            # print("before:", node.key, node.val, node.count)
            self.frequency[node.count].remove_node(node)
            if self.min_freq == node.count and self.frequency[node.count].length == 0:
                self.min_freq = node.count + 1
            if self.frequency[node.count].length == 0:
                self.frequency.pop(node.count)
            node.count += 1
            self.frequency[node.count].push(node)
            # print("after:", node.key, node.val, node.count)
            return node.val
        return -1

    # 每次put如果已存在，那么就只需要从frequency字典中删除原count的节点并判断是否为空，如果为空就min_freq+1，
    # 否则先看是否超过容积，如果超过容积，先删除min_freq的最不常用节点，然后判断是否frequency中min_freq对应双向链表是否为空，为空就删除。然后新加入新节点此时min_freq=1。
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return
        if key in self.hashmap:
            node = self.hashmap[key]
            self.frequency[node.count].remove_node(node)
            if self.min_freq == node.count and self.frequency[node.count].length == 0:
                self.min_freq = node.count + 1
            node.count += 1
            node.val = value
            self.frequency[node.count].push(node)

        elif key not in self.hashmap:
            if self.capacity == len(self.hashmap):
                node = self.frequency[self.min_freq].head.next
                self.hashmap.pop(node.key)
                self.frequency[self.min_freq].pop()
                if self.frequency[self.min_freq].length == 0:
                    self.frequency.pop(self.min_freq)
            self.min_freq = 1
            node = DueNode(key, value)
            node.count += 1
            self.hashmap[key] = node
            self.frequency[node.count].push(node)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
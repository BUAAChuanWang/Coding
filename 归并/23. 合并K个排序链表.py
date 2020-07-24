'''

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 归并
        def merge(l1, l2):
            if not l1: return l2
            if not l2: return l1
            if l1.val < l2.val:
                l1.next = merge(l1.next, l2)
                return l1
            else:
                l2.next = merge(l1, l2.next)
                return l2

        def mergesort(lists, l, r):
            if l >= r:
                return lists[l]
            mid = l + (r - l) // 2
            l1 = mergesort(lists, l, mid)
            l2 = mergesort(lists, mid + 1, r)
            l = merge(l1, l2)
            return l

        if not lists: return []
        res = mergesort(lists, 0, len(lists) - 1)
        return res


        # 优先队列 nlogk
        import heapq
        head = ListNode(0)
        p = head
        priority = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(priority, (lists[i].val, i))
                lists[i] = lists[i].next
        while priority:
            val, idx = heapq.heappop(priority)
            p.next = ListNode(val)
            p = p.next
            if lists[idx]:
                heapq.heappush(priority, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return head.next
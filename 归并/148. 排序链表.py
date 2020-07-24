'''
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:

输入: 4->2->1->3
输出: 1->2->3->4
示例 2:

输入: -1->5->3->4->0
输出: -1->0->3->4->5
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 递归归并排序 但不是真正的O1空间 因为有递归栈
        def merge(l1, l2):
            if not l1: return l2
            if not l2: return l1
            if l1.val < l2.val:
                l1.next = merge(l1.next, l2)
                return l1
            else:
                l2.next = merge(l1, l2.next)
                return l2

        def mergesort(head):
            if not head.next:
                return head
            slow, fast = head, head
            pre = ListNode(0)
            pre.next = slow  # pre用来记录slow的前一个节点 然后割断前面和后面两个子链表
            while fast and fast.next:
                slow, fast = slow.next, fast.next.next
                pre = pre.next
            pre.next = None  # 割断
            l1, l2 = head, slow
            l1 = mergesort(l1)
            l2 = mergesort(l2)
            l = merge(l1, l2)
            return l

        if not head: return None
        dummy = mergesort(head)
        return dummy

        # 迭代 自己写的 真O1空间
        cur, length = head, 0
        while cur: length, cur = length + 1, cur.next
        res = ListNode(0)
        res.next = head
        intv = 1
        while intv < length:
            pre, cur = res, res.next
            while cur:
                h1, i = cur, intv
                while cur and i:
                    cur, i = cur.next, i - 1
                len1 = intv - i

                h2, i = cur, intv
                while cur and i:
                    cur, i = cur.next, i - 1
                len2 = intv - i
                # O1空间 merge
                while len1 and len2:
                    if h1.val <= h2.val:
                        pre.next = h1
                        pre = pre.next
                        h1 = h1.next
                        len1 -= 1
                    elif h1.val > h2.val:
                        pre.next = h2
                        pre = pre.next
                        h2 = h2.next
                        len2 -= 1
                while len1:
                    pre.next = h1
                    pre = pre.next
                    h1 = h1.next
                    len1 -= 1
                while len2:
                    pre.next = h2
                    pre = pre.next
                    h2 = h2.next
                    len2 -= 1
                pre.next = cur
            intv *= 2
        return res.next

        '''
        # 递归 自己写的     归并排序的变种 但不是O1空间 因为有递归栈
        def merge(l1, l2):
            if not l1 or not l2:
                return l1 or l2
            pre = ListNode(0)
            head = pre
            while l1 and l2:
                if l1.val <= l2.val:
                    pre.next = l1
                    pre = l1
                    l1 = l1.next 
                elif l1.val > l2.val:
                    pre.next = l2
                    pre = l2
                    l2 = l2.next
            if l1:pre.next = l1 
            if l2:pre.next = l2
            return head.next

        def mergesort(head):
            if not head or not head.next:
                return head
            slow, fast = head, head.next
            while fast and fast.next:
                slow, fast = slow.next, fast.next.next
            tail = slow.next    # 别忘了这两行
            slow.next = None
            l1 = mergesort(head)
            l2 = mergesort(tail)
            return merge(l1, l2)

        return mergesort(head)
        '''

        '''#别人的代码
        h, length, intv = head, 0, 1
        while h: h, length = h.next, length + 1
        res = ListNode(0)
        res.next = head

        while intv < length:
            pre, h = res, res.next
            while h:
                h1, i = h, intv
                while i and h: h, i = h.next, i - 1
                if i: break # no need to merge because the `h2` is None.

                h2, i = h, intv
                while i and h: h, i = h.next, i - 1
                c1, c2 = intv, intv - i # the `c2`: length of `h2` can be small than the `intv`.

                while c1 and c2: # merge the `h1` and `h2`.
                    if h1.val < h2.val: pre.next, h1, c1 = h1, h1.next, c1 - 1
                    else: pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2

                while c1 > 0 or c2 > 0: pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h 
            intv *= 2
        return res.next
        '''
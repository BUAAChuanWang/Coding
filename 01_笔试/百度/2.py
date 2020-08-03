'''
{1,2,3,4,5},2,4

{1,4,3,2,5}
'''

#class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
# 返回反转的链表
# @param head ListNode类 输入链表
# @param m int整型 m
# @param n int整型 n
# @return ListNode类
#
class Solution:
    def reverseBetween(self , head , m , n ):
        # write code here
        if not head: return None
        if m == n: return head
        i = 1
        h1, h2 = None, None
        tail1, tail2 = None, None

        cur = head
        while i < m:
            tail1 = cur
            cur = cur.next
            i += 1
        if m == 1:
            tail1 = None
        else:
            tail1.next = None
        h1 = cur

        pre, dummy = None, h1
        count = 0
        while count < n - m + 1:
            t = dummy.next
            dummy.next = pre
            pre = dummy
            dummy = t
            count += 1
        if m != 1:
            tail1.next = pre
        elif m == 1:
            head = pre
        h1.next = dummy
        return head

# 翻转链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverse(self, head):
    if not head or not head.next:return head
    pre, cur = None, head
    while cur:
        t = cur.next
        cur.next = pre
        pre = cur
        cur = t
    return pre
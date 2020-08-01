'''
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1:

给定链表 1->2->3->4, 重新排列为 1->4->2->3.
示例 2:

给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 空间O1
        # 1.链表快慢指针找中心
        # 2.原地反转后半段 ：翻转链表
        # 3.然后前后两端逐个插入  ：归并排序链表的merge的改变（递归merge）
        if not head: return None
        if not head.next: return head

        def findcenter(head):  # 快慢指针找中心
            slow, fast = head, head.next
            while fast and fast.next:
                slow, fast = slow.next, fast.next.next
            head2 = slow.next
            return slow, head2

        pre, head2 = findcenter(head)
        pre.next = None  # 断开前后链接

        def reverse(head):  # 原地反转链表
            pre, cur = None, head
            while cur:
                t = cur.next
                cur.next = pre
                pre = cur
                cur = t
            return pre

        head2 = reverse(head2)

        def merge(l1, l2, count):  # 递归合并两个链表
            if not l1: return l2
            if not l2: return l1
            if count % 2 == 0:
                l1.next = merge(l1.next, l2, count + 1)
                return l1
            else:
                l2.next = merge(l1, l2.next, count + 1)
                return l2

        head = merge(head, head2, 0)
        return head

        # 递归超时
        def rec(head):
            if not head: return None
            nex = head.next
            pre, cur = ListNode(None), head
            pre.next = cur
            while cur.next:
                cur, pre = cur.next, pre.next
            if head == pre:
                return head
            head.next = cur
            pre.next = None
            cur.next = rec(nex)
            return head

        rec(head)
        return head
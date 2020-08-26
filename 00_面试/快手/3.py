# coding=utf-8
import sys

# str = input()
# print(str)
print('Hello,World!')


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = [6, 3, 9, 1, 4, 8, 10, "#", 2, "#", 5, 7]
root = [str(x) for x in root]


def helper(idx):
    global root
    if idx - 1 >= len(root): return None
    cur = TreeNode(root[idx - 1]) if root[idx - 1] != "#" else None
    if not cur: return
    cur.left = helper(2 * idx)
    cur.right = helper(2 * idx + 1)
    return cur


cur = helper(1)


def func(root):
    res = []
    stack = []
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        res.append(root.val)
        root = root.right
    return res


res = func(cur)
print(res)
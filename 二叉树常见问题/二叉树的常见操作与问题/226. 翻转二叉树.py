'''
翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # 非递归
        if not root: return None
        stack = [root]
        while stack:
            cur = stack.pop(0)  # 加不加0都行 层次遍历和先序遍历都无所谓
            cur.left, cur.right = cur.right, cur.left
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return root


        # 递归  自底向上
        if not root: return None
        def helper(root):
            if not root: return None
            root.left, root.right = root.right, root.left
            root.left = helper(root.left)
            root.right = helper(root.right)
            return root
        root = helper(root)
        return root


        # 递归  自顶向下
        if not root: return None
        def helper(root):
            if not root: return None
            root.left, root.right = root.right, root.left
            helper(root.left)
            helper(root.right)
        helper(root)
        return root


        # 自顶向下
        if not root:
            return None
        if not root.left and not root.right:
            return root
        root.left, root.right = root.right, root.left
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        return root
        '''
        # 自底向上
        if not root:
            return None
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.left = right
        root.right = left
        return root
        '''
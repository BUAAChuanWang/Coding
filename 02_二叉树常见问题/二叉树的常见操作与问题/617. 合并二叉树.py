'''
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。

示例 1:

输入:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
输出:
合并后的树:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
注意: 合并必须从两个树的根节点开始。
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # 非递归
        if not t1 and not t2: return None
        if not t1: return t2
        if not t2: return t1
        stack = [(t1, t2)]
        while stack:
            root1, root2 = stack.pop()
            if root1 and root2:
                root1.val += root2.val
                if root1.left and root2.left:
                    stack.append((root1.left, root2.left))
                elif not root1.left:
                    root1.left = root2.left
                if root1.right and root2.right:
                    stack.append((root1.right, root2.right))
                elif not root1.right:
                    root1.right = root2.right
        return t1

        # 递归
        def helper(root1, root2):
            if not root1 and not root2:
                return None
            if not root1:
                return root2
            if not root2:
                return root1

            root1.val = root1.val + root2.val
            root1.left = helper(root1.left, root2.left)
            root1.right = helper(root1.right, root2.right)
            return root1

        root1 = helper(t1, t2)
        return root1
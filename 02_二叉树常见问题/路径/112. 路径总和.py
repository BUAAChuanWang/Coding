'''
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        if not root: return False
        # 非递归
        queue = [(root, root.val, [root])]
        while queue:
            root, summ, path = queue.pop()
            if not root.left and not root.right and summ == target:
                return True
            if root.right:
                queue.append((root.right, summ + root.right.val, path + [root.right]))
            if root.left:
                queue.append((root.left, summ + root.left.val, path + [root.left]))
        return False
        '''
        # 递归
        def helper(root, summ):
            if not root:
                return
            if not root.left and not root.right and summ + root.val == target:
                self.res = True
                return
            helper(root.left, summ + root.val)
            helper(root.right, summ + root.val)
        self.res = False
        helper(root, 0)
        return self.res
        '''
        '''
        # 202002
        def helper(root, cur, sum):
            if not root:
                return False

            if not root.left and not root.right:
                return cur + root.val == sum
            else:
                return helper(root.left, cur + root.val, sum) or helper(root.right, cur + root.val, sum)
        return helper(root, 0, sum)
        '''
        '''
        def helper(root, sum):
            if not root:
                return False
            sum -= root.val
            if not root.left and not root.right:
                return sum == 0
            else:
                return helper(root.left, sum) or helper(root.right, sum)
        return helper(root, sum)
        '''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        def bst_helper(root, target):
            if not root:
                return TreeNode(target)
            if root.val < target:
                root.right = bst_helper(root.right, target)
            elif root.val > target:
                root.left = bst_helper(root.left, target)
            return root
        root = bst_helper(root, val)
        return root
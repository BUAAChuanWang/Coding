# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        # https://labuladong.gitbook.io/algo/shu-ju-jie-gou-xi-lie/er-cha-sou-suo-shu-cao-zuo-ji-jin
        def bst_helper(root, target):
            if not root: return None
            # print(root.val)
            if root.val == target:
                if not root.left and not root.right:
                    return None
                if not root.left:
                    return root.right
                if not root.right:
                    return root.left
                if root.left and root.right:
                    dummy = root.right
                    while dummy.left:
                        dummy = dummy.left
                    dummy.val, root.val = root.val, dummy.val

                    root.right = bst_helper(root.right, dummy.val)
                    return root
            elif root.val > target:
                root.left = bst_helper(root.left, target)
            elif root.val < target:
                root.right = bst_helper(root.right, target)
            return root
        root = bst_helper(root, key)
        return root
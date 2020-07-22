class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.pre_index = 0

    def postorder(self, preorder, inorder):
        if len(preorder) == 0 or len(inorder) == 0 or len(preorder) != len(inorder):return None
        #pre_index = 0
        idx_map = {val:index for index, val in enumerate(inorder)}
        def helper(left_inorder=0, right_inorder=len(inorder)-1):
            if left_inorder > right_inorder:
                return None
            root = TreeNode(preorder[self.pre_index])
            index = idx_map[preorder[self.pre_index]]

            self.pre_index += 1
            root.left = helper(left_inorder, index - 1)
            root.right = helper(index + 1, right_inorder)
            return root
        return helper()

    def postorder(self, preorder, inorder):
        root = TreeNode(preorder[0])


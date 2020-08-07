# https://blog.csdn.net/yangquanhui1991/article/details/52195511
# 类似124
class Solution:
    def maxPath(self, root):
        self.res = float("-inf")
        def helper(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            left_depth = helper(root.left)
            right_depth = helper(root.right)
            cur_depth = left_depth + right_depth
            self.res = max(self.res, cur_depth)
            return max(left_depth, right_depth) + 1
        helper(root)
        return self.res
'''
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

示例 1:

输入: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

输出: 7
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
示例 2:

输入: [3,4,5,1,3,null,1]

     4
    / \
   4   5
  / \   \
 6   3   4

输出: 17
解释: 小偷一晚能够盗取的最高金额 = 6+3+4+4=17
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        # 后序遍历
        # 这个题的后续遍历是可以走重复路径的，就是没有要求是只能走一颗子树，比如从根出发，偷完左子树，还能返回到根再继续偷右子树
        def helper(root):  # 返回每个节点的包含该节点可以偷的最大值  和  不包含这个节点的可以偷的最大值（他的两边的孩子分别可以偷的最大值之和）
            if not root:
                return 0, 0
            left_gain, lchild_gain = helper(root.left)
            right_gain, rchild_gain = helper(root.right)
            root_gain = root.val + lchild_gain + rchild_gain
            child_gain = max(left_gain, lchild_gain) + max(right_gain, rchild_gain)
            return root_gain, child_gain
        if not root: return 0
        self.res = max(helper(root))
        return self.res


        # 20200705 经典后序
        def helper(root):
            if not root:
                return 0, 0
            left_gain, lchild_gain = helper(root.left)
            right_gain, rchild_gain = helper(root.right)
            root_gain = root.val + lchild_gain + rchild_gain
            child_gain = max(left_gain, lchild_gain) + max(right_gain, rchild_gain)
            return root_gain, child_gain
        if not root: return 0
        res = max(helper(root))
        return res

        '''
        def dfs(root):
            # [0][1]分别表示不选和选
            if root == None:
                return (0, 0)
            left = dfs(root.left)
            right = dfs(root.right)
            return (root.val + left[1] + right[1], max(left) + max(right))
        return max(dfs(root))
        '''
        '''
        # 记忆化memo存储结果 
        memo = {}
        def helper(root):
            if not root:
                return 0
            # 记忆化步骤
            if root in memo:
                return memo[root]
            do_rob = root.val + \
                    (helper(root.left.left) + helper(root.left.right) if root.left else 0) + \
                    (helper(root.right.left) + helper(root.right.right) if root.right else 0)
            not_rob = helper(root.left) + helper(root.right)
            res = max(do_rob, not_rob)
            # 记忆化步骤
            memo[root] = res
            return res
        res = helper(root)
        return res
        '''
'''
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]
'''

class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        if not root: return []
        # 非递归
        self.res = []
        queue = [(root, root.val, [root.val])]
        while queue:
            root, summ, path = queue.pop()
            if not root.left and not root.right and summ == target:
                self.res.append(path)
            if root.right:
                queue.append((root.right, summ + root.right.val, path + [root.right.val]))
            if root.left:
                queue.append((root.left, summ + root.left.val, path + [root.left.val]))
        return self.res
        '''
        # 递归
        def helper(root, summ, path):
            if not root:
                return
            if not root.left and not root.right and summ + root.val == target:
                self.res.append(path + [root.val])
            helper(root.left, summ + root.val, path + [root.val])
            helper(root.right, summ + root.val, path + [root.val])
        self.res = []
        helper(root, 0, [])
        return self.res
        '''
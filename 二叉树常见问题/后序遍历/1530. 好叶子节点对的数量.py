'''
给你二叉树的根节点 root 和一个整数 distance 。

如果二叉树中两个 叶 节点之间的 最短路径长度 小于或者等于 distance ，那它们就可以构成一组 好叶子节点对 。

返回树中 好叶子节点对的数量 。

 

示例 1：
输入：root = [1,2,3,null,4], distance = 3
输出：1
解释：树的叶节点是 3 和 4 ，它们之间的最短路径的长度是 3 。这是唯一的好叶子节点对。、
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        if not root or distance < 2: return 0
        # DFS 后序遍历
        def helper(root):   # 返回该节点分别到该节点的子节点的距离
            if not root: return []
            if not root.left and not root.right: return [1]
            left = helper(root.left)
            right = helper(root.right)
            self.res += sum(l + r <= distance for l in left for r in right)
            return [i + 1 for i in left + right if i < distance - 1]    # 剪枝
        self.res = 0
        helper(root)
        return self.res

        # 记录路径 然后找不同
        queue = [(root, [])]
        leaf = []
        while queue:
            cur, step = queue.pop(0)
            if cur.left:
                queue.append((cur.left, step + [0]))
            if cur.right:
                queue.append((cur.right, step + [1]))
            if not cur.left and not cur.right:
                leaf.append(step)
        res = 0
        # print(leaf)
        for i in range(len(leaf)):
            for j in range(i + 1, len(leaf)):
                mini = min(len(leaf[i]), len(leaf[j]))
                for k in range(mini):
                    if leaf[i][k] != leaf[j][k]:
                        if len(leaf[i][k:]) + len(leaf[j][k:]) <= distance: res += 1
                        break
        return res
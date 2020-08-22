'''
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层次遍历如下：

[
  [3],
  [20,9],
  [15,7]
]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        # https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/solution/die-dai-he-di-gui-by-powcai-3/
        # BFS
        if not root: return []
        res = []
        cur_level = [root]
        depth = 0
        while cur_level:
            tmp = []
            next_level = []
            for node in cur_level:
                tmp.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if depth % 2 == 1:
                res.append(tmp[::-1])
            else:
                res.append(tmp)
            depth += 1
            cur_level = next_level
        return res

        # DFS
        res = []
        def helper(root, depth):
            if not root: return
            if len(res) == depth:
                res.append([])
            if depth % 2 == 0:res[depth].append(root.val)
            else: res[depth].insert(0, root.val)
            helper(root.left, depth + 1)
            helper(root.right, depth + 1)
        helper(root, 0)
        return res


        res = []
        cur = [root]
        sign = False   # 设置反转标识
        while cur:
            curr_res = []
            next_node_list = []
            for node in cur:
                if node:
                    curr_res.append(node.val)
                    next_node_list.extend([node.left, node.right])

            if curr_res:
                if sign:
                    curr_res=curr_res[::-1]   #将结果反转，如果为从右到左。
                res.append(curr_res)
            cur = next_node_list
            sign = False if sign else True

        return res
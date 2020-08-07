'''
给定一个二叉树，编写一个函数来获取这个树的最大宽度。树的宽度是所有层中的最大宽度。这个二叉树与满二叉树（full binary tree）结构相同，但一些节点为空。

每一层的宽度被定义为两个端点（该层最左和最右的非空节点，两端点间的null节点也计入长度）之间的长度。

示例 1:

输入:

           1
         /   \
        3     2
       / \     \
      5   3     9

输出: 4
解释: 最大值出现在树的第 3 层，宽度为 4 (5,3,null,9)。
'''
class Solution:
    def widthOfBinaryTree(self, root) -> int:
        # 层次遍历
        queue = [(root, 1, 0)]  # 因为空节点也算宽度，所以用左孩子2x，右孩子2x+1的编号来计算宽度  同时用深度来标记每一层
        depth = 0
        left = 1
        res = float("-inf")
        while queue:
            node, index, step = queue.pop(0)
            if step == depth:
                count = index - left + 1
                res = max(res, count)
            else:
                depth = step
                left = index
                count = 1
                res = max(res, count)
            if node.left:
                queue.append((node.left, 2*index, step + 1))
            if node.right:
                queue.append((node.right, 2*index+1, step + 1))
        return res
        '''
        # BFS 层次遍历
        q = [(root, 0, 1)] # (node, depth, pos)
        cur_depth,left = 0, 1
        res = 0
        while q:
            node, depth, pos = q.pop(0)
            if node:
                q.append((node.left, depth + 1, pos * 2))
                q.append((node.right, depth + 1, pos * 2 + 1))
                if cur_depth != depth:
                    cur_depth = depth
                    left = pos
                res = max(res, pos - left + 1)  
        return res
        '''
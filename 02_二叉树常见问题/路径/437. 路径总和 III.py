'''
给定一个二叉树，它的每个结点都存放着一个整数值。

找出路径和等于给定数值的路径总数。

路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

示例：

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

返回 3。和等于 8 的路径有:

1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        # 原题  递归。 如果打印出来对应的路径就是微软的一个题
        self.res = 0

        def helper(root, sumlist):
            if not root:
                return
            sumlist = [num + root.val for num in sumlist] + [root.val]
            for num in sumlist:
                if num == target:
                    self.res += 1
            helper(root.left, sumlist)
            helper(root.right, sumlist)

        helper(root, [])
        return self.res

        # Microsoft ： 打印路径总和的路径
        if not root: return 0
        # 非递归   不记录具体路径就不会超时
        self.res = 0
        self.path = []
        queue = [(root, [root.val], [[root.val]])]
        while queue:
            root, summ, path = queue.pop()
            for i in range(len(summ)):
                if summ[i] == target:
                    self.res += 1
                    self.path.append(path[i])
            if root.right:
                new_summ = [i + root.right.val for i in summ] + [root.right.val]
                new_path = [i + [root.right.val] for i in path] + [[root.right.val]]
                queue.append((root.right, new_summ, new_path))
            if root.left:
                new_summ = [i + root.left.val for i in summ] + [root.left.val]
                new_path = [i + [root.left.val] for i in path] + [[root.left.val]]
                queue.append((root.left, new_summ, new_path))
        # print(self.path)
        return self.res

        # 递归
        self.res = 0
        self.path = []

        def helper(root, path):
            if not root: return
            path = [i + [root.val] for i in path] + [[root.val]]
            for p in path:
                if sum(p) == target:
                    self.res += 1
                    self.path.append(p)
            helper(root.left, path)
            helper(root.right, path)

        helper(root, [])
        # print(self.path)
        return self.res

        '''
        # 一次递归 + 前缀和
        def dfs(root, sumlist):
            if root is None: return 0
            sumlist = [num + root.val for num in sumlist] + [root.val]
            return sumlist.count(target) + dfs(root.left, sumlist) + dfs(root.right, sumlist)
        return dfs(root, [])
        '''

    '''
    # 暴力递归
        if not root:
            return 0
        def helper(root, sum):
            if not root:
                return 0
            res = 0
            if root.val == sum:
                res += 1         
            res += helper(root.left, sum - root.val)
            res += helper(root.right, sum - root.val)
            return res
        return helper(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
    '''
    '''
    def pathSum(self, root, target):
        # define global result and path
        self.result = 0
        cache = {0:1}

        # recursive to get result
        self.dfs(root, target, 0, cache)

        # return result
        return self.result

    def dfs(self, root, target, currPathSum, cache):
        # exit condition
        if root is None:
            return  
        # calculate currPathSum and required oldPathSum
        currPathSum += root.val
        oldPathSum = currPathSum - target
        # update result and cache
        self.result += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1

        # dfs breakdown
        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)
        # when move to a different branch, the currPathSum is no longer available, hence remove one. 
        cache[currPathSum] -= 1
    '''

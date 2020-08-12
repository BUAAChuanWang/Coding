'''
给定一个整数 n, 返回从 1 到 n 的字典顺序。

例如，

给定 n =1 3，返回 [1,10,11,12,13,2,3,4,5,6,7,8,9] 。

请尽可能的优化算法的时间复杂度和空间复杂度。 输入的数据 n 小于等于 5,000,000。
'''


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # return sorted(range(1, n + 1), key=str)

        # DFS  如此看来 DFS往往伴随着递归
        res = []

        def dfs(tmp):
            if tmp > n:
                return
            res.append(tmp)
            for d in range(10):
                dfs(tmp * 10 + d)

        for t in range(1, 10):
            dfs(t)
        return res

    # https://leetcode-cn.com/problems/lexicographical-numbers/solution/zi-fu-chuan-pai-xu-dfs-by-powcai/

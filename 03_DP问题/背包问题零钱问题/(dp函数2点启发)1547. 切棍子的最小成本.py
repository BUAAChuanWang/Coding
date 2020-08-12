'''
有一根长度为 n 个单位的木棍，棍上从 0 到 n 标记了若干位置。例如，长度为 6 的棍子可以标记如下：
给你一个整数数组 cuts ，其中 cuts[i] 表示你需要将棍子切开的位置。

你可以按顺序完成切割，也可以根据需要更改切割的顺序。

每次切割的成本都是当前要切割的棍子的长度，切棍子的总成本是历次切割成本的总和。对棍子进行切割将会把一根木棍分成两根较小的木棍（这两根木棍的长度和就是切割前木棍的长度）。请参阅第一个示例以获得更直观的解释。

返回切棍子的 最小总成本 。
示例 1：

输入：n = 7, cuts = [1,3,4,5]
输出：16
解释：按 [1, 3, 4, 5] 的顺序切割的情况如下所示：

第一次切割长度为 7 的棍子，成本为 7 。第二次切割长度为 6 的棍子（即第一次切割得到的第二根棍子），第三次切割为长度 4 的棍子，最后切割长度为 3 的棍子。总成本为 7 + 6 + 4 + 3 = 20 。
而将切割顺序重新排列为 [3, 5, 1, 4] 后，总成本 = 16（如示例图中 7 + 4 + 3 + 2 = 16）。
'''
import functools
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        # 比较好的递归dp
        # 启发：1. 对cuts收尾添加0和n，就可以不再dp函数中添加cuts的状态了
        #   2.递归函数里面 res直接定义 就可以返回结果，不需要额外定义全局变量ans
        cuts = sorted(cuts)
        cuts = [0] + cuts + [n]
        @functools.lru_cache(None)
        def dp(s, e):
            if e - s == 1:
                return 0
            if s == e:
                return e - s
            res = float("inf")
            for i in range(s + 1, e):
                res = min(res, cuts[e] - cuts[s] + dp(s, i) + dp(i, e))
            return res
        return dp(0, len(cuts) - 1)

        # 比赛时写的   这里self.ans 和 dp(cut, s, e) 都可以优化
        self.ans = float("inf")
        cuts = sorted(cuts)
        @functools.lru_cache(None)
        def dp(cut, s, e):
            # print(cut, s, e)
            if len(cut) == 0:
                return 0
            if len(cut) == 1:
                return e - s
            for i in range(len(cut)):
                self.ans = min(self.ans, e - s + dp(cut[ : i], s, cut[i]) + dp(cut[i + 1 : ], cut[i], e))
            return self.ans
        res = dp(tuple(cuts), 0, n)
        return res
'''
有两种形状的瓷砖：一种是 2x1 的多米诺形，另一种是形如 "L" 的托米诺形。两种形状都可以旋转。

XX  <- 多米诺

XX  <- "L" 托米诺
X
给定 N 的值，有多少种方法可以平铺 2 x N 的面板？返回值 mod 10^9 + 7。

（平铺指的是每个正方形都必须有瓷砖覆盖。两个平铺不同，当且仅当面板上有四个方向上的相邻单元中的两个，使得恰好有一个平铺有一个瓷砖占据两个正方形。）

示例:
输入: 3
输出: 5
解释:
下面列出了五种不同的方法，不同字母代表不同瓷砖：
XYZ XXZ XYY XXY XYY
XYZ YYZ XZZ XYY XXY
'''
class Solution:
    def numTilings(self, N: int) -> int:
        # https://leetcode.com/problems/domino-and-tromino-tiling/discuss/722908/Python3-TopDown-Approach-Play-Tetris
        @functools.lru_cache(None)
        def dp(n, a, b):  # dp返回填满 n 列并且 上面突出块a，下面突出块b 的情况下的可以装填方法的个数
            if n < 0: return 0
            if n == 0:
                return 1 if a + b == 0 else 0
            res = 0
            if a == 0 and b == 0:
                res += dp(n - 1, 0, 0)
                res += dp(n - 2, 0, 0)  # 这种情况是XX的砖的横着放的情况 ：在（n,0,0）的情况下，如果横着放只能一次放两块
                res += dp(n - 1, 1, 0)
                res += dp(n - 1, 0, 1)
            if a == 1 and b == 0:
                res += dp(n - 2, 0, 0)
                res += dp(n - 1, 0, 1)
            if a == 0 and b == 1:
                res += dp(n - 2, 0, 0)
                res += dp(n - 1, 1, 0)
            return res
        res = dp(N, 0, 0) % (10 ** 9 + 7)
        return res
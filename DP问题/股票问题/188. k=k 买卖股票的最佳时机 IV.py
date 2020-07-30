'''
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [2,4,1], k = 2
输出: 2
解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
'''


class Solution:
    def maxProfit(self, max_k: int, prices: List[int]) -> int:
        if not prices: return 0
        '''
        dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
        dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
        '''
        # 超内存的错误，是传入的 k 值会非常大，dp 数组太大了。现在想想，交易次数 k 最多有多大呢？
        # 一次交易由买入和卖出构成，至少需要两天。所以说有效的限制 k 应该不超过 n/2，如果超过，就没有约束作用了，相当于 k = +infinity。
        if max_k < len(prices) // 2:
            dp = [[[0 for _ in range(2)] for _ in range(max_k + 1)] for _ in range(len(prices))]
            for i in range(len(prices)):
                for k in range(1, max_k + 1):
                    if i == 0:
                        dp[0][k][0] = 0
                        dp[0][k][1] = -prices[0]
                        continue
                    dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                    dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
            return dp[-1][-1][0]
        else:
            # max_k >= n // 2  相当于k = +infinity 无限制交易次数
            dp = [[0 for _ in range(2)] for _ in range(len(prices))]
            dp[0][0] = 0
            dp[0][1] = -prices[0]
            for i in range(1, len(prices)):
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            return dp[-1][0]

        # 201912
        if not prices:
            return 0

        n = len(prices)
        if max_k > n / 2:
            dp = [[0 for i in range(2)] for i in range(n)]
            for i in range(len(prices)):
                if i - 1 == -1:
                    dp[i][0] = 0
                    dp[i][1] = -prices[i]
                    continue
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            return dp[-1][0]
        else:
            dp = [[[0 for n in range(2)] for k in range(max_k + 1)] for i in range(len(prices))]

            for i in range(len(prices)):
                for k in range(1, max_k + 1, 1):
                    if i - 1 == -1:
                        dp[i][k][0] = 0
                        dp[i][k][1] = -prices[i]
                        continue
                    dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i]);
                    dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i]);
            return dp[-1][-1][0]
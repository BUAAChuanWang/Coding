'''
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        '''
        dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
        dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
        '''
        dp = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(len(prices))]
        for i in range(len(prices)):
            for k in range(1, 3):
                if i == 0:
                    dp[0][k][0] = 0
                    dp[0][k][1] = -prices[0]
                    continue
                # k = 0 不考虑 因为都没有交易 手上也不可能有股票 所以都是0
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
        return dp[-1][2][0]

        # 201912
        '''
        if not prices:
            return 0

        dp = [[[0 for n in range(2)] for k in range(3)] for i in range(len(prices))]

        for i in range(len(prices)):
            for k in range(1, 3 , 1):
                if i-1==-1:
                    dp[i][k][0] = 0      
                    dp[i][k][1] = -prices[i]
                    continue
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i]);
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i]);

        return dp[-1][2][0];
        '''
        if not prices:
            return 0

        dp_i = [[0 for n in range(2)] for k in range(3)]

        for i in range(len(prices)):
            for k in range(1, 3, 1):
                if i - 1 == -1:
                    dp_i[k][0] = 0
                    dp_i[k][1] = -prices[i]
                    continue
                dp_i[k][0] = max(dp_i[k][0], dp_i[k][1] + prices[i]);
                dp_i[k][1] = max(dp_i[k][1], dp_i[k - 1][0] - prices[i]);

        return dp_i[2][0]
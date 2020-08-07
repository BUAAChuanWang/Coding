'''
剑指 Offer 63. 股票的最大利润
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？



示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        # dp_i_k_n i天k次交易n状态时的利润
        # dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1]+prices[i])
        # dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0]-prices[i])

        # k=1
        # dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1]+prices[i])
        # dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][0]-prices[i])
        #             = max(dp[i-1][1][1], 0-prices[i])
        # k=1是没用的 可简化为两维 dp_i_n  又可优化空间为一维
        dp = [[0 for _ in range(2)] for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], -prices[i])  # 这里必须是 -prices[i] 因为只能买一次
        return dp[-1][0]

        # 202003
        if not prices: return 0
        # dp[i][k][0] = max(dp[i-1][k][0], dp[i][k][1] + prices[i - 1])
        # dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i - 1])
        dp = [[0 for _ in range(2)] for _ in range(len(prices) + 1)]
        dp[0][0] = 0
        dp[0][1] = float("-inf")
        for i in range(1, len(prices) + 1):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i - 1])
            dp[i][1] = max(dp[i - 1][1], -prices[i - 1])
        return dp[-1][0]
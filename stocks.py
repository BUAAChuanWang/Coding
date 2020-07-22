while 1:
    # sample:[7,1,5,3,6,4]
    prices = list(map(lambda x: int(x), input().split(" ")))

    def maxProfit(prices):
        if not prices:
            return 0
        # dp[i][k][0] = max(dp[i-1][k][0], dp[i][k][1] + prices[i])
        # dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        dp = [[0 for _ in range(2)] for _ in range(len(prices) + 1)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, len(prices) + 1):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i - 1])
            dp[i][1] = max(dp[i - 1][1], -prices[i - 1])
        print(dp[-1][0])
        return dp[len(prices)][0]

    maxProfit(prices)
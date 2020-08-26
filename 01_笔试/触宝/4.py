'''
10 15 12 14
20 22 17 16

26

14 15 12 10
20 22 17 16

28
'''
# AC
import sys
if __name__ == "__main__":
# while 1:
    a = list(map(lambda x: int(x), sys.stdin.readline().strip().split(" ")))
    b = list(map(lambda x: int(x), sys.stdin.readline().strip().split(" ")))
    na, nb = len(a), len(b)

    res = float("inf")
    for i in range(na - 1):
        for j in range(i + 1, nb):
            res = min(res, a[i] + b[j])
    if na > 1: print(res)
    else: print("-1")

    # 40AC 因为a,b可能长度不一样
    n = len(a)
    dp = [[float("inf") for _ in range(2)] for _ in range(len(a))]
    dp[0][0] = float("inf")
    dp[0][1] = a[0]
    for i in range(1, len(a)):
        dp[i][0] = min(dp[i - 1][0], dp[i - 1][1] + b[i])
        dp[i][1] = min(dp[i - 1][1], a[i])
    if n > 1: print(dp[-1][0])
    else: print("-1")
    # if not prices: return 0
    # # dp_i_k_n i天k次交易n状态时的利润
    # # dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1]+prices[i])
    # # dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0]-prices[i])
    #
    # # k=1
    # # dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1]+prices[i])
    # # dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][0]-prices[i])
    # #             = max(dp[i-1][1][1], 0-prices[i])
    # # k=1是没用的 可简化为两维 dp_i_n  又可优化空间为一维
    # dp = [[0 for _ in range(2)] for _ in range(len(prices))]
    # dp[0][0] = 0
    # dp[0][1] = -prices[0]
    # for i in range(1, len(prices)):
    #     dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
    #     dp[i][1] = max(dp[i - 1][1], -prices[i])  # 这里必须是 -prices[i] 因为只能买一次
    # return dp[-1][0]

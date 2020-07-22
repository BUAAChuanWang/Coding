while 1:
    #   完全背包问题 coins中是不同coin的面额，可以无限选择任何coin的个数，以达到总面值为amount
    coins = list(map(lambda x: int(x), input().split(" ")))
    amount = int(input())
    # 自顶下下
    def coinChange(coins: List[int], amount: int):
        # 备忘录
        memo = dict()

        def dp(n):
            # 查备忘录，避免重复计算
            if n in memo: return memo[n]

            if n == 0: return 0
            if n < 0: return -1
            res = float('INF')
            for coin in coins:
                subproblem = dp(n - coin)
                if subproblem == -1: continue
                res = min(res, 1 + subproblem)

            # 记入备忘录
            memo[n] = res if res != float('INF') else -1
            return memo[n]

        return dp(amount)
    # 自底向上
    def coinChange(coins, amount):
        # dp[i]表示面值为i时的最少硬币个数
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        print(dp[-1] if dp[-1] != float("inf") else -1)

#================================================================================
    #   0 1背包问题
    '''
    给你一个可装载重量为W的背包和N个物品，每个物品有重量和价值两个属性。
    其中第i个物品的重量为wt[i]，价值为val[i]，现在让你用这个背包装物品，最多能装的价值是多少？
    '''
    def knapsack(W, N, wt, val):
        # dp全填入0，base case 已初始化。    dp[i][j]表示前i个物品重量为j的价值为dp[i][j]
        dp = [[0] * (W + 1) for _ in range(N + 1)]
        for i in range(1, N + 1):
            for j in range(1, W + 1):
                if j >= wt[i - 1]:
                    # 装入或者不装入背包，择优
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - wt[i - 1]] + val[i - 1])
                else:
                    # 当前背包容量装不下，只能选择不装入背包
                    dp[i][j] = dp[i - 1][j]
        return dp[N][W]

    N = int(input())
    W = int(input())
    wt = list(map(lambda x: int(x), input().split(" ")))
    val = list(map(lambda x: int(x), input().split(" ")))
    print(knapsack(W, N, wt, val))
    '''
    N = 3, W = 4
    wt = [2, 1, 3]
    val = [4, 2, 3]
    算法返回6，选择前两件物品装进背包，总重量3小于W，可以获得最大价值6。
    '''
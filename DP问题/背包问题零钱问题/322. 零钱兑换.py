'''
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1
'''


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # https://leetcode-cn.com/problems/perfect-squares/   相似题目 基本一模一样
        # BFS   因为求最小数量 所以BFS求得的第一个解一定是最小的
        queue = [(amount, 0)]
        seen = {amount}
        while queue:
            cur, step = queue.pop(0)
            if cur == 0:
                return step
            for i in range(len(coins)):
                if cur - coins[i] >= 0 and cur - coins[i] not in seen:
                    seen.add(cur - coins[i])
                    queue.append((cur - coins[i], step + 1))
        return -1

        # 完全背包问题 即物品无限次放入
        # DP  dpi -> 填满背包i需要的最少物品个数
        dp = [float("inf") for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            for j in coins:
                if i - j < 0: continue
                dp[i] = min(dp[i], dp[i - j] + 1)
        return dp[-1] if dp[-1] != float("inf") else -1

        '''
        # 202003
        # 完全背包问题 即物品无限次放入
        # dp[i]表示面值为i时的最少硬币数
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        # 状态转移方程：dp[i] = min(dp[i - coin] + 1)
        for i in range(1, amount + 1):
            #一行写法：dp[i] = min(dp[i - coin] + 1 if i - coin >= 0 else float("inf") for coin in coins)
            for coin in coins:
                if i - coin < 0: continue
                dp[i] = min(dp[i], dp[i - coin] + 1)  
        if dp[-1] == float("inf"): return -1
        return dp[-1]


        # DP备忘录直接超时
        memo = {}
        def dp(amount, n):
            if (amount, n) in memo:
                return memo[(amount, n)]
            if amount == 0:
                self.mini = min(self.mini, n)
                memo[(amount, n)] = self.mini
                return memo[(amount, n)]
            for coin in coins:
                if coin <= amount:
                    memo[(amount, n)] = dp(amount - coin, n + 1)
                else:
                    memo[(amount, n)] = -1
            return memo[(amount, n)]
        self.mini = float("inf")
        dp(amount, 0)
        # print(memo)
        return -1 if self.mini == float("inf") else self.mini


        # 贪心 + 剪枝
        if amount == 0:return 0

        def coinChanging(amount, c_index, count, res):
            if amount == 0:
                return min(res, count)
            if c_index == len(coins):
                return res
            k = amount // coins[c_index]
            while k >= 0 and k + count < res: # 剪枝 如：[3,7,405,436] 8839 这样的剪枝掉 不然会超时
                res = coinChanging(amount - k * coins[c_index], c_index + 1, count + k, res)
                k -= 1
            return res

        coins.sort(reverse=True)
        ans = coinChanging(amount, 0, 0, float("inf"))
        return ans if ans != float('inf') else -1
        '''

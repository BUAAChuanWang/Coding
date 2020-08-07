'''
给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。 
示例 1:

输入: amount = 5, coins = [1, 2, 5]
输出: 4
解释: 有四种方式可以凑成总金额:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
示例 2:

输入: amount = 3, coins = [2]
输出: 0
解释: 只用面额2的硬币不能凑成总金额3。
示例 3:

输入: amount = 10, coins = [10]
输出: 1
'''
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # https://labuladong.gitbook.io/algo/di-ling-zhang-bi-du-xi-lie/bei-bao-ling-qian
        # DP
        if amount == 0: return 1
        if not coins: return 0
        '''
        # dpij 表示 用前i个物品 填满j容量的背包  所需的个数
        dp = [[0 for j in range(amount + 1)] for i in range(len(coins)+1)]
        for i in range(1, len(coins)+1): 
            for j in range(amount+1):
                if j == 0:
                    dp[i][0] = 1
                    continue
                if j - coins[i-1] >= 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]
        '''
        dp = [0 for i in range(amount+1)]
        for i in range(1, len(coins)+1):
            for j in range(amount+1):   # 这个不能逆序  因为dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]用到了之前的结果
                if j == 0:
                    dp[0] = 1
                    continue
                if j - coins[i-1] >= 0:
                    dp[j] = dp[j] + dp[j-coins[i-1]]
                else:
                    dp[j] = dp[j]
        return dp[-1]
        '''
        # BFS   会超时
        queue = [(tuple([0 for _ in range(len(coins))]), amount)]
        seen = set()
        res = set()
        while queue:
            cur, step = queue.pop(0)
            if step == 0:
                res.add(cur)
            for i, nei in enumerate(coins):
                new_cur = list(cur)
                new_cur[i] += 1
                new_cur = tuple(new_cur)
                new_step = step - nei
                if new_cur not in seen and new_step >= 0:
                    queue.append((new_cur, new_step))
        # print(res)
        return len(res)
        '''
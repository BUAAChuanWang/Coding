'''
满减凑单问题

假设双十一购物，有满xx减xx的活动（例如满100-30），我现在购物车中有充足的商品，商品价格各不相同，请帮我利用购物车内商品凑单，
每个商品只能用一次，使我获得最大优惠（即凑单商品总价大于等于100但最近接近100）

输入：商品价格数组，凑单金额
输出：总价超过凑单金额但最接近的金额

例如
输入 [90, 52, 30, 65, 20] 100
输出 102
'''
class Solution:
    def function(self, coins, capacity):
        # DP
        dp = [coins[i] for i in range(len(coins))]

        dp = [[0 for i in range(len(coins) + 1)] for _ in range(capacity + 1)]
        for i in range(1, len(coins) + 1):
            for j in range(1, capacity + 1):
                # if dp[i-1][j]
                dp[i][j] = dp[i-1][j] or dp[i-1][j-coins[i]]
        # BFS
        queue = [(0, coins[0])]
        visited = [False for i in range(len(coins))]
        visited[0] = True
        self.res = float("inf")
        while queue:
            cur, step = queue.pop(0)
            if step >= capacity:
                self.res = min(self.res, step)
                continue
            for i in range(len(coins)):
                if not visited[i]:
                    new_cur, new_step = i, step + coins[i]
                    queue.append((new_cur, new_step))
        return self.res if self.res != float("inf") else -1

        dp = [coins[i] for i in range(len(coins))]
        for i in range(len(coins)):
            for j in range(i):
                if dp[i] >= capacity and dp[j] + coins[i] >= capacity:
                    dp[i] = min(dp[i], dp[j] + coins[i])
                elif dp[i] < capacity and dp[j] + coins[i] < capacity:
                    dp[i] = max(dp[i], dp[j] + coins[i])
                # elif
                dp[i] = dp[j] + coins[i] if abs(dp[j] + coins[i] - capacity) < abs(dp[i] - capacity) else dp[i]
        # for i in dp:

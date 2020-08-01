'''
在一个火车旅行很受欢迎的国度，你提前一年计划了一些火车旅行。在接下来的一年里，你要旅行的日子将以一个名为 days 的数组给出。每一项是一个从 1 到 365 的整数。

火车票有三种不同的销售方式：

一张为期一天的通行证售价为 costs[0] 美元；
一张为期七天的通行证售价为 costs[1] 美元；
一张为期三十天的通行证售价为 costs[2] 美元。
通行证允许数天无限制的旅行。 例如，如果我们在第 2 天获得一张为期 7 天的通行证，那么我们可以连着旅行 7 天：第 2 天、第 3 天、第 4 天、第 5 天、第 6 天、第 7 天和第 8 天。

返回你想要完成在给定的列表 days 中列出的每一天的旅行所需要的最低消费。

 

示例 1：

输入：days = [1,4,6,7,8,20], costs = [2,7,15]
输出：11
解释：
例如，这里有一种购买通行证的方法，可以让你完成你的旅行计划：
在第 1 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 1 天生效。
在第 3 天，你花了 costs[1] = $7 买了一张为期 7 天的通行证，它将在第 3, 4, ..., 9 天生效。
在第 20 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 20 天生效。
你总共花了 $11，并完成了你计划的每一天旅行。
'''


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # 递归dp  lru_cache
        n = len(days)
        dic = {1: costs[0], 7: costs[1], 30: costs[2]}
        import functools

        @functools.lru_cache(None)  # 自动备忘录 memo
        def dp(index):
            if index >= n:
                return 0
            ans = float("inf")
            new_index = index
            for span, cost in dic.items():
                while new_index < n and days[new_index] < days[index] + span:  # 找到刚好不能满足的最左一天
                    new_index += 1
                ans = min(ans, dp(new_index) + cost)
            return ans

        res = dp(0)
        return res

        # 递归dp memo备忘录
        n = len(days)
        dic = {1: costs[0], 7: costs[1], 30: costs[2]}
        memo = {}

        def dp(index):
            if index in memo: return memo[index]

            if index >= n:
                ans = 0
            else:
                ans = float("inf")
                for span, cost in dic.items():
                    new_index = index
                    while new_index < n and days[new_index] < days[index] + span:
                        new_index += 1
                    ans = min(ans, dp(new_index) + cost)
            memo[index] = ans
            return memo[index]

        res = dp(0)
        return res

        # DP table  别人的答案
        dp = [0 for _ in range(days[-1] + 1)]  # dp数组，每个元素代表到当前天数最少钱数，为下标方便对应，多加一个 0 位置
        days_idx = 0  # 设定一个days指标，标记应该处理 days 数组中哪一个元素
        for i in range(1, len(dp)):
            if i != days[days_idx]:  # 若当前天数不是待处理天数，则其花费费用和前一天相同
                dp[i] = dp[i - 1]
            else:
                # 若 i 走到了待处理天数，则从三种方式中选一个最小的
                dp[i] = min(dp[max(0, i - 1)] + costs[0],
                            dp[max(0, i - 7)] + costs[1],
                            dp[max(0, i - 30)] + costs[2])
                days_idx += 1
        return dp[-1]  # 返回最后一天对应的费用即可

        # 官解答案
        N = len(days)
        durations = [1, 7, 30]

        @lru_cache(None)
        def dp(i):  # dp函数返回的是到index天是还需要多少花费
            if i >= N:
                return 0
            ans = 10 ** 9
            j = i
            for c, d in zip(costs, durations):
                while j < N and days[j] < days[i] + d:
                    j += 1
                ans = min(ans, dp(j) + c)
            return ans

        return dp(0)

        # 自己写的 超时了，因为没有用备忘录，有很多重复计算。 并且参数定义太冗余了，加入（index,count）的备忘录也会超时。
        def dp(index, count, track):
            # print(n, index, count, track)
            if index >= len(days):
                self.res = min(self.res, count)
                self.path = track if self.res == count else self.path  # 能同时输出具体的花费
                return
            for k, v in dic.items():
                new_index = index
                for i in range(index, len(days)):
                    if days[index] + k > days[i]:
                        new_index += 1
                    else:
                        break
                dp(new_index, count + v, track + [k])

        dp(0, 0, [])
        # print(self.res, self.path)
        return self.res
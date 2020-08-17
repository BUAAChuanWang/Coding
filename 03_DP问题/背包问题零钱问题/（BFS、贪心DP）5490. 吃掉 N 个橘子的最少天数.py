'''
厨房里总共有 n 个橘子，你决定每一天选择如下方式之一吃这些橘子：

吃掉一个橘子。
如果剩余橘子数 n 能被 2 整除，那么你可以吃掉 n/2 个橘子。
如果剩余橘子数 n 能被 3 整除，那么你可以吃掉 2*(n/3) 个橘子。
每天你只能从以上 3 种方案中选择一种方案。

请你返回吃掉所有 n 个橘子的最少天数。

示例 1：

输入：n = 10
输出：4
解释：你总共有 10 个橘子。
第 1 天：吃 1 个橘子，剩余橘子数 10 - 1 = 9。
第 2 天：吃 6 个橘子，剩余橘子数 9 - 2*(9/3) = 9 - 6 = 3。（9 可以被 3 整除）
第 3 天：吃 2 个橘子，剩余橘子数 3 - 2*(3/3) = 3 - 2 = 1。
第 4 天：吃掉最后 1 个橘子，剩余橘子数 1 - 1 = 0。
你需要至少 4 天吃掉 10 个橘子。
示例 2：

输入：n = 6
输出：3
解释：你总共有 6 个橘子。
第 1 天：吃 3 个橘子，剩余橘子数 6 - 6/2 = 6 - 3 = 3。（6 可以被 2 整除）
第 2 天：吃 2 个橘子，剩余橘子数 3 - 2*(3/3) = 3 - 2 = 1。（3 可以被 3 整除）
第 3 天：吃掉剩余 1 个橘子，剩余橘子数 1 - 1 = 0。
你至少需要 3 天吃掉 6 个橘子。
'''

import functools


class Solution:
    def minDays(self, n: int) -> int:
        # BFS 记忆化BFS  常规套路
        queue = [(n, 0)]
        seen = set([n])
        while queue:
            cur, step = queue.pop(0)
            if cur == 0: return step
            if cur % 3 == 0 and cur // 3 not in seen:
                seen.add(cur // 3)
                queue.append((cur // 3, step + 1))
            if cur % 2 == 0 and cur // 2 not in seen:
                seen.add(cur // 2)
                queue.append((cur // 2, step + 1))
            if cur - 1 not in seen:
                seen.add(cur - 1)
                queue.append((cur - 1, step + 1))

        # https://leetcode-cn.com/problems/minimum-number-of-days-to-eat-n-oranges/solution/python3-8xing-dai-ma-shi-jian-fu-za-du-olog2ntu-ji/
        # 贪心 + DP
        @functools.lru_cache(None)
        def dp(n):
            if n == 0: return 0
            if n == 1: return 1  # 这个边界条件也很关键  如果没有 dp1根据dp0算出来是2 是错误的
            # if n == 2 or n == 3: return 2  # 这个边界条件可有可无 因为可以通过dp1算出来了
            return 1 + min(dp(n // 2) + n % 2, dp(n // 3) + n % 3)

        return dp(n)

        # 爆递归深度
        @functools.lru_cache(None)
        def dp(n):
            if n == 0: return 0
            res = float("inf")
            if n % 3 == 0:
                res = min(res, dp(n - 2 * (n // 3)) + 1)
            if n > 0:
                res = min(res, dp(n - 1) + 1)
            if n % 2 == 0:
                res = min(res, dp(n - n // 2) + 1)
            return res

        return dp(n)
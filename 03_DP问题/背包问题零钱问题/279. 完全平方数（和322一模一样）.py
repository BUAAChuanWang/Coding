'''
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.
'''


class Solution:
    def numSquares(self, n: int) -> int:
        # https://leetcode-cn.com/problems/coin-change/   基本一模一样
        # BFS  比DP速度快多了
        queue = [(n, 0)]
        seen = {n}  # 只记录n就行了，因为是BFS 所以最先出现的长度肯定小于等于后来出现的
        # seen = {(n, 0)}
        while queue:
            cur, step = queue.pop(0)
            residuals = [x ** 2 for x in range(1, int(cur ** 0.5) + 1)]
            for i in residuals:
                new_cur = cur - i
                new_step = step + 1
                if new_cur == 0:
                    return new_step
                if new_cur not in seen:
                    queue.append((new_cur, new_step))
                    seen.add(new_cur)
        return -1

        # 递归dp  6000ms
        residuals = [x ** 2 for x in range(1, int(n ** 0.5) + 1)]

        @functools.lru_cache(None)
        def dp(state):
            if state == 0:
                return 0
            res = float("inf")
            for i in residuals:
                if i > state:
                    return res
                if i <= state:
                    res = min(res, 1 + dp(state - i))
            return res

        return dp(n)

        # DP table
        # https://leetcode-cn.com/problems/perfect-squares/solution/chao-zhi-bai-kao-zui-jiang-xiao-xue-sheng-du-neng-/
        dp = [float("inf") for i in range(n + 1)]
        dp[0] = 0
        for i in range(1, n + 1):
            for j in range(1, int(i ** 0.5) + 1):
                dp[i] = min(dp[i], dp[i - j * j] + 1)  # dpi表示i需要多少个平方数表示   其实就是N = 1、2、4、9... + N’ 一个数=一个平方数+另一个数
        return dp[-1]

        '''
        # DFS 超时
        self.res = float("inf")
        self.ans = []
        def backtrack(track):
            if len(track) >= self.res: return
            if sum(track) == n:
                self.res = min(self.res, len(track))
                if self.res == len(track):
                    self.ans = track[:]
                return
            diff = n - sum(track)
            for i in range(int(sqrt(diff)), 0, -1):
                track.append(i ** 2)
                backtrack(track)
                track.pop()
        backtrack([])
        # print(self.res, self.ans)
        return self.res
        '''
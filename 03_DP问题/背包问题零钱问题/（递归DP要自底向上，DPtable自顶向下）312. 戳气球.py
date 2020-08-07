'''
有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。

现在要求你戳破所有的气球。如果你戳破气球 i ，就可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的 left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。

求所能获得硬币的最大数量。

说明:

你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
示例:

输入: [3,1,5,8]
输出: 167
解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
     coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
'''

import functools
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if not nums: return 0
        # https://leetcode-cn.com/problems/burst-balloons/solution/chuo-qi-qiu-by-leetcode-solution/
        # 自底向上DP 也就是递归DP  （逆过程：从气球中选一个然后加进去）
        n = len(nums)
        nums = [1] + nums + [1]

        @functools.lru_cache(None)
        def dp(left, right):  # dp返回nums的开区间(left, right)内结果的最大值
            if left >= right - 1:  # 终止条件  因为开区间，所以此时为空
                return 0
            res = 0
            for i in range(left + 1, right):
                cur = nums[left] * nums[i] * nums[right]  # 选择一个数
                cur += dp(left, i) + dp(i, right)  # 选完后分为左右dp(left, i) 和 dp(i, right)两个子问题
                res = max(res, cur)
            return res

        return dp(0, n + 1)

        # DP table
        n = len(nums)
        dp = [[0] * (n + 2) for _ in range(n + 2)]  # dpij表示填满开区间 (i,j) 能得到的最多硬币数
        val = [1] + nums + [1]

        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n + 2):
                for k in range(i + 1, j):
                    total = val[i] * val[k] * val[j]
                    total += dp[i][k] + dp[k][j]
                    dp[i][j] = max(dp[i][j], total)

        return rec[0][n + 1]

        # DP 自顶向下回溯DP 自己写的 超时  总结：如果要写递归DP 那就就得自底向上写
        @functools.lru_cache(None)
        def dp(state, count):
            if len(state) == 2:
                self.res = max(self.res, count)
                return
            for i in range(1, len(state) - 1):
                new_state = state[: i] + state[i + 1:]
                dp(new_state, count + state[i - 1] * state[i] * state[i + 1])

        self.res = float("-inf")
        state = tuple([1] + nums + [1])
        dp(state, 0)
        return self.res
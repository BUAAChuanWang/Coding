'''
还记得童话《卖火柴的小女孩》吗？现在，你知道小女孩有多少根火柴，请找出一种能使用所有火柴拼成一个正方形的方法。不能折断火柴，可以把火柴连接起来，并且每根火柴都要用到。

输入为小女孩拥有火柴的数目，每根火柴用其长度表示。输出即为是否能用所有的火柴拼成正方形。

示例 1:

输入: [1,1,2,2,2]
输出: true

解释: 能拼成一个边长为2的正方形，每边两根火柴。
示例 2:

输入: [3,3,3,3,4]
输出: false

解释: 不能用所有火柴拼成一个正方形。
'''


class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        # https://leetcode-cn.com/problems/partition-to-k-equal-sum-subsets/  和这个题一模一样
        # 解法：https://leetcode-cn.com/problems/matchsticks-to-square/solution/hui-su-by-powcai/
        # 模拟四个边  140ms
        if not nums: return False
        if sum(nums) % 4: return False
        edge = sum(nums) // 4
        nums = sorted(nums)

        def backtrack(track):
            if not nums: return True
            val = nums.pop()
            for i in range(len(track)):
                if track[i] + val <= edge:
                    track[i] += val
                    if backtrack(track): return True
                    track[i] -= val
                if track[i] == 0: break  # 这个剪枝非常有必要 不然2000ms 剪枝100ms
            nums.append(val)
            return False

        return backtrack([0] * 4)

        # 解法：https://leetcode-cn.com/problems/matchsticks-to-square/solution/hui-su-by-powcai/
        # 递归dp 500ms
        if len(nums) < 4: return False
        div, mod = divmod(sum(nums), 4)
        if mod != 0: return False

        nums = sorted(nums, reverse=True)

        def dp(cnt, start, edge, visited):
            if edge == 0:
                if cnt == 0:
                    return True
                return dp(cnt - 1, 0, div, visited)
            for i in range(start, len(nums)):
                if i not in visited and nums[i] <= edge:
                    if dp(cnt, i + 1, edge - nums[i], visited + [i]): return True
            return False

        return dp(3, 0, div, [])

        # 4800ms
        if len(nums) < 4: return False
        div, mod = divmod(sum(nums), 4)
        if mod != 0: return False

        c = collections.Counter(nums)

        def dfs(cnt, start, edge):
            if edge == 0:
                if cnt == 0:
                    return True
                return dfs(cnt - 1, 0, div)
            for i in range(start, len(c)):
                if c[k] > 0 and k <= edge:
                    c[k] -= 1
                    if dfs(cnt, i + 1, edge - k): return True
                    c[k] += 1
            return False

        return dfs(3, 0, div)

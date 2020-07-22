'''
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:

每个数组中的元素不会超过 100
数组的大小不会超过 200
示例 1:

输入: [1, 5, 11, 5]

输出: true

解释: 数组可以分割成 [1, 5, 5] 和 [11].
 

示例 2:

输入: [1, 2, 3, 5]

输出: false

解释: 数组不能分割成两个元素和相等的子集.
'''

# -0-
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 20200710
        # https://labuladong.gitbook.io/algo/dong-tai-gui-hua-xi-lie/bei-bao-zi-ji
        if sum(nums) % 2: return False
        summ = sum(nums) // 2
        '''# 正常二维dp
        # dp[i][j] 表示只用前i个num能否正好填满容量为j的背包 
        # dp[i][j] = dp[i-1][j-nums[i]] or dp[i-1][j]   状态压缩去掉i
        dp = [[False for i in range(summ+1)]for i in range(len(nums)+1)]
        for i in range(1, len(nums)+1):
            for j in range(summ+1):
                if j == 0:
                    dp[i][j] = True
                    continue
                if j - nums[i-1] >= 0:
                    dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
        return dp[-1][-1]
        '''
        # 状态压缩dp可以省空间  要逆序 不然会调用之前的解决造成错误  这是状态压所造成的。。。
        # 比如 【1，5】 如果正序  当i=0，那么dp[1]=True 因为nums0=1然后容量为1时可以填满，
        # 但是下一轮就会出现dp[2] 此时nums0=1 容量为2时 2-1=1本不能填满，但因为上一个结果dp1=True，所以也就填满了，造成了错误
        dp = [False for i in range(sum(nums) // 2 + 1)]
        dp[0] = True
        for i in range(1, len(nums) + 1):
            for j in range(summ, -1, -1):
                if j - nums[i - 1] >= 0:
                    dp[j] = dp[j - nums[i - 1]] or dp[j]
        return dp[-1]

        '''
        #https://leetcode.com/problems/partition-equal-subset-sum/discuss/90592/01-knapsack-detailed-explanation
        # 0/1背包 (还没理解为什么1d的dp要逆序，只是知道不能正序，逆序可能是可以避免利用前面的结果)
        summ = sum(nums)
        if summ & 1:return False
        summ //= 2
        dp = [False] * (summ + 1)
        dp[0] = True
        for i in range(1, len(nums) + 1):
            for j in range(summ, 0, -1): # 逆序 是因为变成了1d，那么还是正序的话就相当于DP[i][j] = DP[i-1][j] or DP[i][j-num]（而正确的应该是dp[i][j] = dp[i-1][j] or dp[i-1][j-num]）
                if nums[i - 1] <= j:
                    dp[j] = dp[j] or dp[j - nums[i - 1]]
        return dp[summ]
        '''
        '''
        # 未优化空间DP 便于理解
        summ = sum(nums)
        if summ & 1:return False
        summ //= 2
        # dp[i][j]表示是否可以用包括i之前的数字填满大小为j的数（i从1到len(nums)，j从0到sum）
        dp = [[False] * (summ + 1) for _ in range(len(nums) + 1)]
        dp[0][0] = True # i=0是没有数字, 用没有数字填满0 这肯定是True 因为i从1开始到len(nums)

        for j in range(1, summ + 1):
            dp[0][j] = False    # i=0是没有数字, 用没有数字填满j 这肯定是False
        for i in range(1, len(nums) + 1):
            dp[i][0] = True # 任何从1 到i的数字填满大小为0的背包都是可以的
        for i in range(1, len(nums) + 1):
            for j in range(1, summ + 1):
                dp[i][j] = dp[i - 1][j]
                if nums[i - 1] <= j: # 因为i从1到len(nums)
                    dp[i][j] = dp[i][j] or dp[i - 1][j - nums[i - 1]]
        return dp[len(nums)][summ]
        '''
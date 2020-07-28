'''
给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。

注意:
数组长度 n 满足以下条件:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
示例:

输入:
nums = [7,2,5,10,8]
m = 2

输出:
18

解释:
一共有四种方法将nums分割为2个子数组。
其中最好的方式是将其分为[7,2,5] 和 [10,8]，
因为此时这两个子数组各自的和的最大值为18，在所有情况中最小.
'''


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        if m == 1: return sum(nums)

        '''
        首先分析题意，可以得出结论，结果（子数组和的最大值的最小值）必定落在【max（nums）， sum（nums）】这个区间内，
        因为左端点对应每个单独的元素构成一个子数组，右端点对应所有元素构成一个子数组.  

        然后可以利用二分查找法逐步缩小区间范围，当区间长度为1时，即找到了最终答案。

        每次二分查找就是先算一个mid值，这个mid就是代表当前猜测的答案，然后模拟一下划分子数组的过程，
        可以得到用这个mid值会一共得到的子区间数cnt，然后比较cnt和m的关系，来更新区间范围。

        本题跟1014 875 非常类似。
        '''

        # 二分  「使……最大值尽可能小」是二分搜索题目常见的问法。
        l, r = max(nums), sum(nums) + 1  # 子数组和最大值的最小值的取值范围是 当每个数是一个子数组时的max(nums)和所有数字是一个子数组时的sum(nums)
        print(l, r)
        while l < r:
            mid = l + (r - l) // 2  # 最大和
            # 以下在模拟划分子数组的过程
            summ, count = 0, 1  # count初始值须为1 因为最后少加一个
            for i in range(len(nums)):
                summ += nums[i]
                if summ > mid:  # 说明当前这个子数组的和已经超过了允许的最大值mid，需要把当前元素放在下一个子数组里
                    summ = nums[i]
                    count += 1

            if count <= m:  # 二分求最左  也就是最小的符合条件的
                r = mid
            elif count > m:  # 说明分出了比要求多的子数组，多切了几刀，说明mid应该加大，这样能使子数组的个数减少
                l = mid + 1
        return l

        # DP 会超时
        # https://leetcode-cn.com/problems/split-array-largest-sum/solution/pythondong-tai-gui-hua-er-fen-fa-by-idealworld/
        presum = [nums[0] for _ in range(len(nums))]
        for i in range(1, len(nums)):
            presum[i] = presum[i - 1] + nums[i]

        dp = [[float("inf") for i in range(len(nums))] for _ in range(m + 1)]  # dp[i][j]表示从nums[0]~nums[j]分成i组的解
        for i in range(len(nums)):  # dp[1][j] = sum(0, j), 包含边界，表示只划分一段时的解
            dp[1][i] = presum[i]

        for i in range(2, m + 1):
            for j in range(i - 1, len(nums)):
                for k in range(0, j):
                    dp[i][j] = min(dp[i][j], max(dp[i - 1][k], presum[j] - presum[k]))
        return dp[m][len(nums) - 1]
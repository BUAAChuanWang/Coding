'''
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。

进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
'''


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        # dp  其实就是纯暴力解 dpi表示到i为止包括i的最长上升子序列的长度
        if not nums: return 0
        dp = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                dp[i] = max(dp[j] + 1, dp[i]) if nums[i] > nums[j] else dp[i]
        # print(dp)
        return max(dp)
        '''

        # 二分
        # 二分查找最左边界
        def get_lbound(nums, l, r, target):  # d中小于target的元素有多少个
            while l < r:
                mid = l + (r - l) // 2
                if nums[mid] >= target:
                    r = mid
                elif nums[mid] < target:
                    l = mid + 1
            # 完整左边界代码 这里不适用
            # if l == len(nums) or nums[l] != target:
            #     return -1
            return l

        if not nums: return 0
        d = [nums[0]]  # di表示长度为i+1的上升子序列的最后一个数字
        for i in range(1, len(nums)):
            if nums[i] > d[-1]:
                d.append(nums[i])
            else:
                lbound = get_lbound(d, 0, len(d), nums[i])
                print(d, nums[i], lbound)
                d[lbound] = nums[i]
        return len(d)

        '''
        # 贪心 + 二分 O(nlogn)
        if not nums: return 0
        d = [] # d[i]表示长度为i + 1的最长上升子序列的结尾元素的最小值
        d.append(nums[0])  # 初始化, 将第一个元素加入d中 表示长度为1的最长上升子序列的结尾元素的最小值目前为nums[0]
        for i in range(1, len(nums)):
            if nums[i] > d[-1]:
                d.append(nums[i])
            elif nums[i] <= d[-1]:
                l, r = 0, len(d) # [0, len(d))
                while l < r:
                    mid = l + (r - l) // 2
                    if d[mid] < nums[i]:
                        l = mid + 1
                    elif d[mid] == nums[i]:
                        r = mid
                    elif d[mid] > nums[i]:
                        r = mid
                lbound = l  # 比nums[i]大的所有数的左边界，就是比nums[i]大的所有数里面最小的数
                d[lbound] = nums[i] # 把左边界变成nums[i]
        return len(d)
        '''
        '''
        # dp O(n^2)
        if not nums: return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
        '''
'''
给定正整数数组 A，A[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的距离为 j - i。

一对景点（i < j）组成的观光组合的得分为（A[i] + A[j] + i - j）：景点的评分之和减去它们两者之间的距离。

返回一对观光景点能取得的最高分。

 

示例：

输入：[8,1,5,2,6]
输出：11
解释：i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
'''
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        # https://leetcode-cn.com/problems/best-sightseeing-pair/solution/zui-jia-guan-guang-zu-he-by-leetcode-solution/
        # A[i] + A[j] + i - j = A[i] + i + A[j] - j
        # 因此只需一次遍历，当遍历到A[j]时，只需要计算j左边的最大的A[i] + i即可，这在之前的遍历中记录即可
        left, res = A[0], float("-inf")
        for j in range(1, len(A)):
            res = max(res, left + A[j] - j)
            left = max(left, A[j] + j)
        return res
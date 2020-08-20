'''
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 更优化
        res = []

        def backtrack(nums, track):
            if not nums:
                res.append(track)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i + 1:], track + [nums[i]])

        backtrack(nums, [])
        return res


        # 自解
        self.res = []

        def backtrack(track):
            if len(track) == len(nums):
                self.res.append(track[:])
                return
            for i in range(len(nums)):
                if nums[i] not in track:
                    backtrack(track + [nums[i]])
            return

        backtrack([])
        return self.res

        '''
        # 记录「路径」
        track = []
        res = []
        def backtrack(nums, track):
            # 触发结束条件
            if len(track) == len(nums):
                res.append(track[:])
                return
            for i in range(len(nums)):
                # 排除不合法的选择
                if nums[i] in track:
                    continue
                # 做选择
                track.append(nums[i])
                # 进入下一层决策树
                backtrack(nums, track)
                # 取消选择
                track.pop()

        backtrack(nums, track)
        return res
        '''
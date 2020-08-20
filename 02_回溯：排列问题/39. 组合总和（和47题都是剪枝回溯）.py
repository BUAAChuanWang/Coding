'''
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1：

输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]
示例 2：

输入：candidates = [2,3,5], target = 8,
所求解集为：
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 和47题一样的 需要剪枝的回溯
        candidates.sort()  # 剪枝第一步 排序  排序后有利于剪枝
        self.res = []

        def backtrack(track, count):
            print(track, count)
            if count == target:
                self.res.append(track)
                return
            for i in range(len(candidates)):
                if track and candidates[i] < track[-1]:  # 剪枝 排序后只存在递增序列 通过这个条件剪枝
                    continue
                if count + candidates[i] > target:
                    return
                backtrack(track + [candidates[i]], count + candidates[i])

        backtrack([], 0)
        # print(self.res)
        return self.res

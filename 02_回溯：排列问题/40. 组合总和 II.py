'''
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
'''


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        if i > index and nums[i] == nums[i - 1]: continue  这句话是 使得结果没有重复的 比如112与 121和211 这样重复的结果就会被过滤掉
        if i > 0 and nums[i - 1] == nums[i] and not visited[i - 1]: continue  这句话是 使得结果是全排列的 并且是无重复的 比如112 121 211
        '''
        # 回溯 高效剪枝
        candidates.sort()

        def backtrack(index, track, count):
            # print(index, track, count)
            if count == target:
                self.res.append(track)
                return
            for i in range(index, len(candidates)):
                if candidates[i] + count > target:
                    return
                # 剪枝 剪去 1 1’ 2 3中 1‘的情况，因为如果123是一个解的话，那么1’23也是一个解，这就重复了
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                backtrack(i + 1, track + [candidates[i]], count + candidates[i])  # 从下一个起点开始递归

        self.res = []
        backtrack(0, [], 0)
        # print(self.res)
        return self.res

        # 回溯的特点就是求解集  DP是求最值类似的 比如能满足条件的解中个数最少是多少
        candidates.sort()
        visited = set()

        def backtrack(candi, track, count):
            # print(candi, track, count)
            if count == target:
                self.res.add(tuple(track))
                return
            for i in range(len(candi)):
                if candi[i] + count > target:
                    return
                if track and candi[i] < track[-1]:  # 剪枝 排序后只存在递增序列 通过这个条件剪枝
                    continue
                backtrack(candi[: i] + candi[i + 1:], track + [candi[i]], count + candi[i])

        self.res = set()
        backtrack(candidates, [], 0)
        self.res = list(map(lambda x: list(x), list(self.res)))
        # print(self.res)
        return self.res



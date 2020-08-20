'''
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        if i > index and nums[i] == nums[i - 1]: continue  这句话是 使得结果没有重复的 比如112与 121和211 这样重复的结果就会被过滤掉
        if i > 0 and nums[i - 1] == nums[i] and not visited[i - 1]: continue  这句话是 使得结果是全排列的 并且是无重复的 比如112 121 211
        '''
        # 重复元素的回溯+剪枝
        # 重复元素的回溯的剪枝的要领：1.原集合先排序
        # 2.加入index作为遍历起点，然后对i>index的查看，i和i-1是否是同一个数，如果是同一个数就跳过，因为已经遍历过了。
        # 比如：40题中求和，那么有1 1' 2 3 target=6  就有123 和 1‘23是重复的结果，所以判断i == i-1就好
        nums.sort()
        def backtrack(index, track):
            self.res.append(track)
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                backtrack(i + 1, track + [nums[i]])
        self.res = []
        backtrack(0, [])
        # print(self.res)
        return self.res
'''
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 不含重复元素的回溯+剪枝
        # 不含重复的剪枝要领 ： 就是加一个index作为遍历的起点索引，就是从之前遍历过的后面开始新的遍历（如果需要的话，要先排序）
        def backtrack(index, track):
            self.res.append(track)
            for i in range(index, len(nums)):
                backtrack(i + 1, track + [nums[i]])
        self.res = []
        backtrack(0, [])
        # print(self.res)
        return self.res


        # 别人写的非递归 https://leetcode-cn.com/problems/subsets/solution/hui-su-suan-fa-by-powcai-5/
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
        return res
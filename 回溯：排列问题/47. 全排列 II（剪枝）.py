'''
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        '''
        if i > index and nums[i] == nums[i - 1]: continue  这句话是 使得结果没有重复的 比如112与 121和211 这样重复的结果就会被过滤掉
        if i > 0 and nums[i - 1] == nums[i] and not visited[i - 1]: continue  这句话是 使得结果是全排列的 并且是无重复的 比如112 121 211
        '''
        if not nums: return []
        nums.sort()
        res = []
        visited = set()
        def backtrack(track):
            print(track, visited)
            if len(nums) == len(track):
                res.append(track)
                return
            for i in range(len(nums)):
                # 重点就是剪枝：如果这个数和之前的数一样，并且之前的数还未使用过（说明已经回溯过） 前提是排序过
                if i in visited or (i > 0 and i - 1 not in visited and nums[i-1] == nums[i]):
                    continue
                visited.add(i)
                backtrack(track + [nums[i]])
                visited.remove(i)
        backtrack([])
        return res


        # 超时
        nums.sort()
        count = collections.Counter(nums)
        def backtrack(track):
            if len(track) == len(nums):
                self.res.add(tuple(track))
                return
            for num in nums:
                if count[num] == 0: continue
                count[num] -= 1
                backtrack(track + [num])
                count[num] += 1
        self.res = set()
        backtrack([])
        # print(self.res)
        res = []
        for r in list(self.res):
            res.append(list(r))
        return res
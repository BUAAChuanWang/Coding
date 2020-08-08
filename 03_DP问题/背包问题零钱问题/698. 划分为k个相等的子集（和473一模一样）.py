'''
给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。

示例 1：

输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
输出： True
说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。
'''

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # 模拟 k个箱子
        target = sum(nums) // k
        rem = sum(nums) % k
        if rem: return False

        def dp(groups):
            if not nums: return True
            v = nums.pop()
            for i, group in enumerate(groups):
                if group + v <= target:
                    groups[i] += v
                    if dp(groups): return True
                    groups[i] -= v
                # 这里， 如果groups全为0的时候，把v放到groups[0]不成功,
                # 那么把v放到 i > 0的任何groups[i]中也不会成功，所以直接直接break返回false，没必要继续遍历
                if not group: break
            nums.append(v)
            return False

        nums.sort()
        if nums[-1] > target: return False
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1

        return dp([0] * k)

        # 递归dp
        part = sum(nums) // k
        if sum(nums) % part: return False
        nums = sorted(nums, reverse=True)

        # 递归DP  start很重要,需要剪枝,不然会超时
        def dp(state, start, count, visited):
            if state == 0:
                return True
            if count == part:
                return dp(state, 0, 0, visited)
            for i in range(start, len(nums)):
                if i not in visited and count + nums[i] <= part:
                    visited.add(i)
                    self.ans = self.ans or dp(state - nums[i], i + 1, count + nums[i], visited)
                    visited.remove(i)
            return self.ans

        self.ans = False
        visited = set()
        dp(sum(nums), 0, 0, visited)
        return self.ans

        '''
        s = sum(nums)
        if s % k != 0 or len(nums) < k:
            return False
        self.res = None
        visited = []
        target = s / k
        nums.sort(reverse=True)
        def dfs(cnt, start, tmp, visited):
            if tmp==target:
                dfs(cnt - 1, 0, 0, visited)
            if cnt == 0:
                self.res = True
                return True
            if not self.res:
                for i in range(start, len(nums)):
                    if tmp + nums[i] <= target and i not in visited:
                        if tmp + nums[i] <= target:
                            dfs(cnt, i + 1, tmp + nums[i], visited + [i])
        dfs(k, 0, 0, [])
        return self.res
        '''
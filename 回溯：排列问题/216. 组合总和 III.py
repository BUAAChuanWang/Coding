'''
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：

所有数字都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: k = 3, n = 7
输出: [[1,2,4]]
示例 2:

输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]
'''
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # 回溯
        def backtrack(track, index, count):
            if len(track) == k:
                if count == n:
                    res.append(track)
                return
            for i in range(index, 10):
                if (not track or track and i > track[-1]) and count + i <= n:
                    backtrack(track + [i], i + 1, count + i)
        res = []
        backtrack([], 1, 0)
        # print(res)
        return res

        # BFS
        queue = [([], 1, 0)]
        res = []
        while queue:
            cur, idx, count = queue.pop(0)
            if len(cur) == k:
                if count == n:
                    res.append(cur)
                continue
            for i in range(idx, 10):
                if (not cur or cur and i > cur[-1]) and count + i <= n:
                    queue.append((cur + [i], idx + 1, count + i))
        # print(res)
        return res

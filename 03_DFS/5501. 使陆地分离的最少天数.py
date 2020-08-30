'''
给你一个由若干 0 和 1 组成的二维网格 grid ，其中 0 表示水，而 1 表示陆地。岛屿由水平方向或竖直方向上相邻的 1 （陆地）连接形成。

如果 恰好只有一座岛屿 ，则认为陆地是 连通的 ；否则，陆地就是 分离的 。

一天内，可以将任何单个陆地单元（1）更改为水单元（0）。

返回使陆地分离的最少天数。

 

示例 1：



输入：grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
输出：2
解释：至少需要 2 天才能得到分离的陆地。
将陆地 grid[1][1] 和 grid[0][2] 更改为水，得到两个分离的岛屿。
示例 2：

输入：grid = [[1,1]]
输出：2
解释：如果网格中都是水，也认为是分离的 ([[1,1]] -> [[0,0]])，0 岛屿。
示例 3：

输入：grid = [[1,0,1,0]]
输出：0
示例 4：

输入：grid = [[1,1,0,1,1],
             [1,1,1,1,1],
             [1,1,0,1,1],
             [1,1,0,1,1]]
输出：1
示例 5：

输入：grid = [[1,1,0,1,1],
             [1,1,1,1,1],
             [1,1,0,1,1],
             [1,1,1,1,1]]
输出：2
'''

# 因为肯定是会有角的，所以最多只需删除两次。

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        # 用 i*n+j 来 dfs，注意左右边界
        def dfs(x, s, res):
            res.add(x)
            for v in (x - (0 if x % n == 0 else 1), x + (0 if (x + 1) % n == 0 else 1), x - n, x + n):
                if 0 <= v < m * n and not v in res and v in s:
                    dfs(v, s, res)
            return res

        # 直接取第一个值做dfs，比较给入的值如果差为空，证明两者相等，不能分割
        def fine(ones):
            s = set(ones)
            if not s - dfs(ones[0], s, set()):
                return False
            return True

        m, n = len(grid), len(grid[0])
        # 转换所有值为1的数字成为 i*n+j
        ones = [i * n + j for i in range(m) for j in range(n) if grid[i][j] == 1]
        if not ones or fine(ones):
            return 0
        else:
            for i in range(len(ones)):
                if fine(ones[:i] + ones[i + 1:]):
                    return 1
        return 2

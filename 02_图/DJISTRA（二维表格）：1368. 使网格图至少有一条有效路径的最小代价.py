'''
给你一个 m x n 的网格图 grid 。 grid 中每个格子都有一个数字，对应着从该格子出发下一步走的方向。 grid[i][j] 中的数字可能为以下几种情况：

1 ，下一步往右走，也就是你会从 grid[i][j] 走到 grid[i][j + 1]
2 ，下一步往左走，也就是你会从 grid[i][j] 走到 grid[i][j - 1]
3 ，下一步往下走，也就是你会从 grid[i][j] 走到 grid[i + 1][j]
4 ，下一步往上走，也就是你会从 grid[i][j] 走到 grid[i - 1][j]
注意网格图中可能会有 无效数字 ，因为它们可能指向 grid 以外的区域。

一开始，你会从最左上角的格子 (0,0) 出发。我们定义一条 有效路径 为从格子 (0,0) 出发，每一步都顺着数字对应方向走，最终在最右下角的格子 (m - 1, n - 1) 结束的路径。有效路径 不需要是最短路径 。

你可以花费 cost = 1 的代价修改一个格子中的数字，但每个格子中的数字 只能修改一次 。

请你返回让网格图至少有一条有效路径的最小代价。

 示例 1：

输入：grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
输出：3
解释：你将从点 (0, 0) 出发。
到达 (3, 3) 的路径为： (0, 0) --> (0, 1) --> (0, 2) --> (0, 3) 花费代价 cost = 1 使方向向下 --> (1, 3) --> (1, 2) --> (1, 1) --> (1, 0) 花费代价 cost = 1 使方向向下 --> (2, 0) --> (2, 1) --> (2, 2) --> (2, 3) 花费代价 cost = 1 使方向向下 --> (3, 3)
总花费为 cost = 3.
'''
import heapq
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        # https://leetcode-cn.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/solution/python-jian-dan-bfs-jie-jue-by-hao-shou-bu-juan-2/
        # 二维ij的disjkstra  堆的标准写法
        # 相当于每个点有上下左右四个nei，将原始方向的nei看做w=0，其他三个方向的要改变方向所以w=1。
        # 就可以把问题转换为（0，0）到（-1，-1）的单源最小路径和问题
        # 因为二维已经有ij的grid了，就不用构建graph了 直接四个方向就完事了
        m, n = len(grid), len(grid[0])
        priorityq = [(0, 0, 0)]        # 状态定义(开销，行号，列号)
        dist = {}

        while priorityq:
            cost, i, j = heapq.heappop(priorityq)
            if (i, j) in dist: continue
            dist[(i, j)] = cost
            if i == m-1 and j == n-1:  # 提前结束 没必要求出源点到每个点的最小路径和
                return cost
            for x, y, d in [(i-1, j, 4), (i+1, j, 3), (i, j-1, 2), (i, j+1, 1)]:
                if x >= 0 and x < m and y >= 0 and y < n:
                    if (x, y) not in dist:
                        new_cost = cost+1 if d != grid[i][j] else cost
                        heapq.heappush(priorityq, (new_cost, x, y))
        return -1
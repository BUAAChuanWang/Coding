'''
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

 

示例 1:

输入:
[
['1','1','1','1','0'],
['1','1','0','1','0'],
['1','1','0','0','0'],
['0','0','0','0','0']
]
输出: 1
示例 2:

输入:
[
['1','1','0','0','0'],
['1','1','0','0','0'],
['0','0','1','0','0'],
['0','0','0','1','1']
]
输出: 3
解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成
'''


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 20200820
        if not grid or not grid[0]: return 0
        # 并查集
        m, n = len(grid), len(grid[0])
        self.count = sum(sum(list(map(int, x))) for x in grid)
        # 简版并查集的构建的套路框架
        parent = [i for i in range(m * n + 1)]  # 二维并查集 将行列都变成一维的基本套路

        def union(p, q):
            rootp = find(p)
            rootq = find(q)
            if rootp == rootq: return
            parent[rootp] = rootq
            self.count -= 1  # 针对本题加的一句

        def find(p):
            while p != parent[p]:
                p = parent[p]
            return p

        # 利用并查集搜索
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0": continue
                index = i * n + j
                if j < n - 1 and grid[i][j + 1] == "1":
                    union(index, index + 1)
                if i < m - 1 and grid[i + 1][j] == "1":
                    union(index, index + n)
        return self.count

        # 20200820
        # DFS
        m, n = len(grid), len(grid[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]

        def dfs(i, j):
            if grid[i][j] == "1":
                visited[i][j] = 1
                for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    x, y = i + a, j + b
                    if 0 <= x < m and 0 <= y < n and not visited[x][y] and grid[x][y] == "1":
                        dfs(x, y)

        count = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count

        # 202003
        # 并查集
        if len(grid) == 0: return 0
        row = len(grid);
        col = len(grid[0])
        self.count = sum(grid[i][j] == '1' for i in range(row) for j in range(col))  # 初始每个点都是一个连通块
        parent = [i for i in range(row * col)]  # 初始化祖先就是每个人的祖先都是自己

        # find就是取祖先的函数
        def find(x):
            if parent[x] != x:
                return find(parent[x])  # 递归找祖先
            return parent[x]

        # union是合并祖先的函数。相当于一直找祖先的过程，如果现在的和下一个点是一样的值，那么下个点就是这个点的祖先
        def union(x, y):
            xroot, yroot = find(x), find(y)  # 先找到目前两个点各自的祖先
            if xroot == yroot: return
            parent[xroot] = yroot  # 把这点的祖先指向下个点
            self.count -= 1  # 连通块减一

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':
                    continue
                index = i * col + j
                if j < col - 1 and grid[i][j + 1] == '1':
                    union(index, index + 1)  # 合并祖先
                if i < row - 1 and grid[i + 1][j] == '1':
                    union(index, index + col)
        return self.count
        '''
        # DFS
        def dfs(grid, i, j):
            if i <0 or i == len(grid) or j <0 or j == len(grid[0]):
                return

            if grid[i][j] == "1":
                grid[i][j] = "0"
                dfs(grid, i-1, j)
                dfs(grid, i+1, j)
                dfs(grid, i, j-1)
                dfs(grid, i, j+1)
            else:
                return
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(grid, i, j)
                    res += 1
                    #print(grid)
                    #return 0
        return res
        '''
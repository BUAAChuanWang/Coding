'''
2、 一个地图n*m，包含1个起点，1个终点，其他点包括可达点和不可达点。
求走的最短路径，一个matrix，S表示start，E表示目的地，剩下的“#“ 表示障碍，”.“表示可以通过，求可以从S到E的最短路径，没有就输出-1.
每一次可以：上下左右移动，或使用1点能量从（i,j)瞬间移动到（n-1-i, m-1-j)，最多可以使用5点能量。
数据范围：2 <= n,m <= 500;
示例:
输入：
4 4
#S..
E#..
....
....
输出：4
解释:S(0,1)先瞬移到(3, 2)，然后往上一步，往右一步，瞬移到E，一共4步
思路:
如果没有瞬移步数要求，那这就是一个经典的地图问题，算是BFS的模板题，那加入瞬移步数要求之后，需要记录fly变量，fly表示已经瞬移的步数。
'''
while 1:
    import collections
    n, m = list(map(lambda x: int(x), input().split(" ")))
    matrix = [[] for _ in range(n)]
    for i in range(n):
        matrix[i] = list(map(lambda x: str(x), list(input())))

    class Node:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.stp = None
            self.cnt = None

    def BFS():
        q = collections.deque()
        node = Node(sx, sy)
        node.stp = 0
        node.cnt = 5

        q.append(node)
        visited[sx][sy] = 1
        while q:
            now = q.popleft()
            if now.x == ex and now.y == ey:
                res = now.stp
                return res
            for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x, y = now.x + a, now.y + b
                if 0 <= x < n and 0 <= y < m and not visited[x][y] and (matrix[x][y] == "." or matrix[x][y] == "E"):
                    nex = Node(x, y)
                    nex.stp = now.stp + 1
                    nex.cnt = now.cnt
                    q.append(nex)
                    visited[x][y] = 1

            if nex.cnt >= 1:
                x = n - 1 - now.x
                y = m - 1 - now.y
                if 0 <= x < n and 0 <= y < m and not visited[x][y] and (matrix[x][y] == "." or matrix[x][y] == "E"):
                    nex = Node(x, y)
                    nex.stp = now.stp + 1
                    nex.cnt = now.cnt - 1
                    q.append(nex)
                    visited[x][y] = 1
        return -1

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "S":
                sx, sy = i, j
            if matrix[i][j] == "E":
                ex, ey = i, j
    visited = [[0] * m for _ in range(n)]
    res = BFS()
    print(res)
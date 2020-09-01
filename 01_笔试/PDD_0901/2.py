'''
4 4
1 0 1 1
1 1 0 1
0 0 0 0
1 1 1 1

1 0 0 1
1 1 0 1
1 0 0 0
1 1 1 1

8

3 4
0 1 0 0
1 0 1 1
0 1 0 0

0 1 0 0
0 1 1 1
0 1 0 0

5
'''
import sys
if __name__ == "__main__":
    # 读取第一行的n
    n, m = list(map(lambda x:int(x), sys.stdin.readline().strip().split()))
    grid = []
    for i in range(n):
        grid.append(list(map(lambda x:int(x), sys.stdin.readline().strip().split())))

    visited = [[0 for _ in range(m)] for _ in range(n)]
    def dfs(i, j):
        if grid[i][j] == 0: return 0
        if grid[i][j] == 1:
            visited[i][j] = 1
            for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x, y = i + a, j + b
                if 0 <= x < n and 0 <= y < m and grid[x][y] and not visited[x][y]:
                    return 1 + dfs(x, y)


    h = set()
    for i in range(n):
        for j in range(m):
            if grid[i][j] and not visited[i][j]:
                h.add(dfs(i, j))
    print(h)


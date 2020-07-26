'''
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

 

示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false
'''


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]: return False

        def dfs(i, j, length):
            if length == len(word) - 1:
                return board[i][j] == word[length]
            if board[i][j] == word[length]:
                visited[i][j] = 1
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= x < len(board) and 0 <= y < len(board[0]) and not visited[x][y] and dfs(x, y, length + 1):
                        return True
                visited[i][j] = 0
            return False

        visited = [[0] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False

        '''
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
        dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

        def haspath(i, j, k):
            # 先写递归终止条件
            if k == len(word) - 1:
                return board[i][j] == word[k]
            # 中间匹配了，再继续搜索
            if board[i][j] == word[k]:
                # 先占住这个位置，搜索不成功的话，要释放掉
                visited[i][j] = True
                for a, b in dirs:
                    x = i + a
                    y = j + b
                    # 注意：如果这一次 search word 成功的话，就返回    
                    # 我们发现 回溯的核心就是再递归的时候 变量的递增写在函数里面 比如这里 haspath(x, y, k + 1)
                    if 0 <= x < m and 0 <= y < n and not visited[x][y] and haspath(x, y, k + 1):
                        return True
                visited[i][j] = False
            return False

        for i in range(m):
            for j in range(n):
                # 对每一个格子都从头开始搜索
                if haspath(i, j, 0):
                    return True
        return False
        '''
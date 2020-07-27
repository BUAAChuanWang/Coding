'''
给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

示例:

输入:
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

输出: ["eat","oath"]
'''
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 前缀树 + DFS
        # 构建前缀树的方法 背下来吧
        trie = {}
        for word in words:
            t = trie
            for w in word:
                t = t.setdefault(w, {})
            t["end"] = 1
        #     print(t)
        #     print(trie)
        # print(trie)
        res = []
        row = len(board)
        col = len(board[0])
        def dfs(i, j, trie, s):
            #print(i, j, trie, s)
            c = board[i][j]
            if c not in trie: return
            trie = trie[c]
            if "end" in trie and trie["end"] == 1:
                res.append(s + c)
                trie["end"] = 0 # 防止重复数组加入
            board[i][j] = "#"
            for x, y in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                tmp_i = x + i
                tmp_j = y + j
                if 0 <= tmp_i < row and 0 <= tmp_j < col and board[tmp_i][tmp_j] != "#":
                    dfs(tmp_i, tmp_j, trie, s + c)
            board[i][j] = c
        for i in range(row):
            for j in range(col):
                dfs(i, j, trie, "")
        return res
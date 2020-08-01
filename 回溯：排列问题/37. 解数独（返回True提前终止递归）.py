'''
编写一个程序，通过已填充的空格来解决数独问题。

一个数独的解法需遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。
'''


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 回溯  通过返回True来终止后续递归
        # 模拟行列顺序填数字
        # https://labuladong.gitbook.io/algo/suan-fa-si-wei-xi-lie/sudoku
        m, n = 9, 9
        def check(board, x, y, k):
            a, b = x // 3, y // 3
            for i in range(9):
                if k in board[x][i] or k in board[i][y] or k in board[a * 3 + i // 3][b * 3 + i % 3]: return False
                # np切片：if k in track[x] or k in track[:, y] or k in track[a * 3 : a * 3 + 3, b * 3 : b * 3 + 3]: return False
            return True

        def backtrack(board, x, y):
            if x == m:
                return True
            if y == n:
                return backtrack(board, x + 1, 0)
            if board[x][y] != ".":
                return backtrack(board, x, y + 1)
            for k in range(1, 10):
                if check(board, x, y, str(k)):
                    board[x][y] = str(k)
                    if backtrack(board, x, y + 1):
                        return True  # 返回True 找到第一个解后直接返回结果。终止后续递归
                    board[x][y] = "."
            return False

        backtrack(board, 0, 0)
        return


        # 回溯  自己写的backtrack内部循环遍历
        count = 0
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    count += 1
        m, n = 9, 9

        def backtrack(board, x, count):  # x是行的起点，剪枝用的，就是上面填好的就不用遍历了，里面没有"."了，可以节省400ms时间
            if count == 0: return True
            for i in range(x, m):
                for j in range(n):
                    if board[i][j] != ".": continue
                    for k in range(1, 10):
                        if check(board, i, j, str(k)):
                            board[i][j] = str(k)
                            if backtrack(board, i, count - 1):
                                return True
                            board[i][j] = "."
                    return False
            return False

        backtrack(board, 0, count)
        return

        # 注释版本
        # 对 board[i][j] 进行穷举尝试
        def backtrack(board, i, j):
            m, n = 9, 9
            if j == n:  # 走到9才越界，进入下一行
                return backtrack(board, i + 1, 0)
            if i == m:  # 走到最后一行，找到一个可行解
                return True
            if board[i][j] != '.':  # 当前是预设数字，直接跳到下一个
                return backtrack(board, i, j + 1)

            ch_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            for ch in ch_list:
                if not isValid(board, i, j, ch):  # 如果遇到不合法的数字，则跳过
                    continue

                board[i][j] = ch  # 做选择
                if backtrack(board, i, j + 1):  # 如果找到一个可行解，立即结束
                    return True
                board[i][j] = '.'  # 撤销选择
            # 穷举完 1~9，依然没有找到可行解，此路不通
            return False

        # 判断 board[i][j] 是否可以填入 n
        def isValid(board, r, c, n):
            for i in range(9):
                # 判断行是否存在重复
                if board[r][i] == n: return False
                # 判断列是否存在重复
                if board[i][c] == n: return False
                # 判断 3 * 3 方框是否存在重复
                if board[(r // 3) * 3 + i // 3][(c // 3) * 3 + i % 3] == n:
                    return False
            return True

        backtrack(board, 0, 0)
import collections
class Solution:
    def slidingPuzzle(self, board):
        # https://leetcode-cn.com/problems/sliding-puzzle/solution/hua-dong-mi-ti-by-leetcode/
        '''
        BFS 模版
        queue = collections.deque([(start, 0)])
        seen = {start}
        while queue:
            node, depth = queue.popleft()
            if node == target: return depth
            for nei in neighbors(node):
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth+1))
        '''
        # BFS 模板套路 参考非递归便利二叉树 一样一样的
        m, n = len(board), len(board[0])
        board = tuple([x for i in range(m) for x in board[i]])
        queue = collections.deque([(board, board.index(0), 0)])
        target = tuple(list(range(1, m * n)) + [0])
        seen = {board}
        while queue:
            cur, idx, step = queue.popleft()
            if cur == target:
                return step
            for d in [-1, 1, n, -n]:
                new_idx = idx + d
                if abs(new_idx // n - idx // n) + abs(new_idx % n - idx % n) != 1: continue  # 比如 2+1=3,这种变换就不行
                if new_idx < 0 or new_idx >= m * n: continue
                new_board = list(cur)
                new_board[idx], new_board[new_idx] = new_board[new_idx], new_board[idx]
                new_board = tuple(new_board)
                if new_board not in seen:
                    seen.add(new_board)
                    queue.append((new_board, new_idx, step + 1))
        return -1

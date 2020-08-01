'''
你是一位施工队的工长，根据设计师的要求准备为一套设计风格独特的房子进行室内装修。
房子的客厅大小为 n x m，为保持极简的风格，需要使用尽可能少的 正方形 瓷砖来铺盖地面。
假设正方形瓷砖的规格不限，边长都是整数。
请你帮设计师计算一下，最少需要用到多少块方形瓷砖？

示例 1：
输入：n = 2, m = 3
输出：3
解释：3 块地砖就可以铺满卧室。
     2 块 1x1 地砖
     1 块 2x2 地砖

示例 2：
输入：n = 5, m = 8
输出：5

示例 3：
输入：n = 11, m = 13
输出：6
 
提示：
1 <= n <= 13
1 <= m <= 13
'''


class Solution:
    def __init__(self):
        self.memo = {}

    def tilingRectangle(self, n: int, m: int) -> int:
        # https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/discuss/630149/BFS_Python
        # BFS 看成[n] * m个 进行BFS
        if not m and not n:
            return 0
        heights = [n] * m
        count, leftmost = 0, 0
        q = deque([(count, heights, leftmost)])
        while q:
            count, heights, leftmost = q.popleft()
            if leftmost == m:
                return count
            w = m - leftmost
            h = heights[leftmost]
            bound = min(w, h)
            for x in range(bound, 0, -1):
                new_heights, new_leftmost = heights[:], leftmost
                for i in range(leftmost, leftmost + x):  # 添加一块正方形
                    new_heights[i] -= x
                    if new_heights[i] == 0:  # 如果有一列=0，就说明这列填满了 所以最左+1
                        new_leftmost += 1
                q.append((count + 1, new_heights, new_leftmost))  #
        return -1

        # Backtracking with memo (DP)
        # Note 2 things from the description:
        # 1. Range is bounded (<= 13)
        # 2. As the example shows, (11, 13) and (13, 11) is the only special case
        # all other cases can be solved by backtracking on subrectangles (divided along either long or short axis)

        # Total of 4 base cases
        # base-1: square
        if n == m: return 1

        # Always keep n < m to reduce space complexity of memoization
        if n > m: n, m = m, n

        # base-2: narrowest rectangle possible.
        if n == 1: return m

        # base-3: 11, 13 or 13, 11     这是个极端情况 说实话 想不明白
        if (n, m) == (11, 13): return 6

        # base-4: in memo
        if (n, m) in self.memo: return self.memo[(n, m)]

        ans = math.inf
        # Check both axes
        for i in range(1, m // 2 + 1):
            ans = min(ans, self.tilingRectangle(n, i) + self.tilingRectangle(n, m - i))
        for i in range(1, n // 2 + 1):
            ans = min(ans, self.tilingRectangle(i, m) + self.tilingRectangle(n - i, m))

        self.memo[(n, m)] = ans
        return ans

        # 自己写的暴力  但是11 13是错误的 这个是个特殊的例子，但是我觉得应该可以遍历到，不应该错误解答，不清楚
        def get_len(state, i, j):
            a, b = i, j
            while i < len(state) and j < len(state[0]) and a < len(state) and b < len(state[0]) and state[i][b] == 0 and \
                    state[a][j] == 0:
                a += 1
                b += 1
            return min(a - i, b - j)

        def fill(state, i, j, k):
            num = 0
            for x in range(i, i + k):
                for y in range(j, j + k):
                    state[x][y] = 1
                    num += 1
            return state, num

        def dp(state, num, count):
            if num == n * m:
                self.res = min(self.res, count)
                return
            for i in range(n):
                for j in range(m):
                    if state[i][j] == 0:
                        maxi = get_len(state, i, j)
                        for k in range(maxi, 0, -1):
                            new_state = state
                            new_state, add = fill(new_state, i, j, k)
                            dp(new_state, num + add, count + 1)

        self.res = float("inf")
        dp([[0 for _ in range(m)] for _ in range(n)], 0, 0)
        print(self.res)
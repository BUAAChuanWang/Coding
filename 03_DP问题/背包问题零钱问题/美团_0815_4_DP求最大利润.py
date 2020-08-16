'''
# 5辆车 A地需要2辆 B地需要2两
# 这5辆车到A B两地分别的利润
# 一辆车只能去一个地方，求利润最大
5 2 2
4 2
3 3
5 4
5 3
1 5

18
'''
import functools
while 1:
    n, A, B = list(map(int, input().split(" ")))
    profits = []
    for i in range(n):
        profits.append(list(map(int, input().split(" "))))

    # 我的
    @functools.lru_cache(None)
    def dp(a, b, index):
        # print(a, b, index)
        if a == 0 and b == 0: return 0
        res = 0
        for i in range(index, n):
            if a != 0 and b != 0:
                res = max(res, dp(a, b, i + 1), dp(a - 1, b, i + 1) + profits[i][0],
                          dp(a, b - 1, i + 1) + profits[i][1])
            elif a != 0:
                res = max(res, dp(a, b, i + 1), dp(a - 1, b, i + 1) + profits[i][0])
            elif b != 0:
                res = max(res, dp(a, b, i + 1), dp(a, b - 1, i + 1) + profits[i][1])
        return res
    t = dp(A, B, 0)
    print(t)

    # 唐心怡
    @functools.lru_cache(None)
    def dp(a, b, index):
        if a < 0 or b < 0: return float("-inf")
        if a == 0 and b == 0 or index == len(profits): return 0
        return max(dp(a - 1, b, index + 1) + profits[index][0],
                   dp(a, b - 1, index + 1) + profits[index][1],
                   dp(a, b, index + 1))
    print(dp(A, B, 0))

# 不好的做法
# import functools
#
# while 1:
#     n, A, B = list(map(int, input().split(" ")))
#     profits = []
#     for i in range(n):
#         profits.append(list(map(int, input().split(" "))))
#
#     # visited = set()
#
#     @functools.lru_cache(None)
#     def dp(a, b, visited):
#         visited = list(visited)
#         # print(a, b, visited)
#         if a == 0 and b == 0:
#             return 0
#         res = 0
#         for i in range(n):
#             if i in visited: continue
#             visited.append(i)
#             visited = tuple(visited)
#             if a != 0 and b != 0:
#                 res = max(res, dp(a - 1, b, visited) + profits[i][0], dp(a, b - 1, visited) + profits[i][1],
#                           dp(a, b, visited))
#             elif a != 0:
#                 res = max(res, dp(a - 1, b, visited) + profits[i][0], dp(a, b, visited))
#             elif b != 0:
#                 res = max(res, dp(a, b - 1, visited) + profits[i][1], dp(a, b, visited))
#             visited = list(visited)
#             visited.pop()
#         return res
#     t = dp(A, B, ())
#     print(t)

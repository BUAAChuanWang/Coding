def func():
    while 1:
        # 输入
        # n, m, q = list(map(lambda x : int(x), input().split(" ")))
        # board = []
        # query = []
        # for i in range(n):
        #     board.append(list(input().split()))
        # for i in range(q):
        #     query.append(list(map(lambda x:int(x)-1, input().split())))
        # print(n, m, q)
        # print(board)
        # print(query)
        n, m, q = 4, 4, 2
        board = [['C', 'C', 'C', 'S'], ['S', 'S', 'S', 'S'], ['C', 'S', 'C', 'S'], ['S', 'S', 'C', 'C']]
        query = [[0, 0, 2, 3], [2, 0, 0, 2]]
        import functools
        for q in query:
            res = float("inf")
            bx, by, ex, ey = q
            visited = [[0 for _ in range(m)]for _ in range(n)]
            functools.lru_cache(None)
            def dp(x, y, cost):
                # print(x, y, cost)
                nonlocal res, visited
                if x == ex and y == ey:
                    res = min(res, cost)
                    return
                for a, b in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    new_x, new_y = x + a, y + b
                    if n > x + a >= 0 and m > y + b >= 0 and not visited[new_x][new_y]:
                        visited[new_x][new_y] = 1
                        if board[new_x][new_y] == board[x][y]:
                            if board[new_x][new_y] == "S":
                                dp(new_x, new_y, cost + 2)
                            elif board[new_x][new_y] == "C":
                                dp(new_x, new_y, cost + 3)
                        else:
                            dp(new_x, new_y, cost + 5)
                        visited[new_x][new_y] = 0
            dp(bx, by, 0)
            print(res)
        break
func()
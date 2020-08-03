'''
5 1 9
9 1
4 9
3 1
2 3
6 5
9 8

4

1 1 0
3 1
2 1

0
'''
import sys
import functools
import bisect
if __name__ == "__main__":
    # 读取第一行的n
    N, M, T = list(map(int, sys.stdin.readline().strip().split(" ")))
    if T == 0:
        print(0)

    else:
        lunch, dinner = [], []
        for i in range(N):
            lunch.append(list(map(int, sys.stdin.readline().strip().split(" "))))
        for i in range(M):
            dinner.append(list(map(int, sys.stdin.readline().strip().split(" "))))
        lunch = [[0, 0]] + lunch
        dinner = [[0, 0]] + dinner
        lunch = sorted(lunch, key=lambda x: (-x[1], x[0]))
        dinner = sorted(dinner, key=lambda x: (-x[1], x[0]))
        print(lunch, dinner)
        res = float("inf")
        i, j = 0, 0
        while i < N + 1:
            # j = bisect.bisect_left(dinner, T - h1)
            j = 0
            while j < M + 1 and lunch[i][1] + dinner[j][1] >= T:
                res = min(res, lunch[i][0] + dinner[j][0])
                while j < M and dinner[j][1] == dinner[j + 1][1]:
                    j += 1
                j += 1
            while i < N and lunch[i][1] == lunch[i + 1][1]:
                i += 1
            i += 1
        print(res)
        '''
        for i in range(N + 1):
            x, y = lunch[i]  # HEAT, YUMMY
            for j in range(M + 1):
                a, b = dinner[j]
                if y + b < T:
                    continue
                else:
                    res = min(res, x + a)
                    print(x, a)
        print(res)
        '''
        '''
        @functools.lru_cache(None)
        def dp(t, heat, index1, index2):
            # print(t, heat)
            global res
            if t >= T:
                return heat
            for i in range(index1, N + 1):
                x, y = lunch[i]  # HEAT, YUMMY
                for j in range(index2, M + 1):
                    a, b = dinner[j]
                    if y + b < T:
                        continue
                    else:
                        res = min(res, x + a)
                    # res = min(res, dp(t + y + b, heat + x + a, i + 1, j + 1))
            return res
        dp(0, 0, 0, 0)
        print(res)
        '''
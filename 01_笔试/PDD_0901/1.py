'''
5

0 2 0 1 0
3 0 0 0 8
0 0 0 0 0
4 0 0 0 7
0 5 0 6 0
'''
import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(input())
    res = [[0 for _ in range(n)]for _ in range(n)]
    mid = n // 2
    for i in range(n):
        for j in range(n):
            if i < mid and j >= mid:
                if i + j < n - 1:
                    res[i][j] = 1
                if i + j > n - 1:
                    res[i][j] = 8
            if i < mid and j < mid:
                if i < j:
                    res[i][j] = 2
                if i > j:
                    res[i][j] = 3
            if i >= mid and j < mid:
                if i + j < n - 1:
                    res[i][j] = 4
                if i + j > n - 1:
                    res[i][j] = 5
            if i >= mid and j >= mid:
                if i < j:
                    res[i][j] = 7
                if i > j:
                    res[i][j] = 6
    if n % 2 != 0:
        mid = n // 2
        for i in range(n):
            res[i][mid] = 0
        for i in range(n):
            res[mid][i] = 0
    for i in range(n):
        print(" ".join(map(str, res[i])))
    # print(res)
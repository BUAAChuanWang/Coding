while 1:
    N, M = input().split(" ")
    N, M = int(N), int(M)
    li = list(map(int, input().split(" ")))
    # 二分
    l, r = 0, sum(li)

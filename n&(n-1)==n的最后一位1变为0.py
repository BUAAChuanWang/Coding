while 1:
    n = int(input())
    res = 0
    while n:
        res += 1
        n = n & (n - 1)
    print(res)
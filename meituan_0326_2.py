import math
while 1:
    n = int(input())
    ri = list(map(int, input().split(" ")))

    r2 = 0
    sign = 1
    i = 0
    while n > 0:
        r2 += sign * (ri[i] ** 2)
        n, i ,sign = n - 1, i + 1, -1 * sign
    print(math.pi * r2)
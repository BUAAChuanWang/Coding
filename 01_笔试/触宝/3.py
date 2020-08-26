'''
4
1 2 5 10
17

1
'''
# AC 85.71
import sys
if __name__ == "__main__":
# while 1:
    n = int(sys.stdin.readline().strip())
    cost = list(map(int, sys.stdin.readline().strip().split(" ")))
    m = int(sys.stdin.readline().strip())
    cost.sort()
    if n % 2:
        t = cost[0]
        for i in range(1, len(cost) - 1, 2):
            t += max(cost[i], cost[i + 1])
    else:
        t = 0
        for i in range(0, len(cost) - 1, 2):
            t += max(cost[i], cost[i + 1])
    res = 1 if t <= m else 0
    print(res, t)
    # def dp()

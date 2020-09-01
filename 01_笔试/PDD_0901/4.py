'''
10 1
2

5

10 2
2
3

7

10 3
2
3
5

8
'''
import sys
if __name__ == "__main__":
    # 读取第一行的n
    n, m = list(map(lambda x:int(x), sys.stdin.readline().strip().split()))
    mlist = []
    for i in range(m):
        mlist.append(int(input()))
    # mlist.sort()
    new = []
    for m in mlist:
        flag = True
        for i in range(2, m):
            if m % i == 0:
                flag = False
                break
        if flag: new.append(m)

    count = 0
    for m in new:
        count += n // m

    for i in range()
    h = set()
    for i in range(1, n + 1):
        for j in new:
            if i % j == 0:
                h.add(i)
    print(len(h))
    # def func(n, mlist):
    #     count = 0
    #     for m in mlist:
    #         count += n // m
    #
    #     for i in range(len(mlist)):
    #         for j in range(i + 1, len(mlist)):
    #             if
    #             x, y = mlist[i], mlist[j]
    #             x = min(x, y)
    #             y = max(x, y)
    #             if y % x == 0:
    #                 count -= n // y
    #             else:
    #                 count -= n // (x * y)
    #             # count -= n // (mlist[i] * mlist[j])
    #     return count
    # res = func(n, mlist)
    # print(res)
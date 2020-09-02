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

8 3
2
3
3

5
'''
import sys, math
# 计算最大公约数
def gcd(a, b):
    return gcd(b, a % b) if b > 0 else a
# 计算最小公倍数
def lcm(a, b):
    return (a * b) // math.gcd(a, b)
# if __name__ == "__main__":
while 1:
    # 读取第一行的n
    n, m = list(map(lambda x:int(x), sys.stdin.readline().strip().split()))
    mlist = []
    for i in range(m):
        mlist.append(int(input()))
    mlist = list(mlist)
    cnt = 0
    flag = 1
    while mlist:
        for m in mlist:
            cnt += flag * (n // m)
        print(f"mlist:{mlist}, cnt:{cnt}, flag:{flag}")
        mlist = list(set(mlist))
        new_mlist = []
        for i in range(len(mlist)):
            for j in range(i + 1, len(mlist)):
                t = lcm(mlist[i], mlist[j])
                if t <= n: new_mlist.append(t)
        flag = -flag
        mlist = new_mlist
    print(cnt)
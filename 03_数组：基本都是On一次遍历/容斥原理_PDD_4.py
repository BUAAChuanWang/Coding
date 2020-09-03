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

    # 以下代码求 [1,n]区间中 能被mlist中的任意m整数的数字的个数
    # 容斥原理，求所有m的集合，在这个集合的所有数，求一下lcm（最小公倍数），如果|集合|是奇数，ans+=n/lcm，否则ans-=n/lcm 。
    ans = 0
    # print("1<<m", 1<<m)
    for i in range(1, 1 << m):  # 排列组合 每一个数字都有选和不选两种
        # print(f"i={i}")
        cnt = 0
        for j in range(m):  # 把m个数变成二进制的形式进行与操作就是排列组合
            # print(f"j={j}, 1<<j={1<<j}, i & (1 << j)={i & (1 << j)}")
            if i & (1 << j):
                cnt += 1
                if cnt == 1:
                    gd = mlist[j]
                else:
                    gd = gd * mlist[j] // math.gcd(mlist[j], gd)  # 当前集合的最大公倍数
                # print(f"gd={gd}")
        if cnt & 1:  # 奇数个就+
            ans += n // gd
            # print(f"cnt&1: ans={ans}")
        else:  # 偶数个就-
            ans -= n // gd
            # print(f"cnt&1=0: ans={ans}")
    print(ans)


    # 以下代码求 [1,n]区间中 能被mlist中的任意m整数的数字的个数
    def rongchi_count(n, mlist):
        ans = 0
        m = len(mlist)
        for i in range(1, 1 << m):
            cnt = 0
            for j in range(m):
                if i & (1 << j):
                    cnt += 1
                    if cnt == 1:
                        gd = mlist[j]
                    else:
                        gd = gd * mlist[j] // math.gcd(gd, mlist[j])
            if cnt & 1:
                ans += n // gd
            else:
                ans -= n // gd
        return ans
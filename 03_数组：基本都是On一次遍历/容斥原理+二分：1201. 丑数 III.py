'''
请你帮忙设计一个程序，用来找出第 n 个丑数。
丑数是可以被 a 或 b 或 c 整除的 正整数。

示例 1：

输入：n = 3, a = 2, b = 3, c = 5
输出：4
解释：丑数序列为 2, 3, 4, 5, 6, 8, 9, 10... 其中第 3 个是 4。
示例 2：

输入：n = 4, a = 2, b = 3, c = 4
输出：6
解释：丑数序列为 2, 3, 4, 6, 8, 9, 10, 12... 其中第 4 个是 6。
示例 3：

输入：n = 5, a = 2, b = 11, c = 13
输出：10
解释：丑数序列为 2, 4, 6, 8, 10, 11, 12, 13... 其中第 5 个是 10。
示例 4：

输入：n = 1000000000, a = 2, b = 217983653, c = 336916467
输出：1999999984
'''
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        import math
        # 计算最小公倍数
        def lcm(a, b):
            return (a * b) // math.gcd(a, b)

        # 以下代码求 [1,n]区间中 能被mlist中的任意m整数的数字的个数   可查看pycharm中03_数组/容斥原理
        def rongchi_count(n, mlist):  # 可以是多个数字不止3个都可以计算
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

        l, r = 0, min(a, b, c) * n + 1
        while l < r:
            mid = l + (r - l) // 2
            cnt = rongchi_count(mid, [a, b, c])
            # print(f"n={n}, l={l}, r={r}, mid={mid}, cnt={cnt}")
            if cnt < n:
                l = mid + 1
            else:
                r = mid
        return l

        # 应对本题三个数字的容斥原理 可以直接写公式
        l, r = 0, min(a, b, c) * n + 1
        while l < r:
            mid = l + (r - l) // 2
            cnt = mid // a + mid // b + mid // c - mid // lcm(a, b) - mid // lcm(a, c) - mid // lcm(b, c) + mid // lcm(lcm(a, b), c)
            if cnt < n:
                l = mid + 1
            else:
                r = mid
        return l
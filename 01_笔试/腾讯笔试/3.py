import sys
# if __name__ == "__main__":
import math
while 1:
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    if n == 1: print(1)
    else:
        mod = 10 ** 9 + 7
        # 快速幂 a >= 1
        def quickpower(x, a):
            global mod
            res = 1
            while a > 0:
                if a % 2: res *= x
                x = (x * x) % mod  # 虽然不能用幂函数的库函数 但是这里只是做平方乘积，为了快速幂的标准写法，所以还是用**2，用x*x也是一样的。
                a //= 2
            return res

        ans = (quickpower(2, n - 1) * n) % mod
        print(ans)

        # ========
        # 超时 AC30
        def C(a, b):
            if b == 0: return 1
            if b > a / 2:
                b = a - b
            fenzi, fenmu = 1, 1
            for i in range(a, a - b, -1):
                fenzi *= i
            for i in range(1, b + 1):
                fenmu *= i
            return fenzi // fenmu
        # print(C(3,1))
        res = 0
        mod = 10 ** 9 + 7
        for i in range(1, n + 1):
            res += ((i % mod) * (C(n, i) % mod)) % mod
            res %= mod
        print(res)
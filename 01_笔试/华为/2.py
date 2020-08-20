'''
4
1 0 2 2

2
'''
import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    depth = list(map(lambda x:int(x), sys.stdin.readline().strip().split(" ")))

    depth.sort()
    count = 1
    dic = {}
    for i, d in enumerate(depth):
        dic[d] = dic.get(d, 0) + 1
    # print(dic)

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

    res = 1
    pre = dic[0]
    mod = 10 ** 9 + 7
    for k, v in dic.items():
        if k == 0: continue
        t1 = res % mod
        t2 = C(2 * pre, v) % mod
        res = (t1 * t2) % mod
        pre = v
    print(res)


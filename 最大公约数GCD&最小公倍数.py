while 1:
    # GCD 辗转相除法  最大公约数
    a, b = list(map(int, input().split(" ")))

    def GCD(a, b):
        r = a % b
        while r:
            a = b
            b = r
            r = a % b
        return b
    print(GCD(a, b))

    # 最小公倍数 = a * b / 最大公约数
    def min_gongbeishu(a, b):
        return a * b // GCD(a, b)
    print(min_gongbeishu(a, b))
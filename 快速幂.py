while 1:
    # 求x**a   若非python语言则存在大数越界问题，并且时间复杂度上快速幂logn更佳
    x = int(input())
    a = int(input())

    # 快速幂 a >= 1
    def quickpower(x, a):
        res = 1
        while a > 0:
            if a % 2: res *= x
            x = x ** 2  # 虽然不能用幂函数的库函数 但是这里只是做平方乘积，为了快速幂的标准写法，所以还是用**2，用x*x也是一样的。
            a //= 2
        print(res)
    # quickpower(x, a)

    # 递归写法
    def quickpower(x, a):
        if a == 0: return 1
        res = 1
        if a % 2 == 1:
            return x * quickpower(x, a - 1)
        else:
            sub = quickpower(x, a// 2)
            return sub * sub
    res = quickpower(x, a)
    print(res)
def func():
    while 1:
        n, m = input().split(" ")
        n, m = int(n), int(m)
        res = 1
        # 求 C(a, b)
        def get_C(a, b):
            if a > b // 2:
                a = b - a
            fenzi, fenmu = 1, 1
            for i in range(b, b - a, -1):
                fenzi *= i
            for i in range(1, a + 1):
                fenmu *= i
            return fenzi // fenmu
        print("c:", get_C(2, 5))

        for i in range(1, n + 1):
            res += get_C(i, n) * m ** i
        print(res % 10 ** 9)
func()
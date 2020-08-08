import functools
while 1:
    @functools.lru_cache(None)
    def func(n):
        if n < 0:
            return 0
        return min(func(n - 2) + b[n - 1], func(n - 1) + a[n])
    a = [20, 25, 30]
    b = [40, 30]
    N = len(a)
    diff = func(N - 1)
    print(diff)
    break
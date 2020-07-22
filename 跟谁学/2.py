'''
给一个大于2的偶数，找出两个质数的和为该数字
'''

def goldbach_conjecture(even_integer, x=None, y=None):
    # 判断是否质数
    def is_even(num):
        if num == 1: return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    # 寻找两个和为even_integer的数
    for i in range(even_integer // 2 + 1):
        j = even_integer - i
        if i % 2 == 0 or j % 2 == 0: continue
        if is_even(i) and is_even(j):
            x, y = i, j
            print(x, y)
            return x, y
    print(-1, -1)
    return -1, -1

# goldbach_conjecture(14)
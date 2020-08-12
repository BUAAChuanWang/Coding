def f(n, x):
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'b', 'C', 'D', 'E', 'F', "G", "H", "I", \
         "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    res = []
    while True:
        shang, yushu = n // x, n % x
        res = res + [yushu]
        if shang == 0:
            break
        n = shang
    ans = ""
    for i in res[::-1]:
        ans += str(a[i])
    print(ans)
f(44, 8)
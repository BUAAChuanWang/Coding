a = "0010010"
print(a.count("0010"))
print("0010" not in a)
'''
3
0123456789ABCDEF
001023456789ABCDEF00
0010010
'''
while 1:
    T = int(input())
    res = []
    for _ in range(T):
        # num = input()
        num = "0010" * 500

        ans = 0
        while num.find("0010") != -1:
            t = num.find("0010")
            num = num[t + 3 : ]  # 计算有几个"0010"
            ans += 1
        res.append(ans)
    for i in range(T):
        print(res[i])



while 1:
    T = int(input())
    res = []
    for i in range(T):
        num = input()
        # num = "0010" * 500

        queue = [(num, 0)]
        seen = {num}  # ********
        while queue:
            cur, step = queue.pop(0)
            if "0010" not in cur:
                res.append(step)
                break
            idx = cur.index("0010")
            for j in range(idx, idx + 4):
                new_cur = cur[ : j] + cur[j + 1 : ]  # ********
                if new_cur not in seen:  # ********
                    seen.add(new_cur)  # 2222222222
                    queue.append((new_cur, step + 1))  # ********

    for i in range(T):
        print(res[i])


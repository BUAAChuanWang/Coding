'''
10 10

[[7,9],[1,1],[8,2],[7,5],[4,4]]
'''
import sys

if __name__ == "__main__":
    t = sys.stdin.readline().strip().split(" ")
    if len(t) != 2:
        print("[]")
    else:
        m, n = t
        if m < "10" or m > "1000" or n < "10" or n > "1000":
            print("[]")
        else:
            m, n = int(m), int(n)
            l, r, t, b = 0, n - 1, 0, m - 1
            count = 0
            res = []
            flag = False
            while 1:
                for i in range(l, r + 1):
                    count += 1
                    if count % 10 == 7 and count // 10 % 10 % 2 == 1:
                        res.append([t, i])
                t += 1
                if t > b: break

                for i in range(t, b + 1):
                    count += 1
                    if count % 10 == 7 and count // 10 % 10 % 2 == 1:
                        res.append([i, r])
                r -= 1
                if r < l: break

                for i in range(r, l - 1, -1):
                    count += 1
                    if count % 10 == 7 and count // 10 % 10 % 2 == 1:
                        res.append([b, i])
                b -= 1
                if t > b: break

                for i in range(b, t - 1, -1):
                    count += 1
                    if count % 10 == 7 and count // 10 % 10 % 2 == 1:
                        res.append([i, l])
                l += 1
                if l > r: break
            res = str(res).replace(" ", "")
            # sys.stdout.write(res)
            print(res, end='')
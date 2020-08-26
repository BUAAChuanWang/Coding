'''
input:
1 2 2 3
3 2
output:
3 2 2 1
input:
1 2 3 4 5 6 7
3 6 5
output:
3 6 5 1 2 4 7
input:
12 45
23
output:
12 45
'''
import sys
if __name__ == "__main__":
# while 1:
    a = list(map(lambda x: int(x), sys.stdin.readline().strip().split(" ")))
    b = list(map(lambda x: int(x), sys.stdin.readline().strip().split(" ")))
    sb = set(b)
    res = []
    t1, t2 = {}, []
    for c in a:
        if c in sb:
            t1[c] = t1.get(c, 0) + 1
        else:
            t2.append(c)
    for c in b:
        res += [c for _ in range(t1[c])]

    t2.sort()
    res += t2
    print(" ".join(list(map(str, res))))
'''
2
1 2 3 4 5 6
1 2 6 5 3 4

1
2


3
1 2 3 4 5 6
1 2 6 5 3 4
1 2 3 4 6 5

2
2 1

4
1 5 6 3 4 2
5 1 4 2 6 3
6 2 3 1 5 4
5 3 6 1 4 2

3
2 1 1

10
2 5 1 3 4 6
5 4 3 2 1 6
1 4 6 2 3 5
1 5 6 3 4 2
6 4 2 1 5 3
3 6 4 5 2 1
1 6 3 4 2 5
5 1 4 2 6 3
6 2 3 1 5 4
5 3 6 1 4 2
'''
import sys
if __name__ == "__main__":
    # 读取第一行的n
    ans = 0
    N = int(sys.stdin.readline().strip())
    touzi = []
    for i in range(N):
        touzi.append(list(map(lambda x:int(x), sys.stdin.readline().strip().split())))

    def reverse(t):
        return[t[1], t[0]]

    def check(i, j):
        t1, t2 = touzi[i], touzi[j]
        if t1 == t2: return True
        tb1, lr1, fb1 = touzi[i][:2], touzi[i][2:4], touzi[i][4:]
        tb2, lr2, fb2 = touzi[j][:2], touzi[j][2:4], touzi[j][4:]
        swap = set()
        reve = set()
        a = [tb1, lr1, fb1]
        b = [tb2, lr2, fb2]
        # print("a, b:", a, b)
        for i in range(len(a)):
            for j in range(len(b)):
                if reverse(a[i]) == b[j]:
                    # print("rever in :", a[i])
                    if i > j:
                        if (j, i) not in reve:
                            reve.add((j, i))
                    else:
                        if (i, j) not in reve:
                            reve.add((i, j))
                    if j != i:
                        if i > j:
                            if (j, i) not in swap:
                                swap.add((j, i))
                        else:
                            if (i, j) not in swap:
                                swap.add((i, j))
                    break
                elif a[i] == b[j]:
                    if i != j:
                        if i > j:
                            if (j, i) not in swap:
                                swap.add((j, i))
                        else:
                            if (i, j) not in swap:
                                swap.add((i, j))
                    break
        # print(reve, swap)
        if len(swap) == 1 and len(reve) == 1:
            return True
        else:
            return False

    seen = set()
    cate = []
    for i in range(N):
        if i not in seen:
            tmp = [i]
            cur = touzi[i]
            seen.add(i)
            for j in range(i + 1, N):
                if j not in seen:
                    if check(i, j):
                        seen.add(j)
                        tmp.append(j)
            cate.append(len(tmp))
    cate = sorted(cate, reverse=True)
    print(len(cate))
    # print(cate)
    for i in range(len(cate)):
        print(cate[i], end=" ")



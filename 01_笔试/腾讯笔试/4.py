'''
4 3
1 2
2 3
2 4

3
'''
import sys
if __name__ == "__main__":
    def C(a, b):
        if b == 0: return 1
        if b > a / 2:
            b = a - b
        fenzi, fenmu = 1, 1
        for i in range(a, a - b, -1):
            fenzi *= i
        for i in range(1, b + 1):
            fenmu *= i
        return fenzi // fenmu


    n, m = sys.stdin.readline().strip().split(" ")
    n, m = int(n), int(m)
    graph = []
    for i in range(m):
        graph.append(list(map(int, sys.stdin.readline().strip().split(" "))))
    import collections
    dic = collections.defaultdict(list)
    for i in range(m):
        a, b = graph[i]
        dic[a].append(b)
        dic[b].append(a)
    # print(dic)

    h = {}
    for k, v in dic.items():
        t = tuple(sorted(v))
        h[t] = h.get(t, 0) + 1

    res = 0
    for val in h.values():
        if val < 2: continue
        res += C(val, 2)
    print(res)
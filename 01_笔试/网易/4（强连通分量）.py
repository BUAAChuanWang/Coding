'''
第4题，a教授认可b教授，b教授认可c教授，那么a也认可c。
现有n (小于50000)个教授，m（小于600000）个认可，可能自己认可自己，也可能重复。
求，互相认可的教授有多少，多少对？
5 6
1 3
2 1
3 2
3 5
4 5
5 4

4
'''
import sys, collections, copy
if __name__ == "__main__":
    # https://blog.csdn.net/weixin_43843835/article/details/88381828
    # Tarjan算法 计算强连通分量
    N, M = list(map(lambda x:int(x), sys.stdin.readline().strip().split()))
    nums = []
    for i in range(M):
        nums.append(list(map(lambda x:int(x), sys.stdin.readline().strip().split())))

    graph = collections.defaultdict(list)
    for i in range(len(nums)):
        graph[nums[i][0]].append(nums[i][1])
    print(graph)

    dfn = [0 for _ in range(N + 1)]
    scg = [i for i in range(N + 1)]
    stack = []
    index = 0
    visited = set()
    def dfs_tarjan(u):
        global index
        index += 1
        dfn[u], scg[u] = index, index
        stack.append(u)
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                dfs_tarjan(v)
                scg[u] = min(scg[u], scg[v])
            elif v in visited:
                scg[u] = min(scg[u], scg[v])

        if dfn[u] ==scg[u]:
            v = stack.pop()
            while u != v:
                v = stack.pop()

    start = graph.keys()[0]
    dfs_tarjan(start)

    SCG = collections.defaultdict(list)
    for i in range(1, N + 1):
        SCG[scg[i]].append(i)
    res = 0
    for k, v in SCG.items():
        res += len(v) * (len(v) - 1) // 2
    print(dfn)
    print(scg)
    print(SCG)
    print(res)

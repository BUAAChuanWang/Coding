'''
5 3 2
1 2 1
2 3 1
3 4 1
4 5
1 2

2
'''
import sys
if __name__ == "__main__":
# while 1:
    n, m, k = list(map(int, sys.stdin.readline().strip().split(" ")))
    dis = []
    for i in range(m):
        dis.append(list(map(int, sys.stdin.readline().strip().split(" "))))
    tp = set()
    for i in range(k):
        tp.add(tuple(list(map(int, sys.stdin.readline().strip().split(" ")))))
    # print("0")
    import collections, heapq
    graph = collections.defaultdict(list)
    for u, v, w in dis:
        if (u, v) in tp:
            tp.remove((u, v))
            graph[u].append((v, 0))
        else:
            graph[u].append((v, w))
        graph[v].append((u, w))
    for u, v in tp:
        graph[u].append((v, 0))
    # dist是一个dic，表示从源节点到每个节点的距离
    priorityq = [(0, 1)]  # weight, node  表示：起点K到K的距离是0， weight在前便于heapq排序
    dist = {}
    while priorityq:
        d, cur = heapq.heappop(priorityq)  # 每次都取出距离原点最近的w的点 利用了堆得性质
        if cur in dist: continue
        dist[cur] = d
        for nei, w in graph[cur]:
            # print(cur, nei)
            if nei not in dist:  # 这里再做一次重复筛选，如果在dist中就不加入优先队列了，因为之前的一定是距离最短的
                heapq.heappush(priorityq, (d + w, nei))
    # print(dist)
    print(dist[n])
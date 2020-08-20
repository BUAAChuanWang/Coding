'''
有 N 个网络节点，标记为 1 到 N。

给定一个列表 times，表示信号经过有向边的传递时间。 times[i] = (u, v, w)，其中 u 是源节点，v 是目标节点，
w 是一个信号从源节点传递到目标节点的时间。

现在，我们从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1。

 

示例：



输入：times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
输出：2
'''

import collections, heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # https://leetcode-cn.com/problems/network-delay-time/solution/java-ban-dijkstra-spfa-floydxiang-xi-ti-jie-by-jer/
        # DJISTRA 堆写法
        # djstra用于单源的最短距离 ；代码源自官解   ；
        # 堆写法：推荐！！！
        # 构建图标准写法 用dic  本题是个有向图
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        # dist是一个dic，表示从源节点到每个节点的距离
        priorityq = [(0, K)]  # weight, node  表示：起点K到K的距离是0， weight在前便于heapq排序
        dist = {}
        while priorityq:
            d, cur = heapq.heappop(priorityq)  # 每次都取出距离原点最近的w的点 利用了堆得性质
            if cur in dist: continue
            dist[cur] = d
            for nei, w in graph[cur]:
                if nei not in dist:  # 这里再做一次重复筛选，如果在dist中就不加入优先队列了，因为之前的一定是距离最短的
                    heapq.heappush(priorityq, (d + w, nei))
        return max(dist.values()) if len(dist) == N else -1

        # https://leetcode-cn.com/problems/network-delay-time/solution/743-wang-luo-yan-chi-shi-jian-dijkstra-suan-fa-by-/
        # SPFA   可以处理负权值边
        # DJISTRA不能处理负权重的边的最短路径问题，SPFA可以，只需要一点点改变就好。
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        pq = [(0, K)]  # 这里没必要用堆对w权重排序了，因为下面是吧所有结果都对dist更新的，就是所有令居都遍历一次，所以排序反而还多了时间复杂度
        dist = {i: float("inf") for i in range(1, N + 1)}
        dist[K] = 0
        while queue:
            d, cur = pq.pop(0)  # 主要区别在这里，djstra是贪心的，选择最小权值以后就加入dist然后判断if cur in dist: continue不在后续的更新了
            for nei, w in graph[cur]:
                if d + w < dist[nei]:
                    dist[nei] = d + w  # 这里是重复的更新，所以就能处理负权值的最小值
                    queue.append((dist[nei], nei))
        return max(dist.values()) if len(dist) == N else -1

        # 非堆的正常写法 djistra  不推荐
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {node: float('inf') for node in range(1, N + 1)}
        seen = [False] * (N + 1)
        dist[K] = 0
        print(dist)

        while True:
            cand_node = -1
            cand_dist = float('inf')
            for i in range(1, N + 1):
                if not seen[i] and dist[i] < cand_dist:
                    cand_dist = dist[i]
                    cand_node = i

            if cand_node < 0: break
            seen[cand_node] = True
            for nei, d in graph[cand_node]:
                dist[nei] = min(dist[nei], dist[cand_node] + d)

        ans = max(dist.values())
        return ans if ans < float('inf') else -1
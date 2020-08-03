'''
给你一个由 n 个节点（下标从 0 开始）组成的无向加权图，该图由一个描述边的列表组成，其中 edges[i] = [a, b] 表示连接节点 a 和 b 的一条无向边，且该边遍历成功的概率为 succProb[i] 。

指定两个节点分别作为起点 start 和终点 end ，请你找出从起点到终点成功概率最大的路径，并返回其成功概率。

如果不存在从 start 到 end 的路径，请 返回 0 。只要答案与标准答案的误差不超过 1e-5 ，就会被视作正确答案。

 示例 1：

输入：n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
输出：0.25000
解释：从起点到终点有两条路径，其中一条的成功概率为 0.2 ，而另一条为 0.5 * 0.5 = 0.25
'''


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        if not n or not edges or not edges[0] or not succProb or not succProb[0]: return 0
        import collections, heapq
        # dijkstra算法
        # 构造无向图
        mem = collections.defaultdict(list)
        for (u, v), p in zip(edges, succProb):
            mem[u].append((v, p))
            mem[v].append((u, p))

        # 表示从起点开始到每个点的最大概率
        dist = [0 for _ in range(n)]
        visitd = [False for _ in range(n)]

        # 需要构造一个优先队列来辅助实现
        queue = []
        heapq.heappush(queue, (-1, start))
        dist[start] = 1

        while (queue):
            maxprob, u = heapq.heappop(queue)
            if visitd[u]:
                continue
            visitd[u] = True

            for v, p in mem[u]:
                new_prob = - (p * maxprob)
                if dist[v] < new_prob:
                    dist[v] = new_prob
                    heapq.heappush(queue, (-dist[v], v))

        return dist[end]

        '''
        # BFS
        adj = collections.defaultdict(list)
        for e, p in zip(edges, succProb):
            adj[e[0]].append((e[1], p))
            adj[e[1]].append((e[0], p))

        self.prob = 0
        seen = {start:1}    # node:prob
        queue = [(start, 1)]
        while queue:
            cur_node, cur_prob = queue.pop(0)
            if cur_node == end:
                self.prob = max(self.prob, cur_prob)
                continue
            for nei, p in adj[cur_node]:
                new_prob = cur_prob * p
                if new_prob > self.prob and (nei not in seen or new_prob > seen[nei]):
                    seen[nei] = new_prob
                    queue.append((nei, new_prob))
        return self.prob
        '''
        '''
        # DFS 具体思路是DFS+heapq   已经不能再优化了  要么超时 要么错误解答 我淦！ 
        import heapq
        adj = collections.defaultdict(list)
        for e, p in zip(edges, succProb):
            heapq.heappush(adj[e[0]], (-p, e[1]))    # 这里是大顶堆
            heapq.heappush(adj[e[1]], (-p, e[0]))

        seen = {start:1}    # node:prob
        self.prob = 0
        def backtrack(track, prob):
            # print(track, prob)
            if track[-1] == end:
                self.prob = max(self.prob, prob)
                return
            if prob <= self.prob:
                return
            for _ in range(len(adj[track[-1]])):
                p, nei = heapq.heappop(adj[track[-1]])
                new_prob = -p * prob
                if new_prob > self.prob and (nei not in seen or new_prob > seen[nei]):
                    seen[nei] = new_prob
                    backtrack(track + [nei], new_prob)
            return 
        backtrack([start], 1)
        return self.prob
        '''
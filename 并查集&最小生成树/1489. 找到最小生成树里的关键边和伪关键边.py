'''
https://leetcode-cn.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/
'''


# 标准化UF作业 + Kruskal算法生成最小生成树
# https://leetcode-cn.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/solution/kruskalbing-cha-ji-jie-fa-pythonshi-xian-by-java_l/
# https://leetcode-cn.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/solution/pythonzui-xiao-sheng-cheng-shu-kruskal-by-dreamcat/
class UnionFind:
    def __init__(self, n):
        self.count = n
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def find(self, p):
        dummy = p
        while self.parent[p] != p:
            p = self.parent[p]
        # 路径压缩
        while self.parent[dummy] != p:
            tmp = self.parent[dummy]
            self.parent[dummy] = p
            dummy = tmp
        return p

    def union(self, p, q):
        rootp = self.find(p)
        rootq = self.find(q)
        if rootp == rootq:
            return
        # 按秩合并
        if self.size[rootp] > self.size[rootq]:
            self.parent[rootq] = rootp
        else:
            self.parent[rootp] = rootq
        self.count -= 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def count(self):
        return self.count


class Solution:
    # kruskal算法最小生成树
    def kruskal(self, n, edges, must_contain_edge=None):
        uf = UnionFind(n)
        edges_cnt, min_cost = 0, 0
        if must_contain_edge is not None:
            p, q, w = must_contain_edge
            uf.union(p, q)
            min_cost, edges_cnt = w, 1
        for i in range(len(edges)):
            p, q, w = edges[i]
            if uf.connected(p, q):
                continue
            uf.union(p, q)
            min_cost += w
            edges_cnt += 1
            if edges_cnt == n - 1:
                break
        return min_cost if edges_cnt == n - 1 else float("inf")

    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        indices = sorted(range(len(edges)), key=lambda x: edges[x][2])  # 保留原来的index, 按index再去排序 而不是直接排序
        edges = [edges[x] for x in indices]
        ans = [[], []]
        self.min_cost = self.kruskal(n, edges)
        for i in range(len(edges)):
            if self.kruskal(n, edges[:i] + edges[i + 1:]) > self.min_cost:
                ans[0].append(indices[i])  # 添加indices[i]就是排序前的边编号
            elif self.kruskal(n, edges[:i] + edges[i + 1:], edges[i]) == self.min_cost:
                ans[1].append(indices[i])
        return ans


'''
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:


        # BFS  可惜是错的
        adj = collections.defaultdict(list)
        for idx, edge in enumerate(edges):
            i, j, w = edge
            adj[i].append((j, w, idx))
            adj[j].append((i, w, idx))
        queue = [(edges[0][0], 0, [], [edges[0][0]])]  # start_node, weights_sum, edges_index, nodes_set
        # nodes = set()
        track = []
        self.weights = float("inf")
        while queue:
            cur_node, cur_w, cur_edge, cur_node_list = queue.pop(0)
            print(cur_node, cur_w, cur_edge, cur_node_list)
            if len(cur_node_list) == n:
                if self.weights > cur_w:
                    track = []
                self.weights = min(cur_w, self.weights)
                if self.weights == cur_w:
                    track.append(cur_edge)
                continue
            for nei, w, e in adj[cur_node]:
                if nei not in cur_node_list:
                    queue.append((nei, cur_w + w, cur_edge + [e], cur_node_list + [nei]))
        print(track)
'''
class UnionFind:
    def __init__(self, n):
        self.count = n  # 并查集数量
        self.parent = [i for i in range(n)]  # 父节点 会在Find时（优化操作：）路径压缩
        self.size = [1 for _ in range(n)]  # 树高 用于Union时（优化操作：）按秩合并

    def Union(self, p, q):  # 都一样p加到q
        rootP = self.Find(p)
        rootQ = self.Find(q)
        if rootP == rootQ:
            return
        else:
            # 按秩合并  就是size记录了rootP和rootQ的树高，我们希望吧树低一些的树接到树高一些的树上
            if self.size[rootP] > self.size[rootQ]:
                self.parent[rootQ] = rootP
            elif self.size[rootP] <= self.size[rootQ]:  # 都一样p加到q
                self.parent[rootP] = rootQ
            self.count -= 1

    def Find(self, p):
        dummy = p
        # 找到最远父节点
        while self.parent[p] != p:
            p = self.parent[p]
        # 路径压缩  把所有路径上的节点的父节点均指向最远父节点 这样就是两层N叉树了
        while self.parent[dummy] != p:
            tmp = self.parent[dummy]
            self.parent[dummy] = p
            dummy = tmp
        return p

    def Connected(self, p, q):
        return self.Find(p) == self.Find(q)

    def Count(self):
        return self.count
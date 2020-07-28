'''
给出方程式 A / B = k, 其中 A 和 B 均为用字符串表示的变量， k 是一个浮点型数字。根据已知方程式求解问题，并返回计算结果。如果结果不存在，则返回 -1.0。

示例 :
给定 a / b = 2.0, b / c = 3.0
问题: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
返回 [6.0, 0.5, -1.0, 1.0, -1.0 ]

输入为: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries(方程式，方程式结果，问题方程式)， 其中 equations.size() == values.size()，即方程式的长度与方程式结果长度相等（程式与结果一一对应），并且结果值均为正数。以上为方程式的描述。 返回vector<double>类型。

基于上述例子，输入如下：

equations(方程式) = [ ["a", "b"], ["b", "c"] ],
values(方程式结果) = [2.0, 3.0],
queries(问题方程式) = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
输入总是有效的。你可以假设除法运算中不会出现除数为0的情况，且不存在任何矛盾的结果。
'''


class Solution:
    def calcEquation(self, equations, values, queries):
        # BFS DFS 源自评论区的powcai
        """
        union find
        https://leetcode.com/problems/evaluate-division/discuss/720327/Easy-to-read-Union-Find-solution
        """
        # initiate union-find data structure
        # e.g. a / b = k
        # root[a] = b; vals[a] = k
        root = {}  # a / b = k  ->  root[a] = b
        vals = {}  # vals[x] = x / root_x

        # find the root and corresponding value for a given variable x
        # so that x / root_x = value
        def find(x):
            if root[x] != x:
                root[x], v = find(root[x])
                vals[x] *= v  # x / root_x = (x / root_a) * (root_a / root_b) * ... * (root_z / root_x)
            return root[x], vals[x]

        # union two variables based on a pair of equation and value, update the value simultaneously
        def union(a, b, v):
            if a not in root:
                root[a] = a
                vals[a] = 1
            if b not in root:
                root[b] = b
                vals[b] = 1
            root_a, v_a = find(a)
            root_b, v_b = find(b)
            """ some math here
            a / b = v
            a / root_a = v_a
            b / root_b = v_b
            => root_a / root_b = a * v_b / b / v_a
            """
            root[root_a] = root_b
            vals[root_a] = v * v_b / v_a

        # calclulate a / b
        def calculate(a, b):
            if a not in root or b not in root:
                return -1.0
            root_a, v_a = find(a)
            root_b, v_b = find(b)
            if root_a != root_b:
                return -1.0
            return v_a / v_b

        # main body
        for (a, b), v in zip(equations, values):
            union(a, b, v)

        return [calculate(a, b) for a, b in queries]


        # DFS
        from collections import defaultdict
        graph = defaultdict(set)
        weight = defaultdict()
        lookup = {}
        # 建图
        for idx, equ in enumerate(equations):
            graph[equ[0]].add(equ[1])
            graph[equ[1]].add(equ[0])
            weight[(equ[0], equ[1])] = values[idx]
            weight[(equ[1], equ[0])] = float(1 / values[idx])

        # 深度遍历(DFS)
        def dfs(start, end, vistied):
            # 当图中有此边,直接输出
            if (start, end) in weight:
                return weight[(start, end)]
            # 图中没有这个点
            if start not in graph or end not in graph:
                return 0
            # 已经访问过
            if start in vistied:
                return 0
            vistied.add(start)
            res = 0
            for nei in graph[start]:
                res = (dfs(nei, end, vistied) * weight[(start, nei)])
                # 只要遍历到有一个不是0的解就跳出
                if res != 0:
                    # 添加此边,以后访问节省时间
                    weight[(start, end)] = res
                    break
            vistied.remove(start)
            return res

        res = []
        for que in queries:
            # 用集合记录是否已经访问节点
            tmp = dfs(que[0], que[1], set())
            if tmp == 0:
                tmp = -1.0
            res.append(tmp)
        return res


        # BFS
        from collections import defaultdict
        graph = defaultdict(set)
        weight = defaultdict()
        # 建图
        for idx, equ in enumerate(equations):
            graph[equ[0]].add(equ[1])
            graph[equ[1]].add(equ[0])
            weight[(equ[0], equ[1])] = values[idx]
            weight[(equ[1], equ[0])] = float(1 / values[idx])
        res = []
        for start, end in queries:
            if (start, end) in weight:
                res.append(weight[(start, end)])
                continue
            if start not in graph or end not in graph:
                res.append(-1.0)
                continue
            if start == end:
                res.append(1.0)
                continue
            stack = []
            # 将从start点可以到达下一个节点压入栈内
            for nei in graph[start]:
                stack.append((nei, weight[(start, nei)]))
            # 记录访问节点
            visited = {start}
            # 为了跳出双循环
            flag = False
            while stack:
                c, w = stack.pop(0)
                if c == end:
                    flag = True
                    res.append(w)
                    break
                visited.add(c)
                for n in graph[c]:
                    if n not in visited:
                        weight[(start, n)] = w * weight[(c, n)]
                        stack.append((n, w * weight[(c, n)]))
            if not flag:
                res.append(-1.0)
        return res






'''
# 并查集  自己写的 还不会写
class UF:
    def __init__(self, n):
        self.count = n
        self.parents = [i for i in range(n)]
        self.sizes = [1 for i in range(n)]
        self.parent_div_cur = [1 for i in range(n)]

    def union(self, p, q, p_div_q):
        rootp = self.find(p)
        rootq = self.find(q)
        if rootp == rootq:
            self.hashmap[p][q] = val
            return
        self.parents[rootq] = rootp
        self.hashmap[rootp][rootq] = val
        # if self.sizes[rootp] >= self.sizes[rootq]:  # 按秩合并
        #     self.parents[rootq] = rootp
        # else:
        #     self.parents[rootp] = rootq
        self.count -= 1

    def find(self, p):
        dummy = p
        while p != self.parents[p]:
            p = self.parents[p]

        while dummy != p:  # 路径压缩
            t = self.parents[dummy]
            self.parents[dummy] = p
            dummy = t
        return p

    def connected(self, p, q):
        return self.find(p) == self.find(q)

class Solution:     
    def calcEquation(self, equations, values, queries):
        # 并查集 没写完 不太会赋权重
        hashset = set()
        for i in range(len(equations)):
            a, b = equations[i]
            hashset.add(a)
            hashset.add(b)
        n = len(hashset)
        uf = UF(n)

        hashmap = collections.defaultdict(dict)
        for i in range(len(equations)):
            a, b = equations[i]
            hashmap[a][b] = values[i]
            hashmap[b][a] = 1 / values[i]

        for i in range(len(equations)):
            a, b = equations[i]
            uf.union(a, b)
'''
'''
给你一棵树（即，一个连通的无环无向图），这棵树由编号从 0  到 n - 1 的 n 个节点组成，且恰好有 n - 1 条 edges 。树的根节点为节点 0 ，树上的每一个节点都有一个标签，也就是字符串 labels 中的一个小写字符（编号为 i 的 节点的标签就是 labels[i] ）

边数组 edges 以 edges[i] = [ai, bi] 的形式给出，该格式表示节点 ai 和 bi 之间存在一条边。

返回一个大小为 n 的数组，其中 ans[i] 表示第 i 个节点的子树中与节点 i 标签相同的节点数。

树 T 中的子树是由 T 中的某个节点及其所有后代节点组成的树。

输入：n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd"
输出：[2,1,1,1,1,1,1]
解释：节点 0 的标签为 'a' ，以 'a' 为根节点的子树中，节点 2 的标签也是 'a' ，因此答案为 2 。注意树中的每个节点都是这棵子树的一部分。
节点 1 的标签为 'b' ，节点 1 的子树包含节点 1、4 和 5，但是节点 4、5 的标签与节点 1 不同，故而答案为 1（即，该节点本身）。
'''
import collections
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        # 树形无向图的遍历
        adj = collections.defaultdict(list)
        # 邻接矩阵  要双向的 不然edges=02 03 12 这样的样例不过了
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        # print("adj:", adj)

        self.ans = [0 for _ in range(n)]

        # 后序遍历
        def rec(root, dic):
            # print(root)
            if root not in adj:
                # print("root:", root)
                dic[labels[root]] = 1
                self.ans[root] = 1
                return dic
            # 后序遍历孩子
            for nei in adj[root]:
                adj[nei].remove(root)   # 无向边 去重
                d = rec(nei, {})
                for k, v in d.items():  # 孩子结果添加到父结果
                    dic[k] = dic.get(k, 0) + v
            # 遍历root
            dic[labels[root]] = dic.get(labels[root], 0) + 1
            self.ans[root] = dic[labels[root]]
            return dic

        rec(0, {})
        return self.ans
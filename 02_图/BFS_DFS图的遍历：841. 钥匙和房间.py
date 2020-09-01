'''
有 N 个房间，开始时你位于 0 号房间。每个房间有不同的号码：0，1，2，...，N-1，并且房间里可能有一些钥匙能使你进入下一个房间。

在形式上，对于每个房间 i 都有一个钥匙列表 rooms[i]，每个钥匙 rooms[i][j] 由 [0,1，...，N-1] 中的一个整数表示，其中 N = rooms.length。 钥匙 rooms[i][j] = v 可以打开编号为 v 的房间。

最初，除 0 号房间外的其余所有房间都被锁住。

你可以自由地在房间之间来回走动。

如果能进入每个房间返回 true，否则返回 false。

示例 1：

输入: [[1],[2],[3],[]]
输出: true
解释:
我们从 0 号房间开始，拿到钥匙 1。
之后我们去 1 号房间，拿到钥匙 2。
然后我们去 2 号房间，拿到钥匙 3。
最后我们去了 3 号房间。
由于我们能够进入每个房间，我们返回 true。
示例 2：

输入：[[1,3],[3,0,1],[2],[0]]
输出：false
解释：我们不能进入 2 号房间。
'''
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # 图的遍历 可以参考 https://leetcode-cn.com/problems/keys-and-rooms/solution/python3-shen-du-you-xian-sou-suo-yan-du-you-xian-s/
        # 以下BFS DFS均为自己写的 20200831
        n = len(rooms)
        graph = collections.defaultdict(list)
        for i, r in enumerate(rooms):
            graph[i] += r

        # BFS
        queue = [0]
        seen = set([0])
        while queue:
            cur = queue.pop(0)
            if len(seen) == n: return True
            if cur not in graph: continue
            # print(cur, step)
            for nei in graph[cur]:
                if nei not in seen:
                    seen.add(nei)
                    queue.append(nei)
        return False

        # DFS
        seen = {0:1}
        def dfs(cur):
            if len(seen) == n: return True
            if not graph[cur]: return False
            res = False
            for nei in graph[cur]:
                if nei not in seen:
                    seen[nei] = 1
                    res = res or dfs(nei)
            return res
        return dfs(0)
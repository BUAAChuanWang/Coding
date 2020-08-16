import numpy as np

class Graph(object):

    def __init__(self, G):
        self.color = [0] * len(G)
        self.G = np.array(G)
        self.isDAG = True
        self.circlecount = 0

    # 对于graph进行预处理，删除孤立点
    def graph_preprocessing(self):
        index = []
        for i in range(len(self.G)):
            if np.sum(self.G[:, i]) == 0 and np.sum(self.G[i, :]) == 0:
                index.append(i)
        # delete columns
        self.G = np.delete(self.G, index, axis=1)
        # delte rows
        self.G = np.delete(self.G, index, axis=0)
        self.color = [0] * len(self.G)

    def DFS(self, i):
        self.color[i] = 1
        for j in range(len(self.G)):
            if self.G[i][j] != 0:
                # print(str(i) + 'can go to '+ str(j))
                if self.color[j] == 1:
                    self.circlecount = self.circlecount + 1
                    self.isDAG = False
                elif self.color[j] == -1:
                    continue
                else:
                    # print('We are visiting node' + str(j))
                    self.DFS(j)
        self.color[i] = -1
        # print(str(i) + " has been examined")

    def DAG(self):
        for i in range(len(self.G)):
            if self.color[i] == 0:
                # print(i)
                self.DFS(i)
    def count(self):
        print(self.circlecount)

while 1:
    N = int(input())
    nums = []
    dic = {}
    id = 0
    for i in range(N):
        t = list(input().split(" "))
        nums.append(t)
        if t[0] not in dic:
            dic[t[0]] = id
            id += 1
        if t[1] not in dic:
            dic[t[1]] = id
            id += 1
    n = len(dic)
    G = [[0 for n in range(n)]for _ in range(n)]
    for i in range(len(nums)):
        a, b = nums[i]
        G[dic[a]][dic[b]] = 1
    # print(G)
    G1 = Graph(G)
    G1.DAG()
    G1.count()
'''
5
a b
b c
c a
a d
d d
'''

# G = [[0,0,1,0,0,0,0],
#      [0,0,1,0,0,0,0],
#      [0,0,0,1,0,0,0],
#      [0,0,0,0,1,1,0],
#      [1,0,0,0,0,0,0],
#      [0,0,0,0,0,0,1],
#      [0,1,0,1,0,0,0]]
# G1 = Graph(G)
# G1.DAG()
# G1.count()
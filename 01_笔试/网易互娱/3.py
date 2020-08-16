'''
input:
1
8
1 1 0
5 2 0
10 3 0
20 3 1
25 4 0
40 4 1
1000 2 1
2000 1 1
output:
1

input:
1
6
0 1 0
5 2 0
6 2 1
6 3 0
11 3 1
11 1 1
output:
1
'''

import sys

if __name__ == "__main__":
# while 1:
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        N = int(sys.stdin.readline().strip())
        nums = []
        res = []
        for i in range(N):
            nums.append(list(map(lambda x:int(x), sys.stdin.readline().strip().split())))
        stack, stack2 = [], []
        pre_id = [nums[0][1]]
        pre_time = [nums[0][0]]
        hashmap = {}
        for i in range(1, N):
            time, id, state = nums[i]
            hashmap[pre_id[-1]] = hashmap.get(pre_id[-1], 0) + time - pre_time[-1]
            if id != pre_id[-1]:
                pre_id.append(id)
                pre_time.append(time)
            elif id == pre_id[-1]:
                pre_id.pop()
                pre_time.pop()
                if pre_time:
                    pre_time[-1] = time
            # print(pre_id, pre_time)
            # print(hashmap)
        res = sorted(hashmap.items(), key=lambda x: (x[1], -x[0]), reverse=True)
        # print(hashmap)
        print(res[0][0])


'''
class EventNode():

    def __init__(self):

        # 建图时计算
        # 开始时记录
        self.id = None
        self.start = None
        # 结束时记录
        self.end = None
        # 遇见父节点记录
        self.parent = None
        self.childs = []

        # 建图完毕
        # dfs记录
        self.time = None


def f(records):

    # print(records)
    roots = []
    stack = []
    nodes = []

    for v in records:

        time, ind, label = v

        if label == 0:
            # 遇见了新的事件，创建
            tmp = EventNode()
            tmp.start = time
            tmp.id = ind

            if not stack:
                # 没有父事件
                roots.append(tmp)
            else:
                # 有父亲事件
                parent = stack[-1][1]
                parent.childs.append(tmp)
                tmp.parent = parent
            stack.append((v, tmp))
        else:
            # 事件的结束，栈顶肯定是同一个事件的开始
            tmp_v, tmp = stack.pop()
            if tmp_v[1] != ind:
                raise BaseException("Err!!!!!!!!!!!!!" + str(records))
            tmp.end = time
    #  建图完毕

    def dfs(root):

        time = root.end - root.start
        for child in root.childs:
            dfs(child)
            time -= child.end - child.start
        nodes.append((time, root.id))

    for root in roots:
        dfs(root)

    nodes = sorted(nodes, key=lambda x: (x[0], -x[1]))
    return nodes[-1][1]


if __name__ == "__main__":

    N = int(input())
    for _ in range(N):
        n = int(input())
        records = []
        for _ in range(n):
            tmp = input().strip().split()
            tmp = [int(c) for c in tmp]
            records.append(tmp)
        print(f(records))
'''
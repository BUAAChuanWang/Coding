class Tree():
    def __init__(self, v):
        self.son = []
        self.v = v
if __name__ == "__main__":
    n = int(input())
    val = []
    for i in range(n):
        val.append(list(map(lambda x:int(x), input().split())))
    students = [Tree(0) for _ in range(n)]
    s = None
    for i, (v, _from) in val:
        students.v = v
        students[_from].append(students[i])
        if _from == 0:
            s = students[i]

    def help(root):
        if not root.son: return max(root.v, 0)
        return max(root.v + sum([help(t) for t in root.son]), 0)
    res = help(s)
    if res > 0:
        print(res)
    else:
        print(s.v)


import sys

class Tree():

    def __init__(self, v):

        self.son = []
        self.v = v

def f(n, lst):

    students = [Tree(0) for _ in range(n)]
    s = None
    for i, (v, parent) in enumerate(lst):
        students[i].v = v
        students[parent].son.append(students[i])
        if parent == 0:
            s = students[i]

    def help(root):

        if not root.son: return max(root.v, 0)
        return max(root.v + sum([help(t) for t in root.son]), 0)

    res = help(s)
    return res if res > 0 else s.v

# n = 3
# val = [[2, 0], [1, 2], [-1, 2]]
# res = f(n, val)
# print(res)

n = int(sys.stdin.readline().strip())
val = []
for i in range(n):
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    val.append(values)
f(n, val)
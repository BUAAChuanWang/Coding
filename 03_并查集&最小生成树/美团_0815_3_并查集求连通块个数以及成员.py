'''
7 5  # 共7个订单  5对订单关系
1 10  # 1号和10号订单属于同一个小区
2 9
1 2
3 2
4 5
output：
2  # 共两个小区
1 2 3 9 10  # 按订单大小顺序分别输出每个小区的订单
4 5
'''
# 并查集 AC
import collections
while 1:
    N, M = input().split(" ")  # N个订单 M对关系
    N, M = int(N), int(M)
    nums = []
    for i in range(M):
        nums.append(list(map(lambda x: int(x), list(input().split(" ")))))

    # 构建简版并查集  不用按秩合并和路径压缩
    n = N
    item = set()
    for num in nums:
        item.add(num[0])
        item.add(num[1])
    parent = {i: i for i in item}
    def Union(p, q):
        rootp = Find(p)
        rootq = Find(q)
        parent[rootp] = rootq
    def Find(p):
        while parent[p] != p:
            p = parent[p]
        return p
    for i in nums:
        Union(i[0], i[1])
    # 构建简版并查集结束
    # 遍历并查集
    res = collections.defaultdict(set)  # 将连通块添加到字典中 {root:set(各联通节点)}
    for i in item:
        res[Find(i)].add(i)
    res = [sorted(res[k]) for k in res]
    res = sorted(res)
    print(len(res), res)
    for i in res:
        print(" ".join(list(map(str, i))))
    break


    # 按秩合并与路径压缩并查集构建  实际应用可以不用写class  直接写方法 这样比较快
    n = N
    item = set()
    for num in nums:
        item.add(num[0])
        item.add(num[1])
    parent = {i : i for i in item}  # parent 构建成字典的方式  可以适用于不是顺序的下标 比如 n=3  但是数字是2 4 8
    size = {i : 1 for i in item}  # 如果超时可以用按秩合并写这个 如果不超时可以写简版
    def Union(p, q):  # 都一样p加到q  按秩合并Union
        rootP = Find(p)
        rootQ = Find(q)
        if rootP == rootQ: return
        else:
            # 按秩合并  就是size记录了rootP和rootQ的树高，我们希望吧树低一些的树接到树高一些的树上
            if size[rootP] > size[rootQ]:
                parent[rootQ] = rootP
            elif size[rootP] <= size[rootQ]:  # 都一样p加到q
                parent[rootP] = rootQ
    def Find(p):  # 路径压缩 如果超时可以用这个 不超时可以写简版
        dummy = p
        # 找到最远父节点
        while parent[p] != p:
            p = parent[p]
        # 路径压缩  把所有路径上的节点的父节点均指向最远父节点 这样就是两层N叉树了
        while parent[dummy] != p:
            tmp = parent[dummy]
            parent[dummy] = p
            dummy = tmp
        return p
    for i in nums:
        Union(i[0], i[1])
    # 构建并查集结束
    # 遍历并查集
    res = collections.defaultdict(set)  # 将连通块添加到字典中 {root:set(各联通节点)}
    for i in item:
        res[Find(i)].add(i)
    res = [sorted(res[k]) for k in res]
    res = sorted(res)
    print(len(res), res)
    for i in res:
        print(" ".join(list(map(str, i))))
    break


# 暴力 AC73
while 1:
    N, M = input().split(" ")
    N, M = int(N), int(M)

    nums = []
    for i in range(M):
        # t = list(input().split(" "))
        t = list(map(lambda x: int(x), list(input().split(" "))))
        tmp = (t[0], t[1]) if t[0] < t[1] else (t[1], t[0])
        nums.append(tmp)
    # nums = sorted(nums, key=lambda x: x[0])
    # print(nums)

    item = []
    for i in range(M):
        a, b = nums[i]
        one, two = None, None
        for j in range(len(item)):
            if a in item[j]:
                one = j
            if b in item[j]:
                two = j
        # print("a b one two:", a, b, one, two)
        if one != None and two != None:
            if one == two: continue
            else:
                item[one] |= item[two]
                item.pop(two)
        elif one != None:
            item[one].add(b)
        elif two != None:
            item[two].add(a)
        elif one == None and two == None:
            item.append(set([a, b]))
        # print("item:", item)
    # print(item)

    res = []
    for ite in item:
        t = sorted(list(ite))
        res.append(t)
    # print(res)
    res = sorted(res)
    print(len(res))
    for i in range(len(res)):
        print(" ".join(list(map(lambda x: str(x), res[i]))))
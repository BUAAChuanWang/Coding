'''
Input

集合S = {a + b | a属于A, b属于B}
A={1,1,4}
B={1,3}
返回S中前k个最小的元素

Sample Output

2,4,5

Source

S = {2,4,5,7}
前3个最小的就是{2,4,5}

'''
# mnlogk
while 1:
    k = int(input())
    A = input()
    B = input()
    A = list(map(lambda x: int(x), A.split(" ")))
    B = list(map(lambda x: int(x), B.split(" ")))
    m, n = len(A), len(B)

    res = set()
    stack = []
    import heapq
    for i in range(m):
        for j in range(n):
            if len(stack) == k:
                break
            while i < m - 1 and A[i] == A[i + 1]:
                i += 1
            while j < n - 1 and B[j] == B[j + 1]:
                j += 1
            summ = A[i] + B[j]
            if (summ) not in res:
                heapq.heappush(stack, summ)
                res.add(summ)
    res = []
    while stack:
        res.append(heapq.heappop(stack))
    print(res)


'''
# klogm
# https://blog.csdn.net/yl1415/article/details/44874487
# 该思路是m个有序数列的合并 只是有些边界问题不好处理 而且python中heapq的排序对类的支持还不太会。。。
while 1:
    k = int(input())
    A = input()
    B = input()
    A = list(map(lambda x: int(x), A.split(" ")))
    B = list(map(lambda x: int(x), B.split(" ")))
    m, n = len(A), len(B)
    class Node():
        def __int_(self, val, i):
            self.val = val
            self.i = i

    import heapq
    res = set()
    stack = []
    d = [0] * m
    t = Node()
    for i in range(m):
        t.val = A[i] + B[d[i]]
        t.i = i
        heapq.heappush(stack, t)

    while k:
        k -= 1
        t = heapq.heappop(stack)
        while t.val in res:
            d[t.i] += 1
            t.val = A[t.i] + B[d[t.i]]
            t = heapq.heappushpop(stack, t)

        res.add(t.val)
        d[t.i] += 1
        t.val = A[t.i] + B[d[t.i]]
        heapq.heappush(stack, t)
    res = []
    while stack:
        res.append(heapq.heappop(stack))
    print(res)



'''   

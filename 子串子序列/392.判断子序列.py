def isSubsequence(slist, t):
    # 二分 + 哈希
    def get_lbound(lis, target):
        l, r = 0, len(lis)
        while l < r:
            mid = l + (r - l) // 2
            if lis[mid] >= target:
                r = mid
            if lis[mid] < target:
                l = mid + 1
        return l

    import collections
    index = collections.defaultdict(list)
    for i in range(len(t)):
        index[t[i]].append(i)
    res = []
    for s in slist:
        j = 0
        flag = True
        for i in range(len(s)):
            if s[i] not in index:
                res.append(False)
                flag = False
                break
            pos = get_lbound(index[s[i]], j)
            if pos == len(index[s[i]]):
                res.append(False)
                flag = False
                break
            j = index[s[i]][pos] + 1
        if flag:
            res.append(True)
    print(res)


isSubsequence(["abc", "bd", "rf", "ad"], "egalblcldfr")
'''
4
1T 4T 7T 2B 5B 8B 9W
1T 2T 3T 4T 5T 6T 7T
1B 2W 3T 4B 5W 6T 8W
2B 8B 5B 2B 6T 7W 4W

YES
NO
YES
NO
'''
import sys
import collections
if __name__ == "__main__":
# while 1:
    T = int(sys.stdin.readline().strip())
    nums = []
    res = []
    for i in range(T):
        nums = list(sys.stdin.readline().strip().split())
        dic = collections.defaultdict(list)
        for j, num in enumerate(nums):
            a, b = num[0], num[1]
            if b in dic and a in dic[b]:
                res.append("NO")
                break
            dic[b].append(int(a))

        if len(dic) != 3:
            res.append("NO")
            continue

        t = set()
        flag = False
        for k, v in dic.items():
            v.sort()
            pre = v[0]
            t.add(v[0])
            if flag:
                break
            for p in range(1, len(v)):
                t.add(v[p])
                if (v[p] - pre) % 3 != 0:
                    res.append("NO")
                    flag = True
                    break
                pre = v[p]

        if len(t) == 7:
            res.append("YES")
        else:
            res.append("NO")
    for i in range(T):
        print(res[i])

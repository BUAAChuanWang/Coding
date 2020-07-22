# 2
# 3 1
# 2
import collections
while 1:
    n = int(input())
    nums = list(map(int, input().split(" ")))
    hashmap = collections.defaultdict(set)
    def get_subseq(nums):
        res = []
        def backtrack(sub, index):
            res.append(sub)
            for i in range(index, len(nums)):
                backtrack(sub + [nums[i]], i + 1)
        backtrack([], 0)
        return res

    def judge(seq):
        if not seq: return 0
        for i in range(len(seq)):
            if seq[i] in hashmap[i + 1]:
                continue
            else:
                if seq[i] % (i + 1):
                    return 0
                else:
                    hashmap[i + 1].add(seq[i])
            # if seq[i] % (i + 1):
            #     return 0
        return 1

    res = 0
    sub_seq = get_subseq(nums)
    for seq in sub_seq:
        res += judge(seq)
    print(res % 998244353)
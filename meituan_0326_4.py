while 1:
    n, p ,q = list(map(int, input().split(" ")))
    a = list(map(int, input().split(" ")))

    pos, neg = p / q, 1 - p / q

    def get_seq(a):
        res = []
        def backtrack(track):
            if len(track) == len(a):
                res.append(track[:])
                return
            for num in [0, 1]:
                backtrack(track + [num])
        backtrack([])
        return res

    def mean(seq):
        prob = 1
        score = 0
        cnt = 0
        for state in seq:
            if state == 1:
                score += a[cnt]
                cnt += 1
            else:
                cnt = 0

            prob *= pos if state == 1 else neg
        return prob * score

    seqs = get_seq(a)
    res = 0
    for seq in seqs:
        res += mean(seq)
    print(res % 998244353)
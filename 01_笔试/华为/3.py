'''
俄罗斯方块
input:
2202
2
output:
0

input:
2122
121
output:
1
'''
import sys
if __name__ == "__main__":
    frame = list(map(int, sys.stdin.readline().strip()))
    brick = list(map(int, sys.stdin.readline().strip()))
    # print(frame, brick)

    def helper(frame, brick):
        frame_n, brick_n = len(frame), len(brick)
        res = float("inf")
        for i in range(frame_n - brick_n + 1):
            max_h = 0
            for j in range(brick_n):
                max_h = max(max_h, brick[j] + frame[i + j])
            total_max_h = max_h
            r = float("inf")
            for j in range(frame_n):
                total_max_h = max(total_max_h, frame[j])
                # 两边最矮的高度
                if j < i:
                    r = min(r, frame[j])
                elif j >= (i + brick_n):
                    r = min(r, frame[j])
                # 中间添加brick的部分的最矮高度
                else:
                    tmp1 = frame[j]
                    tmp2 = brick[j - i]
                    if tmp1 + tmp2 == max_h:
                        r = min(r, max_h)
                    else:
                        r = min(r, tmp1)
            # 结果是每一次的： 最高 - 最低
            res = min(res, total_max_h - r)
        return res
    print(helper(frame, brick))

    '''
    fs = [0 for _ in range(4)]
    for i in range(len(frame)):
        fs[i] = frame[i] - 0

    lenb = len(brick)
    bs = [0 for _ in range(lenb)]
    for i in range(lenb):
        bs[i] = brick[i] - 0
    res = [[0 for _ in range(4)]for _ in range(4)]
    for i in range(4):
        for j in range(4):
            res[i][j] = fs[j]
    print(res)
    if lenb == 4:
        for i in range(4):
            res[i][j] = fs[j] + bs[j - i]
            print(res)
    elif lenb == 3:
        for i in range(2):
            for j in range(i, i + 3):
                res[i][j] = fs[j] + bs[j - i]
    elif lenb == 2:
        for i in range(3):
            for j in range(i, i + 2):
                res[i][j] = fs[j] + bs[j - i]
                print(res)
    elif lenb == 1:
        for i in range(4):
            for j in range(i , i + 1):
                res[i][j] = fs[j] + bs[0]
                print(res)
    minres = 10000
    for i in range(4):
        minl1 = 100000
        maxl2 = -1
        for j in range(4):
            if minl1 >= res[i][j]:
                minl1 = res[i][j]
            if maxl2 <= res[i][j]:
                maxl2 = res[i][j]
        if minres >= (maxl2 - minl1):
            minres = maxl2 - minl1
    print(minres)
    '''
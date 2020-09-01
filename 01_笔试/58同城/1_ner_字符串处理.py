'''
time:月,time:日,loc:小区,loc:超市;5月1号在新龙城或浩客见;月 月 日 日 O 小区 小区 小区 O 超市 超市 O
time:5月1号,loc:新龙城,loc:浩客

time:月,time:日,loc:小区,loc:超市;怎5月1号新龙城浩客怎怎区怎月怎;O 月 月 日 日 小区 小区 小区 超市 超市 O O 小区 O 月 O
'''
# AC
import sys
def func(s):
    s = s.strip("\n")
    d, text, ner = s.split(";")
    map = {}
    for tmp in d.split(","):
        k, v = tmp.split(":")
        map[v] = k
    # print(map)
    ner = ner.split(" ")
    res = []
    pre, pre_t = None, None
    for a, b in zip(text, ner):
        # print(a, b)
        if b not in map:
            if pre: res.append(pre + ":" + pre_t)
            pre, pre_t = None, None
            # print("O")
            continue
        if not pre:
            pre = map[b]
            pre_t = a
            continue
        if pre != map[b]:
            res.append(pre + ":" + pre_t)
            pre = map[b]
            pre_t = a
        else:
            pre_t += a
    if pre: res.append(pre + ":" + pre_t)
    return ",".join(res)


if __name__ == "__main__":
    for line in sys.stdin:
        res = func(line)
        if res: print(res)
        else: print("O")

    # s = sys.stdin.readline().strip("\n")
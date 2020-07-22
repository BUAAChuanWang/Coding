'''
做粽子，共有 m种粽子，现在有原料： 共有n克面粉，每种粽子的馅料有ai克，
做每种粽子i分别所需： bi克馅料和ci克面粉，
售出后每种粽子i可以获得di元收益，粽子也可以只有面粉没有馅料，那么会消耗固定值c0克面粉，获得收益固定值d0元
求包粽子的最大价值

输入：
第一行：n,m,c0,d0 即n克面粉，m种粽子，c0克面粉，d0元收益 (c0>=1)
接下来有m行，每行分别是: ai, bi, ci, di
输出：
一个整数表示获得的最大价值

例子：
input：
10 2 1 1
6 3 2 50
8 2 1 10

output：
142   即做2个一粽子，获得100，4个二粽子，获得40，2个全面粉粽子获得2，共142元
'''
# -0-
import sys
import functools

if __name__ == "__main__":
    # 读取第一行的n
    n, m, c0, d0 = list(map(int, sys.stdin.readline().strip().split(" ")))
    # print(n, m, c0, d0)
    a, b, c, d = [], [], [], []
    for i in range(m):
        ai, bi, ci, di = list(map(int, sys.stdin.readline().strip().split(" ")))
        a.append(ai)
        b.append(bi)
        c.append(ci)
        d.append(di)

    origin_xl = a
    origin_mf = n
    cost_xl = b + [0]
    cost_mf = c + [c0]
    gain = d + [d0]

    # @functools.lru_cache
    memo = {}
    def dp(mf, xl):
        if (mf, xl) in memo:
            return memo[(mf, xl)]
        if mf <= 0:
            return 0
        res = [0 for _ in range(m+1)]
        for i in range(m + 1):
            if mf >= cost_mf[i] and xl[i] >= cost_xl[i]:
                new_xl = list(xl)
                new_xl[i] -= cost_xl[i]
                res[i] = dp(mf - cost_mf[i], tuple(new_xl)) + gain[i]
        memo[(mf, xl)] = max(res)
        return max(res)
    
    res = dp(origin_mf, tuple(origin_xl + [0]))
    print(res)




"""
n: mf 数量
a: xl 数量
b: xl 花费
c: mf 花费
d: 钱
"""

import functools


def f():
    # 定义常量
    cost_xl = []
    cost_mf = []
    money_xl = []

    pure_mf_cost = 0
    pure_mf_money = 0

    @functools.lru_cache
    def dp(state):

        mf = state[0]
        xl = state[1:]
        length = len(xl)

        if mf == 0:
            return 0
        else:
            tmp = [0] * length
            for i in range(length):
                xl_rem = state[i+1]
                mf_rem = mf
                if mf_rem > cost_mf[i] and xl_rem > cost_xl[i]:
                    state_copy = state.copy()
                    state_copy[0] -= cost_mf[i]
                    state_copy[i + 1] -= cost_xl[i]
                    tmp[i] = dp(state_copy) + money_xl[i]
            state_copy = state.copy()
            state_copy[0] -= pure_mf_cost
            tmp += [dp(state_copy) + pure_mf_money]
            return max(tmp)

    # 初始化 state
    state = []
    return dp(state)
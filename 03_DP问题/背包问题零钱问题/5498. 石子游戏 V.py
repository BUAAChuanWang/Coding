'''
几块石子 排成一行 ，每块石子都有一个关联值，关联值为整数，由数组 stoneValue 给出。

游戏中的每一轮：Alice 会将这行石子分成两个 非空行（即，左侧行和右侧行）；Bob 负责计算每一行的值，即此行中所有石子的值的总和。Bob 会丢弃值最大的行，Alice 的得分为剩下那行的值（每轮累加）。如果两行的值相等，Bob 让 Alice 决定丢弃哪一行。下一轮从剩下的那一行开始。

只 剩下一块石子 时，游戏结束。Alice 的分数最初为 0 。

返回 Alice 能够获得的最大分数 。

 

示例 1：

输入：stoneValue = [6,2,3,4,5,5]
输出：18
解释：在第一轮中，Alice 将行划分为 [6，2，3]，[4，5，5] 。左行的值是 11 ，右行的值是 14 。Bob 丢弃了右行，Alice 的分数现在是 11 。
在第二轮中，Alice 将行分成 [6]，[2，3] 。这一次 Bob 扔掉了左行，Alice 的分数变成了 16（11 + 5）。
最后一轮 Alice 只能将行分成 [2]，[3] 。Bob 扔掉右行，Alice 的分数现在是 18（16 + 2）。游戏结束，因为这行只剩下一块石头了。
示例 2：

输入：stoneValue = [7,7,7,7,7,7,7]
输出：28
示例 3：

输入：stoneValue = [4]
输出：0
'''


class Solution:
    def stoneGameV(self, A: List[int]) -> int:
        if len(A) == 1: return 0
        # 前缀和减少计算
        summ = [x for x in A]
        for i in range(1, len(A)):
            summ[i] += summ[i - 1]

        @functools.lru_cache(None)
        def dp(s, e):
            # print(s)
            if s == e:
                return 0
            if s > e:
                return 0
            presum = summ[s - 1] if s > 0 else 0
            res = 0
            for i in range(s, e + 1):
                s1, s2 = summ[i] - presum, summ[e] - summ[i]
                # print("s1,s2:",s1,s2)
                if s1 < s2:
                    res = max(res, s1 + dp(s, i))
                elif s1 > s2:
                    res = max(res, s2 + dp(i + 1, e))
                elif s1 == s2:
                    res = max(res, s1 + dp(s, i), s2 + dp(i + 1, e))
            return res

        return dp(0, len(A) - 1)

        # 赛时 AC 8000ms
        def dp(s):
            # print(s)
            if len(s) == 1:
                return 0
            if not s:
                return 0
            res = 0
            for i in range(len(s) - 1):
                t1 = tuple(s[: i + 1])
                t2 = tuple(s[i + 1:])
                s1, s2 = sum(t1), sum(t2)
                # print("s1,s2:",s1,s2)
                if s1 < s2:
                    res = max(res, s1 + dp(t1))
                elif s1 > s2:
                    res = max(res, s2 + dp(t2))
                elif s1 == s2:
                    res = max(res, s1 + dp(t1), s2 + dp(t2))
            return res

        return dp(tuple(A))



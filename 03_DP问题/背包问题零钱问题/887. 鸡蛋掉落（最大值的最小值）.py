'''
你将获得 K 个鸡蛋，并可以使用一栋从 1 到 N  共有 N 层楼的建筑。
每个蛋的功能都是一样的，如果一个蛋碎了，你就不能再把它掉下去。
你知道存在楼层 F ，满足 0 <= F <= N 任何从高于 F 的楼层落下的鸡蛋都会碎，从 F 楼层或比它低的楼层落下的鸡蛋都不会破。
每次移动，你可以取一个鸡蛋（如果你有完整的鸡蛋）并把它从任一楼层 X 扔下（满足 1 <= X <= N）。
你的目标是确切地知道 F 的值是多少。
无论 F 的初始值如何，你确定 F 的值的最小移动次数是多少？

示例 1：

输入：K = 1, N = 2
输出：2
解释：
鸡蛋从 1 楼掉落。如果它碎了，我们肯定知道 F = 0 。
否则，鸡蛋从 2 楼掉落。如果它碎了，我们肯定知道 F = 1 。
如果它没碎，那么我们肯定知道 F = 2 。
因此，在最坏的情况下我们需要移动 2 次以确定 F 是多少。
示例 2：

输入：K = 2, N = 6
输出：3
'''
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        @functools.lru_cache(None)
        def dp(k, n):  # k个鸡蛋 n层楼的 最少次数
            if n == 0: return 0
            if k == 1: return n
            res = float("inf")
            # DP递归
            # for i in range(1, n + 1):
            #     res = min(res, max(dp(k - 1, i - 1), dp(k, n - i)) + 1)

            # 二分 相当于最大值的最小值 最大值是因为要线性测试，所以取最大值。 最小值是最小测试次数
            l, r = 1, n + 1
            while l < r:
                mid = l + (r - l) // 2
                broken = dp(k - 1, mid - 1)
                not_broken = dp(k, n - mid)
                if not_broken >= broken:
                    l = mid + 1
                    res = min(res, 1 + not_broken)
                else:
                    r = mid
                    res = min(res, 1 + broken)
            return res
        return dp(K, N)



        memo = {}
        def dp(k, n):
            if k == 1: return n
            if n == 0: return 0

            if (k, n) in memo:
                return memo[(k, n)]
            '''# 线性
            for i in rage(1, n+1):
                res = min(res, 1 + max(dp(k-1, i-1), dp(k, n-i)))
            '''
            # 二分查找最小值
            l, r = 1, n
            res = float("inf")
            while l <= r:
                mid = l + (r - l) // 2
                broken = dp(k-1, mid-1)
                not_broken = dp(k, n-mid)
                if broken > not_broken:
                    r = mid - 1
                    res = min(res, 1 + broken)
                else:
                    l = mid + 1
                    res = min(res, 1 + not_broken)
            memo[(k, n)] = res
            return res
        return dp(K, N)
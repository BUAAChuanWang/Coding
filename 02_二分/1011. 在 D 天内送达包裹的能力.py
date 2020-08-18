'''
传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。

传送带上的第 i 个包裹的重量为 weights[i]。每一天，我们都会按给出重量的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。

返回能在 D 天内将传送带上的所有包裹送达的船的最低运载能力。

 

示例 1：

输入：weights = [1,2,3,4,5,6,7,8,9,10], D = 5
输出：15
解释：
船舶最低载重 15 就能够在 5 天内送达所有包裹，如下所示：
第 1 天：1, 2, 3, 4, 5
第 2 天：6, 7
第 3 天：8
第 4 天：9
第 5 天：10

请注意，货物必须按照给定的顺序装运，因此使用载重能力为 14 的船舶并将包装分成 (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) 是不允许的。
示例 2：

输入：weights = [3,2,2,4,1,4], D = 3
输出：6
解释：
船舶最低载重 6 就能够在 3 天内送达所有包裹，如下所示：
第 1 天：3, 2
第 2 天：2, 4
第 3 天：1, 4
示例 3：

输入：weights = [1,2,3,1,1], D = 4
输出：3
解释：
第 1 天：1
第 2 天：2
第 3 天：3
第 4 天：1, 1
'''


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        # 和410、875一样
        # 如果载重为 cap，是否能在 D 天内运完货物？
        def could_cap(cap):
            s, day = 0, 0
            for i in weights:  # 遍历weights的每天重量
                if s + i > cap:  # 当前的重量 + 当该天的包裹重量 > 当前最大运载能力cap；当天包裹重量就一起不能运载，会超重
                    day, s = day + 1, i  # 天数+1，s当前重量就变为该天的包裹重量
                else:  # 反之，当前重量+该天包裹重量
                    s += i
            return day + 1

        l, r = max(weights), sum(weights) + 1
        while l < r:
            mid = l + (r - l) // 2
            if could_cap(mid) == D:
                r = mid
            if could_cap(mid) < D:
                r = mid
            if could_cap(mid) > D:
                l = mid + 1
        lbound = l
        return lbound
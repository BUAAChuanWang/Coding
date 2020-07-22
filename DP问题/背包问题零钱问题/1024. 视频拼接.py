'''
你将会获得一系列视频片段，这些片段来自于一项持续时长为 T 秒的体育赛事。这些片段可能有所重叠，也可能长度不一。
视频片段 clips[i] 都用区间进行表示：开始于 clips[i][0] 并于 clips[i][1] 结束。
我们甚至可以对这些片段自由地再剪辑，例如片段 [0, 7] 可以剪切成 [0, 1] + [1, 3] + [3, 7] 三部分。
我们需要将这些片段进行再剪辑，并将剪辑后的内容拼接成覆盖整个运动过程的片段（[0, T]）。返回所需片段的最小数目，如果无法完成该任务，则返回 -1 。

示例 1：
输入：clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], T = 10
输出：3
解释：
我们选中 [0,2], [8,10], [1,9] 这三个片段。
然后，按下面的方案重制比赛片段：
将 [1,9] 再剪辑为 [1,2] + [2,8] + [8,9] 。
现在我们手上有 [0,2] + [2,8] + [8,10]，而这些涵盖了整场比赛 [0, 10]。

示例 2：
输入：clips = [[0,1],[1,2]], T = 5
输出：-1
解释：
我们无法只用 [0,1] 和 [1,2] 覆盖 [0,5] 的整个过程。
'''


class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        # 两种写法
        '''
        # dpi 从0到i所需的最小个数
        dp = [float("inf") for _ in range(T + 1)]
        dp[0] = 0
        for i in range(1, T + 1):
            flag = False
            for j in range(len(clips)):
                a, b = clips[j]
                if a < i and b >= i:
                    dp[i] = min(dp[i], dp[a] + 1)
                    flag = True
            if not flag:
                return -1
        return dp[-1]
        '''
        # 类似阿里笔试第二题  就是填满0 到 T需要的最小个数为  填到每一个clip【0】所需的最小个数 + 1
        self.flag = True
        memo = {}

        def dp(state):
            if not self.flag: return float("inf")
            if state in memo:
                return memo[state]
            if state <= 0:
                return 0
            res = [float("inf") for _ in range(T + 1)]
            for i in range(len(clips)):
                a, b = clips[i]
                if b >= state and a < state:
                    res[a] = dp(a) + 1
            if min(res) == float("inf"): self.flag = False
            memo[state] = min(res)
            return memo[state]

        res = dp(T)
        if not self.flag: return -1
        return res

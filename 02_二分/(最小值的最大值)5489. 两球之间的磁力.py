'''
在代号为 C-137 的地球上，Rick 发现如果他将两个球放在他新发明的篮子里，它们之间会形成特殊形式的磁力。Rick 有 n 个空的篮子，第 i 个篮子的位置在 position[i] ，Morty 想把 m 个球放到这些篮子里，使得任意两球间 最小磁力 最大。

已知两个球如果分别位于 x 和 y ，那么它们之间的磁力为 |x - y| 。

给你一个整数数组 position 和一个整数 m ，请你返回最大化的最小磁力。

示例 1：
输入：position = [1,2,3,4,7], m = 3
输出：3
解释：将 3 个球分别放入位于 1，4 和 7 的三个篮子，两球间的磁力分别为 [3, 3, 6]。最小磁力为 3 。我们没办法让最小磁力大于 3 。
示例 2：

输入：position = [5,4,3,2,1,1000000000], m = 2
输出：999999999
解释：我们使用位于 1 和 1000000000 的篮子时最小磁力最大。
'''


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def check(x):
            """检查按照当前值分区的个数是否满足题目要求"""
            cnt = 1
            t = position[0]
            for i in range(1, len(position)):
                if position[i] - t >= x:
                    cnt += 1
                    t = position[i]
            return cnt >= m

        # 二分套路 [l, r)
        l, r = 0, (position[-1] - position[0]) // (m - 1) + 1
        while l < r:
            mid = l + (r - l) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid
        return l - 1

        # https://leetcode-cn.com/problems/magnetic-force-between-two-balls/solution/jing-dian-er-fen-cha-zhao-python3-by-dz-lee/
        # 排序，确定上下边界
        position.sort()
        l = min([(position[i + 1] - position[i]) for i in range(len(position) - 1)])
        r = position[-1] - position[0]

        def check(diff):
            """检查按照当前值分区的个数是否满足题目要求"""
            count = 0
            i, j = 0, 0
            while j < len(position):
                while j < len(position) and position[j] - position[i] < diff:
                    j += 1
                if j < len(position):
                    count += 1
                i = j
            return count + 1 >= m

        while l <= r:
            mid = l + (r - l) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return l - 1
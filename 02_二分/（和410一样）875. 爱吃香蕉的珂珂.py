'''
珂珂喜欢吃香蕉。这里有 N 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 H 小时后回来。

珂珂可以决定她吃香蕉的速度 K （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 K 根。如果这堆香蕉少于 K 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。  

珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。

返回她可以在 H 小时内吃掉所有香蕉的最小速度 K（K 为整数）。

 

示例 1：

输入: piles = [3,6,7,11], H = 8
输出: 4
示例 2：

输入: piles = [30,11,23,4,20], H = 5
输出: 30
示例 3：

输入: piles = [30,11,23,4,20], H = 6
输出: 23
'''
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        # 20200727
        # 二分 和410题基本一模一样 二分套路：https://labuladong.gitbook.io/algo/gao-pin-mian-shi-xi-lie/koko-tou-xiang-jiao
        l, r = 1, max(piles) + 1    # 最少一次吃一根 最多一次吃做多的一把香蕉
        while l < r:
            mid = l + (r - l) // 2  # 吃香蕉的速度
            # 模拟吃香蕉
            count = 0
            for i in range(len(piles)):
                count += math.ceil(piles[i] / mid)
            # 二分
            if count <= H:
                r = mid
            elif count > H:
                l = mid + 1
        return l

        # 二分套路 https://labuladong.gitbook.io/algo/gao-pin-mian-shi-xi-lie/koko-tou-xiang-jiao
        def could_eat(speed):
            time = 0
            for p in piles:
                time += math.ceil(p / speed)
            return time

        l, r = 1, max(piles) + 1
        while l < r:
            mid = l + (r - l) // 2
            if could_eat(mid) == H:
                r = mid
            if could_eat(mid) < H:
                r = mid
            if could_eat(mid) > H:
                l = mid + 1
        lbound = l
        return lbound
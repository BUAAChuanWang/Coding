'''
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
'''


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        intervals = sorted(intervals, key=lambda x: x[0])  # 按start排序
        res = []
        start, end = intervals[0]  # 一次遍历排序后的区间集合即可
        for i in range(1, len(intervals)):
            cur_s, cur_e = intervals[i]
            if cur_s <= end:  # 若当前cur_s <= end 表明这个区间可以合并到上一个区间
                end = max(end, cur_e)
            else:  # 否则添加上一个区间到res，更新s，e
                res.append([start, end])
                start, end = cur_s, cur_e
        res.append([start, end])
        return res
        
        '''
        res = []
        intervals.sort()
        for i in intervals:
            if not res or res[-1][1] < i[0]:
                res.append(i)
            else:
                res[-1][1] = max(i[1],res[-1][1])
        return res
        '''
'''
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。

 

示例:

输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]
'''


class Solution:
    def restoreIpAddresses(self, nums: str) -> List[str]:
        # https://leetcode-cn.com/problems/restore-ip-addresses/solution/bao-li-he-hui-su-by-powcai/
        res = []
        s = nums
        n = len(s)

        def backtrack(i, tmp, flag):
            if i == n and flag == 0:
                res.append(tmp[:-1])
                return
            if flag <= 0:
                return
            for j in range(i, i + 3):
                if j < n:
                    if i == j and s[j] == "0":
                        backtrack(j + 1, tmp + s[j] + ".", flag - 1)
                        break
                    if 0 < int(s[i:j + 1]) <= 255:
                        backtrack(j + 1, tmp + s[i:j + 1] + ".", flag - 1)

        backtrack(0, "", 4)
        return res

        # 回溯  自己写的   start是要添加的下一个子串的起始位置  num是还有多少个点可以放
        self.res = []

        def backtrack(track, start, num):
            if num == 0:
                if start < len(nums) - 1 and nums[start] == "0": return  # 特判 x.x.x.0xx
                if start < len(nums) and 0 <= int(nums[start:]) <= 255:
                    track += [nums[start:]]
                    self.res.append(".".join(track))
                return

            if start < len(nums) and nums[start] != "0":
                for i in range(1, 4):
                    if start + i <= len(nums) and 0 <= int(nums[start: start + i]) <= 255:
                        backtrack(track + [nums[start: start + i]], start + i, num - 1)
            elif start < len(nums) and nums[start] == "0":  # 特判 xx.0.xx.xx 0开头的只能直接加进去
                backtrack(track + [nums[start: start + 1]], start + 1, num - 1)

        backtrack([], 0, 3)
        return self.res

        '''
        def valid(segment):
            return int(segment) <= 255 if segment[0] != '0' else len(segment) == 1
        # 处理第三个点后面的 也就是最后一部分，如果valid就添加到output    
        def update_output(curr_pos):
            segment = s[curr_pos + 1:n]
            if valid(segment):
                segments.append(segment)
                output.append('.'.join(segments))
                segments.pop()    
        # 在下标为i的数字的后面放dot。 回溯是通过segments.pop()来进行的
        def backtrack(prev_pos = -1, dots = 3):
            for curr_pos in range(prev_pos + 1, min(n - 1, prev_pos + 4)):#至少要留最后一个数字作为第四部分，所以min(n-1)
                segment = s[prev_pos + 1:curr_pos + 1]
                if valid(segment):
                    segments.append(segment)  # 把这部分加进到segments里面，出里面这个curpos后会pop掉来进行回溯
                    if dots - 1 == 0:  # 如果所有的3个点都被放好了
                        update_output(curr_pos)  # 更新结果
                    else:
                        backtrack(curr_pos, dots - 1)  # 继续放下一个点
                    segments.pop()  # 移除上一个放置的点    
        n = len(s)
        output, segments = [], []
        backtrack() 
        return output
        '''
'''
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

示例 1：

输入："abc"
输出：3
解释：三个回文子串: "a", "b", "c"
示例 2：

输入："aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
'''


class Solution:
    def countSubstrings(self, s: str) -> int:
        # 20200822
        # dp[i][j]表示从i到j的子串是否为回文字符串
        if not s: return 0
        n = len(s)
        res = 0
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                    res += 1
                    continue
                if s[i] != s[j]:
                    continue
                elif s[i] == s[j]:
                    if j == i + 1:
                        dp[i][j] = 1
                        res += 1
                    elif j >= i + 2 and i < n - 1 and dp[i + 1][j - 1]:
                        dp[i][j] = 1
                        res += 1
        return res


        # 201910
        if not s: return 0
        res = len(s)
        # dp[i]表示与index=i能形成回文的index
        # 当前字符根据前一字符形成回文子串的结果上进行推导，比如 i-1 处可以和以 2，4，5 为开始形成的子串为回文串，
        # 那么比较当前字符是否与 1，3，4 处的字符相等，若相等则可以形成回文
        # 初始化 dp 数组的时候要注意，当前字符本身就是一个回文，所以初始化的时候就要加入；加入 i+1 的原因是，上面的情况遗漏了 i 和 i-1 形成回文的情况

        dp = [[i, i + 1] for i in range(len(s))]
        for i in range(1, len(s)):
            for j in dp[i - 1]:
                if j - 1 >= 0 and s[j - 1] == s[i]:
                    res += 1
                    dp[i].append(j - 1)
        return res
#         """
#            就是统计一共有多少个回文串, 那就是发现一个加1就可以了

#            还是令dp[i][j]表示从i到j的序列是否为回文串，如果是就为True, 如果不是就是False

#            如果s[i] == s[j]并且dp[i+1][j-1]==True, 那么 dp[i][j]就为True
#         """
#         size = len(s)
#         if size == 0:
#             return 0
#         if size == 1:
#             return 1

#         dp = [[False for _ in range(size)] for _ in range(size)]
#         for i in range(size):
#             dp[i][i] = True
#         count = size

#         for len_t in range(1, size):
#             for start in range(size - len_t):
#                 end = start + len_t
#                 if s[start] == s[end] and (len_t <= 2 or dp[start+1][end-1]):
#                     dp[start][end] = True
#                     count += 1
#                 else:
#                     dp[start][end] = False

#         return count
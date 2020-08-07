'''
给定一个字符串 s ，找到其中最长的回文子序列，并返回该序列的长度。可以假设 s 的最大长度为 1000 。

 

示例 1:
输入:

"bbbab"
输出:

4
一个可能的最长回文子序列为 "bbbb"。

示例 2:
输入:

"cbbd"
输出:

2
一个可能的最长回文子序列为 "bb"。
'''
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # dp
        if not s:return 0
        dp = [[0 for _ in range(len(s))]for _ in range(len(s))]
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if i == j:
                    dp[i][j] = 1
                    continue

                if s[i] == s[j]:
                    if j - i > 1:
                        dp[i][j] = 2 + dp[i+1][j-1]
                    elif j - i == 1:
                        dp[i][j] = 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][-1]
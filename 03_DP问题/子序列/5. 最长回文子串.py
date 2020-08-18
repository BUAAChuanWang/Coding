''''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp  labuladong   on2 time on2 space
        # https://leetcode-cn.com/problems/longest-palindromic-subsequence/
        # https://leetcode-cn.com/problems/longest-common-subsequence/
        if not s: return ""
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        res = float("-inf")
        ans = None
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if i == j:
                    dp[i][j] = 1
                else:
                    if s[i] == s[j]:
                        if j - i > 1:
                            dp[i][j] = dp[i + 1][j - 1] + 2 if dp[i + 1][j - 1] else 0
                        elif j - i == 1:
                            dp[i][j] = 2
                res = max(res, dp[i][j])
                if res == dp[i][j]:
                    ans = (i, j)
        return s[ans[0]:ans[1] + 1]


        # https://labuladong.gitbook.io/algo/gao-pin-mian-shi-xi-lie/zui-chang-hui-wen-zi-chuan
        # 双指针 ON2 TIME O1 SPACE
        def Palindrome(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        res = ""
        for i in range(len(s)):
            s1 = Palindrome(i, i)
            s2 = Palindrome(i, i + 1)
            res = res if len(res) > len(s1) else s1
            res = res if len(res) > len(s2) else s2
        return res


        '''
        # DP ON2 TIME ON2 SPACE
        size = len(s)
        if size <= 1:
            return s
        # 二维 dp 问题
        # 状态：dp[l,r]: s[l:r] 包括 l，r ，表示的字符串是不是回文串
        # 设置为 None 是为了方便调试，看清楚代码执行流程
        dp = [[False for _ in range(size)] for _ in range(size)]

        longest_l = 1
        res = s[0]

        # 因为只有 1 个字符的情况在最开始做了判断
        # 左边界一定要比右边界小，因此右边界从 1 开始
        for r in range(1, size):
            for l in range(r):
                # 状态转移方程：如果头尾字符相等并且中间也是回文
                # 在头尾字符相等的前提下，如果收缩以后不构成区间（最多只有 1 个元素），直接返回 True 即可
                # 否则要继续看收缩以后的区间的回文性
                # 重点理解 or 的短路性质在这里的作用
                if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True
                    cur_len = r - l + 1
                    if cur_len > longest_l:
                        longest_l = cur_len
                        res = s[l:r + 1]
        return res
        '''
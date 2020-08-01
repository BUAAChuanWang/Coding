'''
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
'''


class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        # 递归DP 备忘录
        memo = {}

        # dp(i, j)表示text[i]和pattern[j]是否匹配
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j + 1 < len(pattern) and pattern[j + 1] == '*':
                        ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                    else:
                        ans = first_match and dp(i + 1, j + 1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)

        # dp table
        dp = [[False for _ in range(len(pattern) + 1)] for _ in range(len(text) + 1)]
        dp[0][0] = True

        for i in range(len(text) + 1):
            for j in range(1, len(pattern) + 1):
                if pattern[j - 1] == "*":
                    dp[i][j] |= dp[i][j - 2]  # 不匹配
                    if j >= 2 and i >= 1 and pattern[j - 2] in {".", text[i - 1]}:
                        dp[i][j] |= dp[i - 1][j]  # 匹配
                elif i >= 1 and pattern[j - 1] in {".", text[i - 1]}:
                    dp[i][j] |= dp[i - 1][j - 1]
        return dp[-1][-1]

        # DP table 原答案
        m, n = len(s), len(p)

        def matches(i: int, j: int) -> bool:
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    f[i][j] |= f[i][j - 2]
                    if matches(i, j - 1):
                        f[i][j] |= f[i - 1][j]
                else:
                    if matches(i, j):
                        f[i][j] |= f[i - 1][j - 1]
        return f[m][n]

        '''
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])
        '''

        ''' 剑指offer 超时
        m, n = len(s), len(p)
        i, j = 0, 0
        def match(i, j):     
            if i == m and j == n:
                return True    
            if j >= n and i < m:
                return False 
            if j < n - 1 and p[j + 1] == "*":
                if i < m and (s[i] == p[j] or p[j] == "."):
                    return match(i + 1, j) or match(i + 1, j + 2) or match(i, j + 2)
                else:
                    return match(i, j + 2)
            else:
                if i < m and (s[i] == p[j] or p[j] == '.'):
                    return match(i + 1, j + 1)
                else:
                    return False
        return match(0, 0)

        '''
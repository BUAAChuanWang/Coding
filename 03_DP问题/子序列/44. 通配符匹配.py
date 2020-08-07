'''
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
'''


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 递归DP  用备忘录记录
        postfix = ""  # postfix是p的最后全是*的子串
        for index in range(len(p) - 1, -1, -1):
            if p[index] == "*":
                postfix += "*"
            else:
                break
        # print(postfix)
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == len(s) and j == len(p):
                return True
            if i == len(s):
                return True if p[j:] == postfix else False  # 可能出现 s = abcd p = abc*c 在abc*已经匹配完了  所以单独判断
            if j == len(p):
                return False

            if p[j] == "*":
                memo[(i, j)] = dp(i + 1, j) or dp(i, j + 1)
                return memo[(i, j)]
                # return dp(i + 1, j) or dp(i, j + 1)
            elif p[j] == "?":
                memo[(i, j)] = dp(i + 1, j + 1)
                return memo[(i, j)]
                # return dp(i + 1, j + 1)
            else:
                if s[i] == p[j]:
                    memo[(i, j)] = dp(i + 1, j + 1)
                    return memo[(i, j)]
                    # return dp(i + 1, j + 1)
                else:
                    memo[(i, j)] = False
                    return memo[(i, j)]
                    # return False

        res = dp(0, 0)
        return res

        # dp table
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        # base case
        dp[0][0] = True
        for j in range(1, len(p) + 1):
            if p[j - 1] == "*":
                dp[0][j] = True
            else:
                break

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    # 匹配则看当前j"*"能否和上一次i-1时匹配成功；不匹配则直接看i 和 j-1是否匹配成功，j处的“*”直接跳过了
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]  # 匹配 or 不匹配 。
                else:
                    if s[i - 1] == p[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = False
        return dp[-1][-1]

        # 原答案
        m, n = len(s), len(p)

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            if p[i - 1] == '*':
                dp[0][i] = True
            else:
                break

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] | dp[i - 1][j]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]
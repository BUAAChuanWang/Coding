'''
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
'''
class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        # dp table
        dp = [[False for _ in range(len(pattern) + 1)] for _ in range(len(text) + 1)]
        dp[0][0] = True
        for j in range(1, len(pattern) + 1):
            if pattern[j] == "*":
                dp[0][j] = True
            else:
                break

        for i in range(1, len(text) + 1):
            for j in range(1, len(pattern) + 1):
                if pattern[j - 1] == "*":
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]  # 匹配 or 不匹配
                elif pattern[j - 1] == "." or text[i] == pattern[j]:
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[-1][-1]


        '''
        # https://labuladong.gitbook.io/algo/dong-tai-gui-hua-xi-lie/dong-tai-gui-hua-zhi-zheng-ze-biao-da
        memo = {}
        # dp(i, j)表示text[i]和pattern[j]是否匹配
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = first_match and dp(i+1, j) or dp(i, j+2)  # 匹配 or 不匹配
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)
        '''
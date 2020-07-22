# 最长公共子串
while 1:
    str1 = input()
    str2 = input()

    def LCS(str1, str2):
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        maxi, cur = 0, None
        for i in range(m):
            for j in range(n):
                if str1[i] == str2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                if maxi < dp[i + 1][j + 1]:
                    maxi = dp[i + 1][j + 1]
                    cur = i + 1
        return str1[cur - maxi : cur] if cur else ""
    print(LCS(str1, str2))

# 最长公共子序列
while 1:
    str1 = input()
    str2 = input()

    def LCS(str1, str2):
        m, n = len(str1), len(str2)
        res = ""
        # 构建 DP table 和 base case
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # 进行状态转移
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    res += str1[i - 1]
                    # 找到一个 lcs 中的字符
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1], res
    print(LCS(str1, str2))
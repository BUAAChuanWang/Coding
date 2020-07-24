'''
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
 

示例 1：

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
'''


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 20200722
        # 递归写dp的写法都是逆向，（比如ali笔试第二题）然后加一个memo。
        # dpij是现在有word1在i，word2在j，然后计算ij到-1-1的花费
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            # base case
            if i < 0 and j < 0: return 0
            if i < 0: return j + 1
            if j < 0: return i + 1

            if word1[i] == word2[j]:
                memo[(i, j)] = dp(i - 1, j - 1)
                return memo[(i, j)]
            else:
                memo[(i, j)] = 1 + min(dp(i - 1, j),  # 插入
                                       dp(i, j - 1),  # 删除
                                       dp(i - 1, j - 1))  # 替换
                return memo[(i, j)]

        return dp(len(word1) - 1, len(word2) - 1)

        # 正向dp table , dp table也可以逆向
        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        # 初始化 必要的 不然就错了
        for i in range(1, len(word1) + 1):
            dp[i][0] = i
        for i in range(1, len(word2) + 1):
            dp[0][i] = i

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + 1,  # 插入
                                   dp[i][j - 1] + 1,  # 删除
                                   dp[i - 1][j - 1] + 1)  # 替换
        return dp[-1][-1]

        '''
        # dp 备忘录减少重复计算 从后往前  其实从前往后也是一样的。
        memo = dict() 
        def dp(i, j):
            if (i, j) in memo: 
                return memo[(i, j)] # 备忘录
            # base case
            if i == -1: return j + 1
            if j == -1: return i + 1

            if word1[i] == word2[j]:
                memo[(i, j)] = dp(i - 1, j - 1)# 啥都不做
            else:
                memo[(i, j)] = min(
                    dp(i, j - 1) + 1,    # 插入
                    dp(i - 1, j) + 1,    # 删除
                    dp(i - 1, j - 1) + 1 # 替换
                    )
            return memo[(i, j)]
        return dp(len(word1) - 1, len(word2) - 1)


        # dp table
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            dp[i][0] = i
        for i in range(1, n + 1):
            dp[0][i] = i

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
        return dp[m][n]
        '''

        '''
        # dp 记忆化（备忘录）从前往后
        d = {}
        def helper(i,j,d):
            # print(i, j, d)
            if (i,j) in d: return d[(i,j)]
            if i == len(word1) or j == len(word2):
                ans = len(word1) - i + len(word2) - j
            else:
                if word1[i] == word2[j]:
                    ans = helper(i+1,j+1,d)
                else:
                    ans = min(helper(i+1,j+1,d),helper(i,j+1,d),helper(i+1,j,d)) + 1
            d[(i, j)] = ans
            return ans
        return helper(0,0,d)
        '''
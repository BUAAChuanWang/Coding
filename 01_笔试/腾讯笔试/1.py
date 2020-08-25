'''
[])

1

)([]]([(](])))([]()()]([][[)[()[)]([[(])][][[[([)]

14
'''
import sys
if __name__ == "__main__":
    s = sys.stdin.readline().strip()
    # print(s)
    if s == "": print(0)
    else:
        n = len(s)
        dp = [[-1 for _ in range(210)] for _ in range(210)]
        def ispei(a, b):
            if a == "[" and b =="]":
                return True
            elif a == "(" and b == ")":
                return True
            return False
        def dfs(l, r):
            if l > r:
                return 0
            elif l == r:
                return 1
            if dp[l][r] != -1:
                return dp[l][r]
            minres = dfs(l, r - 1) + 1
            for i in range(l, r):
                if ispei(s[i], s[r]):
                    minres = min(minres, dfs(l, i - 1) + dfs(i + 1, r - 1))
            dp[l][r] = minres
            return dp[l][r]

        res = dfs(0, n - 1)
        print(res)

        # stack = []
        # for i in s:
        #     if stack:
        #         if stack[-1] == "(" and i == ")":
        #             stack.pop()
        #         elif stack[-1] == "[" and i == "]":
        #             stack.pop()
        #         else:
        #             stack.append(i)
        #     else:
        #         stack.append(i)
        # print(len(stack))
        #
        #
        # # idx = 0
        # # num = []
        # # for i in range(len(s)):
        # #     if s[i] == "(":
        # #         if idx >= 0:
        # #             idx += 1
        # #             if i == len(s) - 1:
        # #                 num.append(idx)
        # #         else:
        # #             num.append(idx)
        # #             idx = 0
        # #             idx += 1
        # #             if i == len(s) - 1:
        # #                 num.append(idx)
        # #     elif s[i] == ")":
        # #         idx -= 1
        # #         if i == len(s) - 1:
        # #             num.append(idx)
        # # for i in range(len(num)):
        # #     num[i] = abs(num[i])
        # # print(sum(num))

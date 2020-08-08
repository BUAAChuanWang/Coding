'''
3
5 3 7

6
'''
# import sys
# memo = {}
# def func(n):
#     if n in memo: return memo[n]
#     if n < 2: return 0
#     if n == 2: return 1
#     if n == 3: return 1
#     if n == 4: return 2
#     dp = [0 for _ in range(n + 1)]
#     dp[2] = 1
#     dp[3] = 1
#     dp[4] = 2
#     for i in range(4, n + 1):
#         dp[i] = max(dp[i - 2] + 1, dp[i - 3] + 1)
#     # print(dp[n])
#     return dp[n]
import sys
if __name__ == "__main__":
# while 1:
    N = int(sys.stdin.readline().strip())
    nums = list(map(lambda x:int(x), sys.stdin.readline().strip().split()))
    def f(n):
        return n // 2

    res = 0
    for i in range(N):

        res += f(nums[i])
    print(res)

'''
给一堆（最多15）有价值的东西，均分给2个人，均分不了的，扔掉，求最小扔掉多少
1
5
30 60 5 15 30

20
'''
import sys
if __name__ == "__main__":

    def dfs(first, second, cost, index):
        global minLoss
        if (index >= N):
            if (first == second):
                minLoss = min(minLoss, cost)
                return
        if (first == second):
            minLoss = min(minLoss, suffixSum[index] + cost)
        if (abs(first - second) > suffixSum[index]):
            return
        # 给first，给second，扔掉
        dfs(first + nums[index], second, cost, index + 1)
        dfs(first, second + nums[index], cost, index + 1)
        dfs(first, second, cost + nums[index], index + 1)


    T = int(sys.stdin.readline().strip())
    for i in range(T):
        N = int(sys.stdin.readline().strip())
        nums = list(map(lambda x:int(x), sys.stdin.readline().strip().split()))
        # nums = sorted(nums, reverse=True)
        minLoss = float("inf")
        suffixSum = [0] * (N + 1)
        # for i in range(N - 1, -1 , -1):
        #     suffixSum[i] = suffixSum[i + 1] + nums[i]
        # print(suffixSum)
        # dfs(0, 0, 0, 0);
        # print(minLoss)

        # DP  背包
        '''
        i索引的是物品，j索引两个人拿到物品的价差，dp维护已经分配好的物品的最大sum，
        先初始化为负无穷，当前物品可能扔给少的，也可能扔给多的，给少的就会缩小差距（j-ai），给多的就会增大差距（j+ai），
        (n,0)就是所有物品看过后，使价差为0，能够分配出去的最大sum，其他就要扔掉
        '''
        summ = sum(nums)
        nums = [0] + nums
        dp = [[float("-inf") for _ in range(summ + max(nums) + 1)]for _ in range(N + 1)]
        dp[0][0] = 0
        for i in range(1, N + 1):
            for j in range(summ + 1):
                dp[i][j] = dp[i - 1][j]
                dp[i][j] = max(dp[i][j], max(dp[i - 1][j + nums[i]] + nums[i], dp[i - 1][abs(j - nums[i])] + nums[i]))
        print(summ - dp[N][0])
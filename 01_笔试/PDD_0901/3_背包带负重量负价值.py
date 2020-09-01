'''
4 4
-1 -1
1 -1
-1 1
6 6

6

6 4
2 6
2 10
2 10
-2 -3
-2 -3
4 60

74

3 4
2 6
2 10
2 10

20

3 6
-2 9
-2 -30
10 15

9
'''
import sys
import functools
# if __name__ == "__main__":
while 1:
    # 读取第一行的n
    n, m = list(map(lambda x:int(x), sys.stdin.readline().strip().split(" ")))
    nums = []
    for i in range(n):
        nums.append(list(map(lambda x:int(x), sys.stdin.readline().strip().split(" "))))

    # 负重量
    # 题意：普通的01背包，但是现在体积可能为负数。
    # 思路：一眼题，因为体积为负数，表示我们的体积会变大，这种情况，我们把它变为相反数即可
    # 表示我一开始就装进去，那么在跑背包的时候如果选择了它的相反数这个物体，代表把它移除。（而这个时候所有的物体都是正他体积，跑01背包就行。）
    ans = 0
    for i in range(len(nums)):
        c, v = nums[i]
        if c < 0:
            m -= c
            ans += v
            nums[i] = [-c, -v]
    # 相当于先把背包扩充，然后进行常规背包dp，
    # 这时如果选中了原始为负值的物品，就相当于是没选这个物品（因为初始加了这个物品扩充了背包同时也对初始收益做了赋值）；
    # 如果没选就相当于选这个物品做了扩充。  最终结果=初始背包收益+常规dp背包收益
    @functools.lru_cache(None)
    def dp(bag, index):
        res = 0
        if bag == 0: return 0
        if bag < 0: return float("-inf")  # 这个base case非常重要 不能忘记
        for i in range(index, n):
            c, v = nums[i]
            res = max(res, v + dp(bag - c, i + 1))
        return res
    res = dp(m, 0)
    print(res + ans)  # 结果就是初始背包收益+常规dp背包收益

    # 常规背包 全为正直的解法
    # 正重量 正价值
    @functools.lru_cache(None)
    def dp(bag, index):
        if bag == 0: return 0
        if bag < 0: return float("-inf")  # 这个base case非常重要 不能忘记
        res = 0
        for i in range(index, n):
            c, v = nums[i]
            res = max(res, v + dp(bag - c, i + 1))
        return res
    res = dp(m, 0)
    print(res)
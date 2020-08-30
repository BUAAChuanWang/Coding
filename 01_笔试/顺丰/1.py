'''
分割序列
时间限制： 3000MS
内存限制： 786432KB
题目描述：
现有一序列，长度为n，所有元素均为整数元素。序列中一些元素是确定值，另一些元素是不确定的。 你的任务是将所有不确定值的元素赋予一个正整数值，使得将整个序列分割成最少的段，每一个段都是一个等差数列。 特别的，长度为1和2的段都是等差数列。

范围

对于100%的数据，n≤100000,数据组数不会超过10，出现的数字不会超过109，且除-1外都是正整数



输入描述
输入包含多组数据，对每组数据第一行包含一个整数n 接下来一行n个整数，空格隔开。如果数为-1,代表该元素不确定，否则该元素为确定值，输入的是这个数的值。

输出描述
输出一行一个数，代表分割后最少的段数，使得每一段都是等差数列


样例输入
3
-1 -1 -1
3
-1 -1 1
3
1 -1 2
7
-1 -1 -1 4 5 1 2
样例输出
1
1
2
2

提示
可以按照以下来填这四组数据
1 1 1
1 1 1
1 1 2
1 2 3 4 5 1 2
'''
import collections
while 1:
    n = int(input())
    nums = list(map(int, input().strip().split(" ")))
    if n == 1 or n == 2:
        print("1")
        continue
    counter = collections.Counter(nums)
    if counter[-1] == n or counter[-1] == n - 1:
        print("1")
        continue

    def helper(nums):
        if not nums:
             return 0
        res = float("inf")
        x = None
        for i in range(len(nums)):
            if nums[i] != -1:
                x = i
                break
        if x != None:
            flag = 1 if nums[x] > x else 2
        else:
            return 0
        while x < len(nums) and nums[x] != -1:
            x += 1
        res = min(res, flag + helper(nums[x : ]))
        return res
    t1 = helper(nums)

    t2 = 1
    tmp = [x for x in nums if x != -1]
    pre = tmp[1]
    dif = tmp[1] - tmp[0]
    for i in range(2, n):
        if tmp[i] == -1: continue
        if tmp[i] - pre != dif:
            t2 += 1
        dif = tmp[i] - pre
        pre = tmp[i]
    print(t1, t2)
    print(t1 + t2)



    # i = 0
    # while i < n and nums[i] == -1:
    #     i += 1
    # res = 1 if nums[i] > i else 2
    # diff = None
    # while i < n:
    #     cnt = 0
    #     if nums[i] != -1:
    #         prenum = nums[i]
    #         preidx = i
    #         i += 1
    #
    #         continue
    #     while i < n and nums[i] == -1:
    #         i += 1
    #     if (nums[i] - prenum) % (i - preidx - 1) != 0:
    #         res += 1
    #     else:
    #         span = (nums[i] - prenum) // (i - preidx - 1)
    #
    # for i in range(n):
    #     if nums[i] != -1:
    #         span = nums[i] - nums
    #         pre = nums[i]
    #     if nums[i] == -1:

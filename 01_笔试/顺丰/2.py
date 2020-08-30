'''
货车运输
时间限制： 3000MS
内存限制： 589824KB
题目描述：
港口新到了n个货物，工人们需要将它们通过货车运送到公司。货物会先后到达港口，第i个到达港口的货物是第i号，价值是a[i]。
现在有k辆货车，每辆货车可以将编号连续的货物一起运输，容量无限，运输费用为该车货物价值的和的平方，每辆车必须装载货物。
你是运输货车公司的老板，你想在赚大钱的同时降低每辆车装载货物数以控制成本。
请问最大的运输费用是多少，以及在费用最大时装载货物最多的货车至少需要装载多少货物。

输入描述
第一行两个数n,k。

接下来n个数a[]，第i个数为a[i]。

输出描述
两个数，第一个数表示最大运输费用，第二个数表示此时运输货物最多的货车最少需要装载的货物数量。


样例输入
6 3
0 0 1 1 0 0
样例输出
4 2

7 3
0 1 0 8 9 0 3
提示
1≤k≤n≤300
0≤a[i]≤100

分组(1 2)(3 4)(5 6)，费用为0+2+0 = 2, 货车最大装载量为2。
'''
import copy
while 1:
    n, k = input().strip().split(" ")
    n, k = int(n), int(k)
    a = list(map(int, input().strip().split(" ")))
    if n == k:
        cost = sum([x ** 2 for x in a])
        num = 1
        print(str(cost) + " 1")
        continue

    t = n - k + 1
    i = 0
    presum = [x for x in a]
    for i in range(1, n):
        presum[i] += presum[i - 1]
    presum = [0] + presum
    # print(f"presum={presum}")

    def cut(l):
        x = len(l)
        i = 0
        while i < x and l[i] == 0:
            i += 1
        j = x - 1
        while j >= 0 and l[j] == 0:
            j -= 1
        return l[i : j + 1]
    # print(f"cut:{cut([0,0,1,0,1,0])}")

    sta, end = 0, 0
    cost = 0
    res = 0
    num = float("inf")
    for i in range(k):
        tmp = res
        res = max(res, (presum[i + t] - presum[i]) ** 2)
        if tmp == res:
            if num > len(cut(a[i: i + t])):
                sta, end = i, i + t
            num = min(num, len(cut(a[i: i + t])))
        else:
            num = len(cut(a[i : i + t]))
            sta, end = i, i + t
    # print(f"sta={sta}, end={end}")
    cost = res + sum([x ** 2 for x in list(a[ : sta] + a[end : ])])
    print(str(cost) + " " + str(num))
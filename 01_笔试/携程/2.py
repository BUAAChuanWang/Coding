'''
求解最少购买旅游产品数量
时间限制： 3000MS
内存限制： 589824KB
题目描述：
给定一笔经费金额和一组旅游产品以及对应的价格。同一个产品可以重复购买多份。

问：最少能够购买多少份产品，正好花掉所有的经费。若没有任何一种产品组合能够正好花掉所有的经费，返回-1.



输入描述
第一行 若干个元素，每个元素表明每种旅游产品的价格，元素之间用空格隔开。

价格均为整数，每种旅游产品的价格均不一样。

第二行 一个整数，表示经费总金额

输出描述
当前经费正好能够购买的最少产品数量。

如果没有一种产品组合能够花掉所有的经费，返回-1.


样例输入
10 20 50
110
样例输出
3
'''
while 1:
    prices = list(map(lambda x: int(x), input().split(" ")))
    amount = int(input())

    queue = [(amount, 0)]
    seen = {amount}
    flag = True
    while queue:
        cur, step = queue.pop(0)
        if cur == 0:
            flag = False
            print(step)
        for i in range(len(prices)):
            if cur - prices[i] >= 0 and cur - prices[i] not in seen:
                seen.add(cur - prices[i])
                queue.append((cur - prices[i], step + 1))
    if flag: print(-1)
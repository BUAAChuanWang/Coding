'''
调整排列
时间限制： 3000MS
内存限制： 589824KB
题目描述：
给定一个1到N的排列P1到PN（N为偶数），初始时Pi=i（1≤i≤N），现在要对排列进行M次操作，每次操作为以下两种中一种：

①将排列的第1个数移到末尾；

②交换排列的第1个数与第2个数、第3个数与第4个数、...、第N-1个数与第N个数。

求经过这M次操作后得到的排列。



输入描述
第一行包含两个整数N和M，2≤N，M≤105。

第二行包含M个空格隔开的整数t1到tM，1≤ti≤2。若ti=1，则表示第i次操作为操作①；若ti=2，则表示第i次操作为操作②。

输出描述
输出N个空格隔开的整数，即经过M次操作后得到的排列。


样例输入
4 3
1 2 1
样例输出
2 1 4 3

10 6
1 2 1 1 2 1

提示
排列变化过程为：{1 2 3 4}->{2 3 4 1}->{3 2 1 4}->{2 1 4 3}。
'''
while 1:
    # 找规律  按奇数偶数找规律
    n, m = input().strip().split(" ")
    n, m = int(n), int(m)
    op = list(map(int, input().strip().split(" ")))
    a, b = 1, 2
    cur = 1
    for i in range(m):
        if op[i] == 1:
            if cur == 1: a += 2
            else: b += 2
        cur = 1 - cur
    print(f"a={a}, b={b}, cur={cur}")
    res = []
    for i in range(1, n + 1):
        print(f"i={i}, cur={cur}, i+cur+1={i+cur+1}, &={(i+cur+1)&1}")
        if (i + cur + 1) & 1:
            print(f"a={a}, n={n}, a%n={a%n}")
            a = a % n if a % n else n
            print(f"a={a}")
            res.append(a)
            a += 2
        else:
            print(f"b={b}, n={n}, b%n={b % n}")
            b = b % n if b % n else n
            print(f"b={b}")
            res.append(b)
            b += 2
    print(" ".join(list(map(str, res))))


    # 暴力模拟 超时 AC27
    string = [str(x) for x in range(1, n + 1)]

    for i in range(m - 1):
        if op[i] == 2 and op[i] == op[i + 1]:
            op = op[:i] + op[i + 2:]

    def back(string):
        string = string[1:] + [string[0]]
        return string

    def switch(string):
        i = 0
        while i < n:
            string = string[ : i] + [string[i + 1]] + [string[i]] + string[i + 2 : ]
            i += 2
        return string

    for a in op:
        if a == 1: string = back(string)
        if a == 2: string = switch(string)
    string = list(string)
    print(" ".join(string))
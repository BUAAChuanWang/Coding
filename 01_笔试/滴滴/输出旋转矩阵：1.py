'''
斐波那契蛇
时间限制： 3000MS
内存限制： 589824KB
题目描述：
小明昨晚做了一个梦。在梦里，很多很多斐波那契数连成了一条蛇。突然，最大的那个数变成了蛇头，把小明一口给吞到肚子里去了。

小明被吓醒了，他赶紧拿笔在纸上面画了一条斐波那契蛇。



这是一个蛇形迂回的斐波那契数列，它是一个n*n的矩阵，在上面的矩阵中n=3。第1行第1列是最大值，然后按照顺时针的次序数字逐渐变小。

下面是n=4时的情况：



小明希望你能够编写一个程序，输入一个正整数n，然后逐行逐列输出斐波那契蛇形矩阵中的元素。



输入描述
单组输入，输入数据占一行，包含一个正整数n，表示斐波那契蛇形矩阵的大小。(n<10)

输出描述
输出数据占一行，逐行逐列（从第1行开始到第n行，每一行从第1列开始到第n列）输出斐波那契蛇形矩阵中的元素，每两个数字之间用一个空格隔开。


样例输入
3
样例输出
34 21 13
1 1 8
2 3 5
'''

while 1:
    n = int(input())
    if not n: print()
    if n == 1: print(1)
    x = n * n
    f = [0] * x
    f[0], f[1] = 1, 1
    for i in range(2, x):
        f[i] = f[i - 1] + f[i - 2]
    res = [[0 for _ in range(n)] for _ in range(n)]
    t, b, l, r = 0, n - 1, 0, n - 1
    index = x - 1
    flag = True
    while 1:
        for i in range(l, r + 1):
            if index < 0:
                flag = False
                break
            res[t][i] = f[index]
            index -= 1
        if not flag: break
        t += 1
        if t > b: break

        for i in range(t, b + 1):
            if index < 0:
                flag = False
                break
            res[i][r] = f[index]
            index -= 1
        if not flag: break
        r -= 1
        if r < l: break

        for i in range(r, l - 1, -1):
            if index < 0:
                flag = False
                break
            res[b][i] = f[index]
            index -= 1
        if not flag: break
        b -= 1
        if t > b: break

        for i in range(b, t - 1, -1):
            if index < 0:
                flag = False
                break
            res[i][l] = f[index]
            index -= 1
        if not flag: break
        l += 1
        if l > r: break
    for i in range(n):
        t = res[i]
        t = [str(a) for a in t]
        t = " ".join(t)
        print(t)
    # print(res)


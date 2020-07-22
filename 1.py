'''
双行道
时间限制：C/C++语言 1000MS；其他语言 3000MS
内存限制：C/C++语言 65536KB；其他语言 589824KB
题目描述：
有一个2*n的网格，有一个人位于(1,1)的位置，即左上角，他希望从左上角走到右下角，即(2,n)的位置。在每一次，他可以进行三种操作中的一种：

1． 向右走一格，即从(x,y)到(x,y+1);

2． 向上右方走一格，即，如果他在(2,y)的位置可以走到(1,y+1);

3． 向下右方走一格，即，如果他在(1,y)的位置可以走到(2,y+1);



问题当然不会这么简单，在这2*n的格子中，有一部分格子上有障碍物，他不能停在障碍物上，当然也不能走出网格，请问他有多少种不同的路线可以到达(2,n)。

输入
输入第一行仅包含一个正整数n，表示网格的长度。(1<=n<=50)

接下来有2行,每行有n个字符，“X”代表障碍物，“.”代表可以停留。

输出
如果没有可以到达的路线则输出-1，否则输出方案数量。


样例输入
5
..X.X
XX...
样例输出
2

规则
请尽量在全场考试结束10分钟前调试程序，否则由于密集排队提交，可能查询不到编译结果
点击“调试”亦可保存代码
编程题可以使用本地编译器，此页面不记录跳出次数
'''
while 1:

    n = input()
    if n == "":
        break
    str1 = input()
    str2 = input()

    n = int(n)
    nums = [[0] * n for _ in range(2)]
    i = 0
    for s in str1:
        if s == "X":
            nums[0][i] = 1
        i += 1
    i = 0
    for s in str2:
        if s == "X":
            nums[1][i] = 1
        i += 1
    # print(nums)
    if nums[0][0] == 1:
        print(-1)
        continue
    if nums[1][-1] == 1:
        print(-1)
        continue

    dp = [[0 for _ in range(n)] for _ in range(2)]
    dp[0][0] = 1
    dp[1][0] = 0
    for j in range(1, n):
        for i in range(2):
            if i == 0:
                if nums[i][j] == 0:
                    dp[i][j] = dp[i][j - 1] + dp[i + 1][j - 1]
                elif nums[i][j] == 1:
                    dp[i][j] = 0
            elif i == 1:
                if nums[i][j] == 0:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
                elif nums[i][j] == 1:
                    dp[i][j] = 0
    if dp[-1][-1] == 0:
        print(-1)
    else:
        print(dp[-1][-1])

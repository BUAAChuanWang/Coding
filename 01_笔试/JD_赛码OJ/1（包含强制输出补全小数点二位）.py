'''
X星人的基因由A、B、C、D、E五种不同的结构组合而成。

如果两个性别不同的X星人的基因序列相似度大于50%，按照X星的法律他们是禁止结婚的，等于50%据说还是可以的。

那么基因的相似度怎么计算呢？分别从两个人身上取长度均为N的基因片段，如果它们的最长公共子序列（注意，最长公共子序列不需要连续）的长度为M，则相似度=M/N。是不是很简单呢？

现在给你两段X星人的基因序列片段，请你判断他们是不是可以结婚？



输入描述
单组输入。

每一组测试数据包含3行：

第1行数字N表示待比较基因序列片段的长度，N<=10^3。

第2行和第3行为两个长度为N的基因序列片段，中间以空格隔开。

输出描述
先输出相似度，结果保留两位小数（四舍五入），然后输出判断结果（中间以空格隔开），如果可以输出”Yes“，如果不可以输出”No“。


样例输入
6
A B C D E E
A E D C B B
样例输出
0.33 Yes
'''
while 1:
    #
    a = 0.3
    b = 0.456
    print("%.2f" % b)
    print("%.2f" % a)
    print(round(0.3, 2))
    break
    N = int(input())
    l1 = input().strip()
    l2 = input().strip()

    def func(A, B):
        m, n = len(A), len(B)
        ans = 0
        dp = [[0 for _ in range(n + 1)]for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        # print(ans)
        return ans

    if N == 0:
        print("Yes")
    else:
        text1 = l1.replace(" ", "")
        text2 = l2.replace(" ", "")
        # print(text1, text2)
        m = func(text1, text2)
        res = m / N
        if m / N == 0:
            print("0.00", "Yes")
        elif m / N <= 0.5:
            print("%.2f" % res, "Yes")  # 强制补全2位小数
        else:
            print("%.2f" % res, "No")

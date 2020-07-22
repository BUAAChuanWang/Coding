'''
1、从n个人中选择任意数量的人员组成一支队伍，然后从一支队伍中选出一位队长，不同的队长算不同的组合，问这样的组合的数量对10^9+7取模 。
数据范围：1 <= n <= 1000000000;
示例:
输入：n = 2
输出：4
解释,(1),(2)(1,2),(2,1)四种，括号第一个为队长

思路:
首先一看数据范围，应该要O(logN)级别的方法才能AC,分析问题首先应该是个排列组合问题，得到通项公式为：
$res = \sum_{i=1}^ni*C_n^ires=∑
思路1：可以暴力算，当然不推荐，算了也是白算
思路2：动态规划，没写出来，而且也达不到O(logN)复杂度
思路3：数学知识告诉我们，res的通项公式为：
要求2^n - 1，O(logN)复杂度，经典的快速幂算法。
小知识：介绍一个解决找规律问题的好网站OEIS（ 在线整数数列查询网站 http://oeis.org/ ），笔试的时候手机被锁了，没想到用电脑去查一查，好气
'''
# Code:
while 1:
    n = int(input())
    
    # 循环乘法
    def pow(x, n):
        # base case
        if n == 0 or x == 1: return 1
        if x == -1:
            if abs(n & 1) == 0:
                return 1
            else:
                return -1
        if n == 1:
            return x
        if n == -1:
            return 1 / x
        if n < 0:
            x = 1 / x
            n = -n
        # 循环乘法
        res, current_product = 1, x
        while n > 0:
            if n & 1 == 1:
                res = res * current_product
            current_product = current_product * current_product
            n = n >> 1
        return res
    print(n * pow(2, n - 1) % (10 ** 9 + 7))

    # 快速幂法:
    '''
    快速幂：
    1,当n为偶数时，x(n) = (x * x)(n / 2)
    2,当n为奇数时，x(n) = (x * x)((n - 1) / 2) * x
    '''
    def pow(x, n):
        # 为了让代码简单 循环乘法中的base case就不复制过来了
        # 快速幂
        if n == 0:
            return 1
        if n == 1:
            return x
        if n & 1:
            return x * pow(x * x, (n - 1) // 2)
        else:
            return pow(x * x, n // 2)
    print(n * pow(2, n - 1) % (10 ** 9 + 7))
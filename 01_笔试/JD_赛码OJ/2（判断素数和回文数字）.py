'''
题目描述：
现有一个正整数，希望去掉这个数中某一个数字之后可以得到一个回文素数。

回文素数是指一个素数同时还是一个回文数（回文数即从左到右和从右到左均一样的数，例如12321）。【注意：一位数也被认为是回文数】

输入两个正整数N和M，满足N<M，请编写一个程序统计N和M之间存在多少个满足上述要求的数？



输入描述
单组输入。

输入一行，包含两个正整数N和M，1<=N<M<=1000000，两个数字之间用空格隔开。

输出描述
输出在N和M之间（包含N和M）满足要求的数的个数。


样例输入
110 120
样例输出
10

提示
样例解释
在110和120之间存在10个满足要求的数，分别是110、111、112、113、114、115、116、117、118和119，它们去掉最后一位数都可以得到一个回文素数11。120不符合。故最终结果为10
'''
memo = set()
not_memo = set()
while 1:
    N, M = input().split(" ")
    N, M = int(N), int(M)
    '''
    def isPrime(n):  # 判断素数
        return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))
    '''
    def isPrime(n):  # 判断素数
        if n in memo:
            return True
        if n in not_memo:
            return False
        t = n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))
        if t:
            memo.add(n)
        if not t:
            not_memo.add(n)
        return t

    def reverse(x):  # 判断回文数
        ans = 0
        while x:
            ans = 10 * ans + x % 10
            x //= 10
        return ans

    res = 0
    for i in range(N, M + 1):
        s = str(i)
        flag = False
        for j in range(len(s)):
            if flag:
                break
            new_s = s[ : j] + s[j + 1 : ]
            new_s = int(new_s)
            if new_s == reverse(new_s) and isPrime(new_s):
                # print(new_s)
                flag = True
                res += 1

    print(res)


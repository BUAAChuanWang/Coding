'''
给一个整数x，一定存在若干对整数（a,b）  使得x ^ a ^ b取得最大值（^异或）
其中x a b均取值[0, 2^31)
求出所有符合要求的（a,b）中，abs(a-b)最小的方案个数

输入
第一行有一个整数代表测试数据个数T([1,150])个
接下来有T行，每行一个整数x
输出
对于每组测试数据，输出一行
每行只有一个整数，代表答案

例子：
input：
2
0
100

output:
2
16

'''
import sys

if __name__ == "__main__":
    # 读取第一行的t
    t = int(sys.stdin.readline().strip())
    input = 0
    res = []
    for i in range(t):
        # 读取每一行
        num = int(sys.stdin.readltine().strip())
        num = str(bin(num))[2:]
        num = [int(i) for i in num]
        s = sum(num)
        res.append(2 ** (s + 1))
    for r in res:
        print(r)


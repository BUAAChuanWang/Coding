'''
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
'''
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 20200705
        # 模拟列式乘法
        if num1 == "0" or num2 == "0": return "0"
        res = [0 for i in range(len(num1) + len(num2))]
        for i, n1 in enumerate(num1[::-1]):
            for j, n2 in enumerate(num2[::-1]):
                d = int(n1) * int(n2)
                low, high = i + j, i + j + 1
                dlow, dhigh = d % 10, d // 10
                carry = (res[low] + dlow) // 10
                res[low] = (res[low] + dlow) % 10
                res[high] = res[high] + dhigh + carry
        for a in res[::-1]:
            if a == 0:
                res.pop()
            break
        return "".join(list(map(lambda x:str(x), res[::-1])))


        '''
        # 优化 但是却更慢 我吐了
        if num1 == "0" or num2 == "0": return "0"
        m, n = len(num1), len(num2)
        res = [0] * (m + n)
        num1, num2 = num1[::-1], num2[::-1]
        for i in range(n):
            n2 = num2[i]
            for j in range(m):
                n1 = num1[j]
                x = int(n1) * int(n2) + res[i + j]
                res[i + j] = x % 10
                res[i + j + 1] += x // 10
        while res[-1] == 0:
            res = res[:-1]
        for i in range(len(res)):
            res[i] = str(res[i])
        return "".join(res[::-1])
        '''
        # 普通思路 反而更快。。。
        num1 = int(num1)
        res = 0
        bit = 1

        for num in reversed(num2):
            res += int(num) * num1 * bit
            bit *= 10
        return str(res)
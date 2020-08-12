'''
不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。

示例 1:

输入: a = 1, b = 2
输出: 3
示例 2:

输入: a = -2, b = 3
输出: 1
'''


class Solution(object):
    def getSum(self, a, b):
        '''
首先有符号整数的值域应该为 [-8, 7] 对于初步运算的结果,当结果小于8直接返回就可.
对于大于 7 的结果, 可知符号位必为1. 现在的问题转化为, 如何通过位运算把负数转换出来.
假设python用的是 8bit 有符号整数,当前结果为0000 1100, 对应8bit有符号整数为12, 但结果应该为-4对应8bit有符号整数为1111 1100
通过两步转换可以得到:

结果 与 0b1111 异或
对异或结果按位取反

~(a ^ 0xF)
这样就搞定了4bit 有符号加法,同理可以拓展到32bit

链接：https://leetcode-cn.com/problems/sum-of-two-integers/solution/python-wei-yun-suan-yi-xie-keng-by-lih/
        '''
        # 2^32
        MASK = 0x100000000
        # 整型最大值
        MAX_INT = 0x7FFFFFFF
        MIN_INT = MAX_INT + 1
        # print(MIN_INT, MASK)

        while b != 0:
            # 计算进位
            carry = (a & b) << 1
            # 取余范围限制在 [0, 2^32-1] 范围内
            a = (a ^ b) % MASK
            b = carry % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)

    # https://leetcode-cn.com/problems/sum-of-two-integers/solution/wei-yun-suan-xiang-jie-yi-ji-zai-python-zhong-xu-y/

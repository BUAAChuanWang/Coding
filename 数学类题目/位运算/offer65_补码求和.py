'''
剑指 Offer 65. 不用加减乘除做加法
写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。



示例:

输入: a = 1, b = 1
输出: 2
'''
class Solution:
    def add(self, a: int, b: int) -> int:
        # https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/solution/pythonti-jie-er-jin-zhi-zhuan-hua-yi-ji-pythonzhua/
        '''
        在32位的系统中int类型的表示范围为[-231,231-1],在python里如果补码超过了2**31-1这个边界,
        那么他代表的原码就是一个负数,我们需要将它转换成对应的源码,而正数的补码等于其源码不用转换

        原码转补码:
        正数的原码即补码不用转换,如果是负数的话通过n & 0xffffffff进行转换
        补码转原码(两种)
        通过-((n-1) & 0xffffffff)或者~(n ^ 0xffffffff)都可以进行转换
        '''
        # (n & 0xffffffff)进行这种变换的原因是,如果存在负数则需要转换成补码的形式,正数补码是他本身
        a &= 0xffffffff#
        b &= 0xffffffff
        while b != 0:
            carry = ((a & b) << 1) & 0xffffffff#如果是负数,转换成补码形式
            a ^= b
            b = carry
        if a < 0x80000000:#如果是正数的话直接返回
            return a
        else:
            return  ~(a^0xffffffff)#是负数的话,转化成其原码

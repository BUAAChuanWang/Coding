'''
给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以字符串形式返回小数。

如果小数部分为循环小数，则将循环的部分括在括号内。

示例 1:

输入: numerator = 1, denominator = 2
输出: "0.5"
示例 2:

输入: numerator = 2, denominator = 1
输出: "2"
示例 3:

输入: numerator = 2, denominator = 3
输出: "0.(6)"
'''
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # https://leetcode-cn.com/problems/fraction-to-recurring-decimal/solution/pythonxun-zhao-di-yi-ge-zhong-fu-de-yu-shu-by-wdmm/
        flag = 1 if numerator * denominator >= 0 else 0
        numerator, denominator = abs(numerator), abs(denominator)
        head = numerator // denominator
        head = str(head) if flag else "-" + str(head)
        post = []
        rest = numerator % denominator
        rest_dic = {}
        index = 0
        while rest != 0 and rest not in rest_dic:
            rest_dic[rest] = index
            index += 1
            rest = rest * 10
            post.append(str(rest // denominator))
            rest = rest % denominator
        if not rest_dic:
            return head
        elif rest == 0:
            return head + "." + "".join(post)
        elif rest != 0:
            return head + "." + "".join(post[:rest_dic[rest]])+'('+''.join(post[rest_dic[rest]:])+')'
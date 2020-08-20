'''
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
说明:

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # KMP和get_pnext基本一模一样 就一点变化
        def KMP(string, substring):
            pnext = get_pnext(substring)
            i, j = 0, 0
            while i < len(string) and j < len(substring):
                if string[i] == substring[j]:
                    i += 1
                    j += 1
                elif j != 0:
                    j = pnext[j - 1]
                else:
                    i += 1
            return i - j if j == len(substring) else -1

        def get_pnext(substring):
            # 构建pnext   penxt先全部赋值0；i从1开始！
            # abcabec = 0001200
            pnext = [0 for _ in range(len(substring))]
            i, j = 1, 0
            while i < len(substring):
                if substring[i] == substring[j]:
                    pnext[i] = j + 1  # 只有这里多了这一行！
                    i += 1
                    j += 1
                elif j != 0:
                    j = pnext[j - 1]
                else:
                    i += 1
            # print(pnext)
            return pnext

        res = KMP(haystack, needle)
        return res

        # def KMP(string, substring):
        #     pnext = get_pnext(substring)

        #     i, j = 0, 0
        #     while i < len(string) and j < len(substring):
        #         if string[i] == substring[j]:
        #             i += 1
        #             j += 1
        #         elif j != 0:
        #             j = pnext[j - 1]
        #         else:
        #             i += 1
        #     return i - j if j == len(substring) else -1

        # def get_pnext(substring):
        #     pnext = [0 for _ in range(len(substring))]
        #     i, j = 1, 0
        #     while i < len(substring):
        #         if substring[i] == substring[j]:
        #             pnext[i] = j + 1
        #             i += 1
        #             j += 1
        #         elif j != 0:
        #             j = pnext[j - 1]
        #         else:
        #             i += 1


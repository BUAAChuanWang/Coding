'''
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

示例 1:
s = "abc", t = "ahbgdc"
返回 true.

示例 2:
s = "axc", t = "ahbgdc"
返回 false.

进阶 :
如果有大量输入的 S，称作S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
        # 双指针  对该问题 ON time  可以了
        i, j = 0, 0
        while i < len(s):
            while j < len(t) and t[j] != s[i]:
                j += 1
            if j < len(t) and t[j] == s[i]:
                i += 1
                j += 1
            else:
                return False
        return True
        '''
        # Follow up进阶问题 多个S, 具体在pycharm里面 这里s还是按一个字符串来做的 实际进阶问题是s是个list
        # 二分 + 哈希
        def get_lbound(lis, target):
            l, r = 0, len(lis)
            while l < r:
                mid = l + (r - l) // 2
                if lis[mid] >= target:
                    r = mid
                if lis[mid] < target:
                    l = mid + 1
            return l

        index = collections.defaultdict(list)
        for i in range(len(t)):
            index[t[i]].append(i)

        j = 0
        for i in range(len(s)):
            if s[i] not in index:
                return False
            pos = get_lbound(index[s[i]], j)
            if pos == len(index[s[i]]):
                return False
            j = index[s[i]][pos] + 1
        return True

# isSubsequence(["abc", "bd", "rf", "ad"], "egalblcldfr")
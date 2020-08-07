'''
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

示例 1:

输入: 2
输出: [0,1,1]
示例 2:

输入: 5
输出: [0,1,1,2,1,2]

进阶：
给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
要求算法的空间复杂度为O(n)。
你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。
'''
class Solution:
    def countBits(self, num: int) -> List[int]:
        # O(n)
        # https://leetcode-cn.com/problems/counting-bits/solution/dong-tai-gui-hua-wei-yun-suan-xing-zhi-python3-by-/
        '''
        二进制的两个特性：
        奇数的二进制中1的个数=它上一位偶数的二进制中1的个数+1。  如：13=1101  12=1100
        偶数中二进制1的个数等于这个偶数除以2后的数二进制1的个数。  如：10=1010 5=101
        '''
        dp = [0 for _ in range(num + 1)]
        dp[0] = 0
        if num >= 1: dp[1] = 1
        for i in range(2, num + 1):
            dp[i] = dp[i // 2] if i % 2 == 0 else dp[i - 1] + 1
        return dp


        # O(n * len(c))
        res = []
        for i in range(num + 1):
            count = 0
            for c in str(bin(i))[2:]:
                if c == "1":
                    count += 1
            res.append(count)
        return res
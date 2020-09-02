'''
请你帮忙设计一个程序，用来找出第 n 个丑数。
丑数是可以被 a 或 b 或 c 整除的 正整数。

示例 1：

输入：n = 3, a = 2, b = 3, c = 5
输出：4
解释：丑数序列为 2, 3, 4, 5, 6, 8, 9, 10... 其中第 3 个是 4。
示例 2：

输入：n = 4, a = 2, b = 3, c = 4
输出：6
解释：丑数序列为 2, 3, 4, 6, 8, 9, 10, 12... 其中第 4 个是 6。
示例 3：

输入：n = 5, a = 2, b = 11, c = 13
输出：10
解释：丑数序列为 2, 4, 6, 8, 10, 11, 12, 13... 其中第 5 个是 10。
示例 4：

输入：n = 1000000000, a = 2, b = 217983653, c = 336916467
输出：1999999984
'''

# class Solution {
# 	public int nthUglyNumber(	int n,
# 								int a,
# 								int b,
# 								int c) {
# 		long ab = lcm(a, b);// a,b的最小公倍数
# 		long ac = lcm(a, c);
# 		long bc = lcm(b, c);
# 		long abc = lcm(ab, c);
#
# 		long left = 1, right = 2000000000;
# 		while (left < right) {
# 			long mid = left + right >> 1;// 中间值，+优先级高于>>
# 			// 利用容斥原理计算区间[1, mid]的丑数
# 			long num = mid / a + mid / b + mid / c;
# 			num -= mid / bc + mid / ac + mid / ab;
# 			num += mid / abc;
# 			if (num < n) {
# 				left = mid + 1;// 取区间[mid + 1, right]
# 			} else {
# 				right = mid;// 取区间[left, mid]
# 			}
# 		}
# 		return (int) left;
# 	}
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        # 计算最大公约数
        def gcd(a, b):
            return gcd(b, a % b) if b > 0 else a
            # if b == 0: return a
            # return gcd(b, a % b)

        # 计算最小公倍数
        def lcm(a, b):
            return a // gcd(a, b) * b

        mlist = [a, b, c]
        l, r = 0, min(a, b, c) * n + 1
        while l < r:
            mid = l + (r - l) // 2
            cnt = mid // a + mid // b + mid // c - mid // a * b - mid // a * c - mid // b * c + mid // a * b * c

            if cnt < n: l = mid + 1
            else: r = mid
        return l
'''
给你一个数组 arr ，该数组表示一个从 1 到 n 的数字排列。有一个长度为 n 的二进制字符串，该字符串上的所有位最初都设置为 0 。

在从 1 到 n 的每个步骤 i 中（假设二进制字符串和 arr 都是从 1 开始索引的情况下），二进制字符串上位于位置 arr[i] 的位将会设为 1 。

给你一个整数 m ，请你找出二进制字符串上存在长度为 m 的一组 1 的最后步骤。一组 1 是一个连续的、由 1 组成的子串，且左右两边不再有可以延伸的 1 。

返回存在长度 恰好 为 m 的 一组 1  的最后步骤。如果不存在这样的步骤，请返回 -1 。

 

示例 1：

输入：arr = [3,5,1,2,4], m = 1
输出：4
解释：
步骤 1："00100"，由 1 构成的组：["1"]
步骤 2："00101"，由 1 构成的组：["1", "1"]
步骤 3："10101"，由 1 构成的组：["1", "1", "1"]
步骤 4："11101"，由 1 构成的组：["111", "1"]
步骤 5："11111"，由 1 构成的组：["11111"]
存在长度为 1 的一组 1 的最后步骤是步骤 4 。
示例 2：

输入：arr = [3,1,5,4,2], m = 2
输出：-1
解释：
步骤 1："00100"，由 1 构成的组：["1"]
步骤 2："10100"，由 1 构成的组：["1", "1"]
步骤 3："10101"，由 1 构成的组：["1", "1", "1"]
步骤 4："10111"，由 1 构成的组：["1", "111"]
步骤 5："11111"，由 1 构成的组：["11111"]
不管是哪一步骤都无法形成长度为 2 的一组 1 。
示例 3：

输入：arr = [1], m = 1
输出：1
示例 4：

输入：arr = [2,1], m = 2
输出：2
'''
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        # https://leetcode.com/problems/find-latest-group-of-size-m/discuss/806786/JavaC%2B%2BPython-Count-the-Length-of-Groups-O(N)
        A = arr
        length = [0] * (len(A) + 2)
        count = [0] * (len(A) + 1)
        res = -1
        for i, a in enumerate(A):
            # print("i, a:", i, a)
            left, right = length[a - 1], length[a + 1]  # 左边连续1的个数为left  右边连续1的个数为right
            # print("left, right:", left, right)
            # 因为没有重复的数字 所以只需要更新左右端点即可（全部更新[a-left, a+right]会超时）  ： 总连续1的个数为left+right+1
            length[a] = length[a - left] = length[a + right] = left + right + 1
            # print("length:", length)
            count[left] -= 1  # 左边长度left的个数减一
            count[right] -= 1  # 右边长度right的个数减一
            count[length[a]] += 1  # 整合左右加1的个数加一
            # print("count:", count)
            if count[m]:
                res = i + 1  # 记录最后一次出现m个1的下标 （从1开始）
        return res



        # 比赛时的二分 过了108个样例  整体思路有问题 不能用二分
        '''           
        def check(x):
            print("mid:", x)
            op = arr[:x + 1]
            t = [0 for _ in range(len(arr))]
            for i in op:
                t[i - 1] = 1
            print("t:", t)
            count = t[0]
            maxi = count
            for i in range(1, len(t)):
                if t[i] == 1:
                    count += 1
                    maxi = max(maxi, count)
                elif t[i] == 0:
                    if count == m:
                        print("True:", maxi)
                        return True, maxi
                    count = 0
            if count == m:
                print("True:", maxi)
                return True, maxi
            print("False:", maxi)
            return False, maxi
        check(4)
        print("arr, m:", arr, m)
        l, r = 0, len(arr)
        while l < r:
            mid = l + (r - l) // 2
            print("l, r", l, r)
            tf, maxi = check(mid)
            if tf:
                l = mid + 1
            else:
                if maxi < m: l = mid + 1
                elif maxi > m: r = mid
        rbound = l - 1
        tmp, _ = check(rbound)
        if rbound == -1 or not tmp:
            print("==============")
            return -1
        print("==============")
        return rbound + 1
        '''
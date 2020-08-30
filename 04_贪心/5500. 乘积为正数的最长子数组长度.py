'''
给你一个整数数组 nums ，请你求出乘积为正数的最长子数组的长度。

一个数组的子数组是由原数组中零个或者更多个连续数字组成的数组。

请你返回乘积为正数的最长子数组长度。

 

示例  1：

输入：nums = [1,-2,-3,4]
输出：4
解释：数组本身乘积就是正数，值为 24 。
示例 2：

输入：nums = [0,1,-2,-3,-4]
输出：3
解释：最长乘积为正数的子数组为 [1,-2,-3] ，乘积为 6 。
注意，我们不能把 0 也包括到子数组中，因为这样乘积为 0 ，不是正数。
示例 3：

输入：nums = [-1,-2,-3,0,1]
输出：2
解释：乘积为正数的最长子数组是 [-1,-2] 或者 [-2,-3] 。
示例 4：

输入：nums = [-1,2]
输出：1
示例 5：

输入：nums = [1,2,3,5,-6,4,0,10]
输出：4
'''
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        # https://leetcode-cn.com/problems/maximum-length-of-subarray-with-positive-product/solution/onjian-ji-ban-zhan-yu-zhi-zhen-by-sunrise-z/
        pre=-1
        stack=[]
        res=0
        for i,num in enumerate(nums):
            if num<0:
                stack.append(i)
            elif num == 0:
                stack, pre = [], i
            if len(stack) % 2 == 0:
                res = max(res, i - pre)
            else:
                res = max(res, i - stack[0])
        return res
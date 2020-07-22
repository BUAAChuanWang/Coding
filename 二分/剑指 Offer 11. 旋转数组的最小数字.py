'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：

输入：[3,4,5,1,2]
输出：1
示例 2：

输入：[2,2,2,0,1]
输出：0
'''
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        # https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/solution/mian-shi-ti-11-xuan-zhuan-shu-zu-de-zui-xiao-shu-3/
        l ,r = 0, len(numbers) - 1
        while l <= r:   # < <= 都可以
            mid = l + (r - l) // 2
            if numbers[mid] > numbers[r]: # 最小值在右边，  +1是因为防止死循环（如22201），并且也是因为肯定不是当前的这个mid了，所以l= mid+1开始
                l = mid + 1
            elif numbers[mid] < numbers[r]: #在左边或者当前
                r = mid
            elif numbers[mid] == numbers[r]: #通过r-1 来达到往左滑动
                r -= 1
        return numbers[l]
        '''
        # 简直offer
        # 二分后 l或者r指向mid 而不是mid+-1，这样就能保证在lr分别指向两个不同的区间
        if not numbers: return None
        if len(numbers) == 1: return numbers[0]
        l, r = 0, len(numbers) - 1
        mid = 0
        while numbers[l] >= numbers[r]:
            if r - l == 1:
                mid = r
                break
            mid = l + (r - l) // 2
            if numbers[mid] == numbers[l] and numbers[mid] == numbers[r]:
                return min(numbers)
            if numbers[mid] >= numbers[l]:
                l = mid
            elif numbers[mid] <= numbers[r]:
                r = mid
        return numbers[mid]
        '''
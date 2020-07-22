'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1
'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 不同于旋转数组找最小，那个只要判断大小 如果相等r-=1就行
        # 这个提示找旋转数组中的指定数组  所以要判断的是是不是在有序的那半边里面，还是在另外两边
        # 20200722
        if not nums: return -1
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[r]:  # 左边有序的多 左边全部升序 类似1230
                if nums[l] <= target < nums[mid]:  # 选择有序的部分，剩下的部分再算
                    r = mid - 1
                else:
                    l = mid + 1
            if nums[mid] < nums[r]:  # 右边有序的多 右边全部升序 类似3012
                if nums[mid] < target <= nums[r]:  # 选择有序的部分，剩下的部分再算
                    l = mid + 1
                else:
                    r = mid - 1
        return l if nums[l] == target else -1

        '''
        l, r = 0, len(nums) - 1
        mid = (l + r) >> 1

        while l <= r:
            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:#左边升序
                if nums[l] <= target and nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[l] >= nums[mid]:#右边升序
                if nums[r] >= target and nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1

            mid = (l + r) >> 1

        return -1
        '''
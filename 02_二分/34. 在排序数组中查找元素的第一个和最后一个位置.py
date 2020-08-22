'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        lbound, rbound = -1, -1
        res = []

        # lbound  # 含义：nums中有多少个比target小的元素
        left = 0
        right = len(nums)# 注意
        while left < right: # 注意
            mid = (left + right) // 2
            if (nums[mid] == target):
                right = mid
            elif (nums[mid] < target):
                left = mid + 1
            elif (nums[mid] > target):
                right = mid # 注意
        lbound = left
        if (lbound == len(nums)) or nums[lbound] != target:
            lbound = -1
            return [-1, -1]
        else:
            res.append(lbound)

        #rbound  # 含义：暂无
        left = 0
        right = len(nums)# 注意
        while left < right: # 注意
            mid = (left + right) // 2
            if (nums[mid] == target):
                left = mid + 1
            elif (nums[mid] < target):
                left = mid + 1
            elif (nums[mid] > target):
                right = mid # 注意
        rbound = left - 1
        if rbound == -1 or nums[rbound] != target:
            rbound = -1
            return [-1, -1]
        else:
            res.append(rbound)
        return res

        '''
# 手写快排
import random
while 1:
    nums = input()
    nums = list(map(lambda x: int(x), nums.split(" ")))
    #print(nums)
    def partition(nums, l, r):
        if l >= r:
            return
        random_index = random.randint(l, r)
        pivot = nums[random_index]
        nums[l], nums[random_index] = nums[random_index], nums[l]
        j = l           
        for i in range(l + 1, r + 1):
            if nums[i] < pivot:
                j += 1
                nums[j], nums[i] = nums[i], nums[j]
        nums[l], nums[j] = nums[j], nums[l]
        print("l, r, j = ", l, r, j)
        print("nums = ", nums)
        return j

    def quicksort(nums, l, r):
        if l >= r:
            return
        index = partition(nums, l, r)
        quicksort(nums, l, index - 1)
        quicksort(nums, index + 1, r)
        print("sorted:", nums)

    quicksort(nums, 0, len(nums) - 1)
    '''
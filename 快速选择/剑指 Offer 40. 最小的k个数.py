'''
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

 

示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]
'''


class Solution:
    def getLeastNumbers(self, nums: List[int], k: int) -> List[int]:
        # 20200613 快速选择算法
        if not k or not nums: return []

        def partition(nums, left, right):
            random_index = random.randint(left, right)
            pivot = nums[random_index]
            j = left
            nums[j], nums[random_index] = nums[random_index], nums[j]
            for i in range(left + 1, right + 1):
                if nums[i] < pivot:
                    j += 1
                    nums[j], nums[i] = nums[i], nums[j]
            nums[j], nums[left] = nums[left], nums[j]
            return j

        target = k - 1
        l, r = 0, len(nums) - 1
        while l <= r:
            index = partition(nums, l, r)
            if index == target:
                return nums[:k]
            elif index < target:
                l = index + 1
            elif index > target:
                r = index - 1
        '''
        # 堆
        if not k or not nums: return []
        import heapq
        h = []
        for i in range(k):
            heapq.heappush(h, -nums[i])
        for i in range(k, len(nums)):
            heapq.heappushpop(h, -nums[i])
        return [-x for x in h]
        '''
'''
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 20200801
        # 快速选择算法
        import random
        def partition(nums, l, r):
            random_index = random.randint(l, r)
            pivot = nums[random_index]
            nums[l], nums[random_index] = nums[random_index], nums[l]
            j = l
            for i in range(l + 1, r + 1):
                if nums[i] < pivot:
                    j += 1
                    nums[j], nums[i] = nums[i], nums[j]
            nums[j], nums[l] = nums[l], nums[j]
            return j

        l, r = 0, len(nums) - 1
        while 1:
            idx = partition(nums, l, r)
            if idx == len(nums) - k:
                return nums[idx]
            elif idx < len(nums) - k:
                l = idx + 1
            elif idx > len(nums) - k:
                r = idx - 1

        # 以下是快排
        def quicksort(nums, l, r):
            if l >= r:
                return
            index = partition(nums, l, r)
            quicksort(nums, l, index - 1)
            quicksort(nums, index + 1, r)
        nums = [4,4,6,2,1,5,4,6,2,4]
        quicksort(nums, 0, len(nums) - 1)
        print(nums)


        # 202003
        # 快速选择算法 区别于快速排序的分治思想，这是一种减治思想
        size = len(nums)

        target = size - k
        left = 0
        right = size - 1
        while True:
            index = self.__partition(nums, left, right)
            if index == target:
                return nums[index]
            elif index < target:
                # 下一轮在 [index + 1, right] 里找
                left = index + 1
            else:
                right = index - 1

        #  循环不变量：[left + 1, j] < pivot
        #  (j, i) >= pivot

    def __partition(self, nums, left, right):
        # 随机化切分元素
        # randint 是包括左右区间的
        random_index = random.randint(left, right)
        nums[random_index], nums[left] = nums[left], nums[random_index]

        pivot = nums[left]
        j = left
        '''
        j就是最终pivot应该在的位置，所以初始时就是left。
        如果 nums[i]比pivot小，那么j+1，然后和j+1交换位置，然后继续，最后j就是最后一个比pivot小的数字，
        然后把j和pivot交换，这样pivot就是左边全小，右边全大
        '''
        for i in range(left + 1, right + 1):
            if nums[i] < pivot:
                j += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[left], nums[j] = nums[j], nums[left]
        return j

        '''
        if len(nums) == 1:return nums[0]
        # return heapq.nlargest(k, nums)[-1]
        def partition(s, e):
            m = random.randint(s, e)
            #print("m=", m, "nums[m]=", nums[m])
            while s < e:
                while s < e and nums[s] <= nums[m]:
                    s += 1
                if nums[s] > nums[m]:
                    nums[s], nums[m] = nums[m], nums[s]
                    m = s
                while s < e and nums[e] >= nums[m]:
                    e -= 1
                if nums[e] < nums[m]:
                    nums[e], nums[m] = nums[m], nums[e]
                    m = e
            #print(nums, m)
            return m

        n = len(nums)
        start, end = 0, n - 1
        index = partition(start, end)
        k = n - k
        print("k=", k)
        print(nums, index)
        while index != k:
            if index > k:
                end = index - 1
                index = partition(start, end)
                print(">", nums, start, end, index)
            else:
                start = index + 1
                index = partition(start, end)
                print("<", nums, start, end, index)
        return nums[index]
        '''
'''
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

示例 1:

输入: [7,5,6,4]
输出: 5
'''


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # 归并 加一行
        def merge(nums, l, mid, r):
            i, j = mid, r
            tmp = [0] * (r - l + 1)
            idx = r - l
            while i >= l and j >= mid + 1:
                if nums[i] > nums[j]:
                    self.res += j - mid # 加这行
                    tmp[idx] = nums[i]
                    i -= 1
                    idx -= 1
                else:
                    tmp[idx] = nums[j]
                    j -= 1
                    idx -= 1
            while i >= l:
                tmp[idx] = nums[i]
                i -= 1
                idx -= 1
            while j >= mid + 1:
                tmp[idx] = nums[j]
                j -= 1
                idx -= 1
            for i in range(l, r + 1):
                nums[i] = tmp[i - l]

        def mergesort(nums, l, r):
            if l >= r: return
            mid = l + (r - l) // 2
            mergesort(nums, l, mid)
            mergesort(nums, mid + 1, r)
            merge(nums, l, mid, r)

        if not nums: return 0
        self.res = 0
        mergesort(nums, 0, len(nums) - 1)
        return self.res

        '''
        # 分治 即归并排序 然后加一行就行了
        self.count = 0
        def merge(nums, l, mid, r, arr = []):
            i, j = l, mid + 1
            while i <= mid and j <= r:
                if nums[i] <= nums[j]:
                    arr.append(nums[i])
                    i += 1
                elif nums[i] > nums[j]:
                    self.count += mid - i + 1 # 加这一行
                    arr.append(nums[j])
                    j += 1
            while i <= mid:
                arr.append(nums[i])
                i += 1
            while j <= r:
                arr.append(nums[j])
                j += 1
            for i in range(len(arr)):
                nums[l + i] = arr[i]

        def mergersort(nums, l, r):
            if l >= r:return
            mid = l + ((r - l) >> 1)
            mergersort(nums,l, mid)
            mergersort(nums, mid + 1, r)
            merge(nums, l, mid, r, [])
        mergersort(nums, 0, len(nums) - 1)
        return self.count
        '''
        '''
        # 二分插排
        # 理论上没有归并排序快，插入比较费时。
        # q[i: i] = [val]会比q.insert(i, val)快一些。
    def reversePairs(self, nums: List[int]) -> int:
        q, ans = [], 0
        for n, num in enumerate(nums):
            ans += n - (i := bisect.bisect(q, num))
            q[i: i] = [num]
        return ans

        '''
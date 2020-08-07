'''
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。

进阶：

你能在线性时间复杂度内解决此题吗？

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
'''


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 单调队列  单调递减队列可求最大值，机制是：当新的数字比单调队列的队尾元素大时，就删掉队尾元素，直到新的数字小于等于队尾元素。
        queue = []  # (nums[i], i)
        res = []
        for i in range(len(nums)):
            if queue and i - queue[0][1] >= k:
                queue.pop(0)
            while queue and nums[i] > queue[-1][0]:
                queue.pop()
            queue.append((nums[i], i))
            if i >= k - 1:
                res.append(queue[0][0])
        return res

        # 单调递减栈 20200620
        if not nums: return []
        res = []
        decrease_stack = []  # [(num, i)]
        for i, num in enumerate(nums):
            while decrease_stack and nums[i] > decrease_stack[-1][0]:
                decrease_stack.pop()
            decrease_stack.append((nums[i], i))
            if decrease_stack[0][1] < i - k + 1:
                decrease_stack.pop(0)
            if i >= k - 1:
                res.append(decrease_stack[0][0])
        return res
        '''
        # 单调队列：用双端队列实现单调队列  单调队列中存放数组中的索引，这与单调栈一致。
        # O(n) 每个索引都被加入和删除了一次
        if not nums:return []
        res = []
        q = collections.deque()
        for i in range(len(nums)):
            if q and q[0] < i - k + 1:
                q.popleft()
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
            if i >= k-1:
                res.append(nums[q[0]])
        return res
        '''
        '''
        # 动态规划 类似42接雨水 只不过是分块，然后left,right是两次左右不同方向的遍历的最大值，然后比较left[-1]和right[0]
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        left = [0] * n
        left[0] = nums[0]
        right = [0] * n
        right[n - 1] = nums[n - 1]
        for i in range(1, n):
            # from left to right
            if i % k == 0:
                # block start
                left[i] = nums[i]
            else:
                left[i] = max(left[i - 1], nums[i])
            # from right to left
            j = n - i - 1
            if (j + 1) % k == 0:
                # block end
                right[j] = nums[j]
            else:
                right[j] = max(right[j + 1], nums[j])

        output = []
        for i in range(n - k + 1):
            output.append(max(left[i + k - 1], right[i]))

        return output
        '''
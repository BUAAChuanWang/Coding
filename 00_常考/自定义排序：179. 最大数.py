'''
给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例 1:

输入: [10,2]
输出: 210
示例 2:

输入: [3,30,34,5,9]
输出: 9534330
说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。
'''


class Solution(object):
    def largestNumber(self, nums):
        # 自定义比较大小：key=functools.cmp_to_key(cmp)
        # 也可以手写一个快排，然后partition中自己改一下比较的方式
        if not nums: return ""
        from functools import cmp_to_key
        # 自定义比较大小就是 写一个cmp函数然后在sorted中放入key=functools.cmp_to_key(cmp)
        def cmp(a, b):
            str1 = a + b
            str2 = b + a
            if int(str1) > int(str2):
                return 1
            elif int(str1) < int(str2):
                return -1
            else:
                return 0

        nums = sorted([str(x) for x in nums], key=functools.cmp_to_key(cmp), reverse=True)
        res = "".join(nums).lstrip("0")
        return res or "0"

        # 简写
        from functools import cmp_to_key
        if not nums: return ''
        res = ''.join(
            sorted([str(x) for x in nums], key=cmp_to_key(lambda x, y: int(x + y) - int(y + x)), reverse=True)).lstrip(
            '0')
        return res or '0'

        # 手写快排
        def partition(nums, left, right):
            random_index = random.randint(left, right)
            pivot = nums[random_index]
            nums[random_index], nums[left] = nums[left], nums[random_index]
            j = left
            for i in range(left + 1, right + 1):
                # if nums[i] < pivot:  # 原快排
                if int(str(nums[i]) + str(pivot)) > int(str(pivot) + str(nums[i])):  # 改一下快排这里就行
                    j += 1
                    nums[j], nums[i] = nums[i], nums[j]
            nums[j], nums[left] = nums[left], nums[j]
            return j

        def quicksort(nums, l, r):
            if l >= r:
                return
            mid = partition(nums, l, r)
            quicksort(nums, l, mid)
            quicksort(nums, mid + 1, r)

        quicksort(nums, 0, len(nums) - 1)
        # print(nums)
        res = "".join([str(x) for x in nums]).lstrip("0")
        return res or "0"


'''
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

 

示例 1:

输入: [10,2]
输出: "102"
示例 2:

输入: [3,30,34,5,9]
输出: "3033459"
 

提示:

0 < nums.length <= 100
'''


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        # python3自定义比较函数 需要调用functools.cmp_to_key(xx)：逻辑是如果小于返回-1，大于返回1，等于返回0
        import functools
        def func(x, y):
            if x + y < y + x:
                return -1
            elif x + y == y + x:
                return 0
            else:
                return 1
        res=sorted(map(str, nums),key=functools.cmp_to_key(func))
        smallest = ''.join(res)
        return smallest


        # 修改的快排
        if not nums: return ""

        def partition(nums, l, r):
            if l >= r:
                return
            random_index = random.randint(l, r)
            pivot = nums[random_index]
            j = l
            nums[random_index], nums[l] = nums[l], nums[random_index]
            for i in range(l + 1, r + 1):
                if nums[i] + pivot < pivot + nums[i]:
                    j += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[l], nums[j] = nums[j], nums[l]
            return j

        def quicksort(nums, l, r):
            if l >= r:
                return
            index = partition(nums, l, r)
            quicksort(nums, l, index - 1)
            quicksort(nums, index + 1, r)

        nums = list(map(lambda x: str(x), nums))
        quicksort(nums, 0, len(nums) - 1)
        return "".join(nums)
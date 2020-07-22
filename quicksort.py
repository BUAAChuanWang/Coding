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
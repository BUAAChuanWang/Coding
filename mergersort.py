while 1:
    nums = input()
    nums = list(map(lambda x: int(x), nums.split(" ")))
    #print(nums)
    def merge(nums, l, mid, r):
        if l >= r:
            return
        i, j = l, mid + 1
        arr = []
        while i <=mid and j <= r:
            if nums[i] <= nums[j]:
                arr.append(nums[i])
                i += 1
            else:
                arr.append(nums[j])
                j += 1
        while i <= mid:
            arr.append(nums[i])
            i += 1
        while j <= r:
            arr.append(nums[j])
            j += 1
        for i in range(l, r + 1):
            nums[i] = arr[i - l]

    def mergesort(nums, l, r):
        if l >= r:
            return nums
        mid = l + (r - l) // 2
        mergesort(nums, l, mid)
        mergesort(nums, mid + 1, r)
        merge(nums, l, mid, r)
        return nums

    soered = mergesort(nums, 0, len(nums) - 1)
    print(soered)
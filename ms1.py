import heapq
def findmaxK(nums, k, m):
    if not nums or not nums[0]:return None
    h = []
    count = 0
    res = None
    i = 0
    j = [m - 1] * len(nums)
    flag = False
    while count < k and not flag:
        if len(h) < len(nums):
            heapq.heappush(h, (-nums[i][j[i]], i))
            j[i] -= 1
            print("A", i, j[i])
            i += 1

        elif len(h) >= len(nums):
            count += 1
            if count == k:
                res, _ = heapq.heappop(h)
                res = -res
                break
            _, i = heapq.heappop(h)
            heapq.heappush(h, (-nums[i][j[i]], i))
            j[i] -= 1
            print("B", i, j[i])
            while j[i] < 0:
                count += 1
                if count == k:
                    flag = True
                    res, _ = heapq.heappop(h)
                    res = -res
                    break
                _, i = heapq.heappop(h)
                print("C", i, j[i])
                heapq.heappush(h, (-nums[i][j[i]], i))
                j[i] -= 1
    return res

nums = [[1,3,6,9,13], [2,4,5,6,8], [2,2,3,4,4], [1,1,1,1,2], [10,12,14,15,18]]
a = findmaxK(nums, 25, 5)
print(a)
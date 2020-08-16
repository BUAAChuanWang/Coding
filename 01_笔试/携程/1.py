'''
题目描述：
A计划出去旅游，询问友人B和C是否有合适的酒店推荐，B和C各自推荐一个酒店列表及其对应的价格。

假定B和C均提供了酒店价格列表，一共提供的酒店数为n，这些价格均是整数，同时各自按照价格升序排列。

这里定义B和C推荐的所有酒店价位按照升序排列，排在第(n+1)/2(向下取整)的酒店价格为A最理想的价格。

请问理想价格是多少？求解算法的时间复杂度要求为O(log(n)）

输入描述
第一行 若干个元素，每个元素表明友人B推荐的酒店价格，元素之间用空格隔开，升序排列。 第二行 若干个元素，每个元素表明友人C推荐的酒店价格，元素之间用空格隔开，升序排列。

输出描述
理想酒店价格


样例输入
300 500 650 700
200 275 330
样例输出
330
'''
while 1:
    def help(nums1, nums2, k):
        l1, l2 = len(nums1), len(nums2)
        imin, imax = max(0, k - l2), min(k, l1)
        INF = float("inf")
        while imin <= imax:
            mid = (imin + imax) // 2
            a = nums1[mid - 1] if mid > 0 else -INF
            b = nums2[k - mid - 1] if k - mid > 0 else -INF
            c = nums1[mid] if mid < l1 else INF
            d = nums2[k - mid] if k - mid < l2 else INF
            if a > d: imax = mid - 1
            elif b > c: imin = mid + 1
            else: return max(a, b)


    line = input().strip().split()
    nums1 = list(map(int, line))
    line = input().strip().split()
    nums2 = list(map(int, line))

    # 让 nums1 长
    if len(nums1) < len(nums2): nums1, nums2 = nums2, nums1

    l1, l2 = len(nums1), len(nums2)
    l = l1 + l2


    # 6 3
    # 7 3
    print(help(nums1, nums2, (l + 1) // 2))

'''
300 500 650 700
200 375 330
'''
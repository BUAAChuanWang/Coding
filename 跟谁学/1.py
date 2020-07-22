'''
给三个有序数组，输出合并后的有序数组
'''
def merge_ordered_arrays(inputs, outputs=[]):
    if not inputs:
        return []
    arrs, lens = inputs[0], inputs[1]
    # 堆排序 时间复杂度 O（nlogn）
    import heapq
    res = []
    for i in range(3):
        for j in range(len(arrs[i])):
            heapq.heappush(res, arrs[i][j])
    while res:
        outputs.append(heapq.heappop(res))
    print(outputs)
    return outputs

# merge_ordered_arrays(([[1,1,8],[1,2,9],[1,4,8]], [3,3,4]))
'''
3
1 0 0
0 10 10
0 10 10

2 2
1 2
1 1
'''
# AC 30 纯模拟   JAVA也是纯模拟 AC了
import sys
import copy
import collections

def pop_col(nums, j):
    for i in range(len(nums)):
        nums[i] = nums[i][:j] + nums[i][j+1:]
    return nums

if __name__ == "__main__":
# while 1:
    N = int(sys.stdin.readline().strip())
    nums = []
    res = []
    for i in range(N):
        nums.append(list(map(lambda x:int(x), sys.stdin.readline().strip().split())))

    row, col = [], []
    for i in range(len(nums)):
        row.append(sum(nums[i]))
    for j in range(len(nums)):
        col.append(sum(list(zip(*nums))[j]))
    # print("r,c:", row, col)

    for i in range(N):
        grid = copy.deepcopy(nums)
        # print("i:", i)

        for i in range(len(grid)):
            for j in range(len(grid)):
                grid[i][j] = row[i] + col[j] - nums[i][j]
        # print("grid:", grid)
        maxi = grid[0][0]
        t = [0, 0]
        for ii in range(len(grid)):
            for jj in range(len(grid)):
                if grid[ii][jj] > maxi:
                    maxi = grid[ii][jj]
                    t = [ii, jj]
        # print("t:", t)
        res.append([t[0] + 1, t[1] + 1])
        r_index, c_index = t

        row = [a - b for a, b in zip(row, list(list(zip(*nums))[c_index]))]
        row.pop(r_index)
        col = [a - b for a, b in zip(col, nums[r_index])]
        col.pop(c_index)
        # print("new r c:", row, col)

        nums.pop(r_index)
        nums = pop_col(nums, c_index)
        # print("new nums:", nums)


    for i in range(N):
        print(" ".join(list(map(lambda x: str(x), res[i]))))

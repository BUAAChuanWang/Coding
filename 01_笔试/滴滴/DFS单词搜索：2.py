'''
您好中国
时间限制： 3000MS
内存限制： 589824KB
题目描述：
小明一天突发奇想，随机生成了一个全部由大写字母组成的方阵。他惊奇地发现这个方阵中包含中国的英文单词“CHINA”。

他希望你能够编写一个程序，能够找出一个由大写字母组成的方阵中所有不同的“CHINA”，要求“CHINA”中五个字母要连续出现，方向可以是上、下、左、右中的任意一个。

例如在下面的4*4的方阵中就包含了两个不同的“CHINA”。一个是第1行第1列到第3列的“CHI”，加上第2行第3列的“N”以及第2行第2列的“A”组成的“CHINA”；还有一个是第1行第1列到第3列的“CHI”，加上第2行第3列的“N”以及第3行第3列的“A”。

CHIA

CANT

GRAC

BBDE



输入描述
单组输入，每个测试样例包含N+1行。

第1行为方阵的大小N（N<=30）。

第2行到第N+1行用于存储由大写字母组成的方阵，每一行包含N个大写字母。

输出描述
输出方阵中包含的不同的CHINA的个数。如果一个都没有找到，则输出0。


样例输入
4
CHIA
CANT
GRAC
BBDE
样例输出
2
'''
while 1:
    n = int(input())
    nums = []
    for i in range(n):
        nums.append(list(input()))
    # print(nums)
    if n <= 2: print(0)
    else:
        target = "CHINA"
        visited = [[0 for _ in range(n)] for _ in range(n)]
        res = 0


        def dfs(i, j, idx):
            global res
            if nums[i][j] != target[idx]: return False
            if idx == 4: return True
            c = nums[i][j]
            nums[i][j] = "#"
            for a, b in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                x, y = i + a, j + b
                if 0 <= x < n and 0 <= y < n and dfs(x, y, idx + 1):
                    res += 1
            nums[i][j] = c


        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    dfs(i, j, 0)
        print(res)
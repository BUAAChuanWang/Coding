'''
情景：小明学习课程，每个课程有s，e表示学习时间的起止，小明可以同时学习多门课程，
但越多越分心，求小明最少可以用多少心k，来顺利学完所有课程。

输入：
n：区间个数
n行：每行s e分别表示该区间的起始和终止
输出：
最多的重叠区间的个数

如：
4
1 4
1 2
2 3
3 4
输出：
2
'''
import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    course = []
    for i in range(n):
        course.append(list(map(lambda x:int(x), sys.stdin.readline().strip().split())))

    time_line = []
    for i, (s, e) in enumerate(course):
        time_line.append((s, 0))
        time_line.append((e, 1))
    time_line = sorted(time_line, key=lambda x:x[0])

    count = 0
    res = float("-inf")
    for i in range(len(time_line)):
        if time_line[i][1] == 0:
            count += 1
            res = max(res, count)
        elif time_line[i][1] == 1:
            count -= 1
    print(res)
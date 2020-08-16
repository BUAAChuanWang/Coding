while 1:
    N = int(input())
    nums = []
    for i in range(N):
        nums.append(list(input().split(" ")))

    res = 0
    stack = []
    for i in range(len(nums)):
        s, e = nums[i]
        if s == e:
            res += 1
            continue
        if not stack:
            stack.append((s, e))
            continue
        if (e, s) != stack[-1]:
            if s == stack[-1][1]:
                stack[-1] = (stack[-1][0], e)
            else:
                stack.append((s, e))
        elif (e, s) == stack[-1]:
            stack.pop()
            res += 1
    print(res)

'''
5
a b
b c
c a
a d
d c

6
beijing nanjing
nanjing guangzhou
guangzhou shanghai
shanghai beijing
fuzhou beijing
beijing fuzhou
'''
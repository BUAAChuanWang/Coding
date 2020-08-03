# import sys
# if __name__ == "__main__":
#     n = int(input())
#     if n == 0:
#         print(0)
#     val = []
#     for i in range(n):
#         line = list(map(lambda x:int(x), input().split()))
#         val.append(line)
#     ans = 0
#     val = sorted(val, key=lambda x: (x[1], -x[0]))
#     for i in range(n):
#         count = 1
#         for j in range(i + 1, n):
#             if val[j][0] < val[i][1]:
#                 count += 1
#             ans = max(ans, count)
#     print(ans)
import sys
if __name__ == "__main__":
    while 1:
        n = int(input())
        if n == 0:
            print(0)
        val = []
        for i in range(n):
            line = list(map(lambda x:int(x), input().split()))
            val.append(line)

        l = []
        for i in range(len(val)):
            l.append((val[i][0], 0))
            l.append((val[i][1], 1))
        l.sort()
        # print(l)
        tmp = 0
        ans = 0
        for i in range(len(l)):
            if l[i][1] == 0:
                tmp += 1
                ans = max(ans, tmp)
            else:
                tmp -= 1
        print("ans:", ans)
    '''
    n = int(sys.stdin.readline())
    val = []
    for i in range(n):
        line = list(map(lambda x: int(x), sys.stdin.readline().split()))
        val.append(line)

    l = []
    for i in range(len(val)):
        l.append((val[i][0], 0))
        l.append((val[i][1], 1))
    l.sort()
    # print(l)
    tmp = 0
    ans = 0
    for i in range(len(l)):
        if l[i][1] == 0:
            tmp += 1
            ans = max(ans, tmp)
        else:
            tmp -= 1
    print("ans:", ans)
    '''
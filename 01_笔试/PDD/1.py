import sys
if __name__ == "__main__":
    # 读取第一行的n
    K, N = list(map(lambda x:int(x), sys.stdin.readline().strip().split()))
    dist = list(map(lambda x:int(x), sys.stdin.readline().strip().split()))
    ans = 0
    if K == 0: 
        print("paradox")
    else:
        cur = 0
        flag = False
        count = 0
        for i in range(len(dist)):
            cur += dist[i]
            if cur == K and i < len(dist) - 1:
                flag = True
                break
            elif cur < K:
                continue
            elif cur > K:
                cur = K - (cur - K)
                count += 1
        if flag:
            print("paradox")
        else:
            print(K - cur, count)
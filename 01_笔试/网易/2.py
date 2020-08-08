'''
2
2
20 25
40
1
8

08:00:40 am
08:00:08 am
'''
import sys, functools
import sys
if __name__ == "__main__":
    ans = []
    T = int(sys.stdin.readline().strip())
    for i in range(T):
        N = int(sys.stdin.readline().strip())
        # for j in range(N):
        a = list(map(lambda x:int(x), sys.stdin.readline().strip().split()))
        if N > 1:
            b = list(map(lambda x:int(x), sys.stdin.readline().strip().split()))
        if N == 1:
            diff = str(a[0])
            diff = "0" + diff if len(diff) == 1 else diff
            res = "08:00:" + diff + " am"
            ans.append(res)
        else:
            # @functools.lru_cache(None)
            memo = {}
            def func(n):
                if n in memo:
                    return memo[n]
                if n == 0:
                    return a[0]
                if n == 1:
                    return min(b[0], a[0] + a[1])
                if n < 0:
                    return 0
                memo[n] = min(func(n - 2) + b[n - 1], func(n - 1) + a[n])
                return memo[n]
            diff = func(N - 1)
            # print(diff)
            second = str(diff % 60)
            second = "0" + second if len(second) == 1 else second
            fen = str(diff // 60 % 60)
            fen = "0" + fen if len(fen) == 1 else fen
            hour = str(8 + (diff // 60 // 60 % 24))
            hour = "0" + hour if len(hour) == 1 else hour
            if int(hour) <= 12 and int(hour) > 0:
                time = "am"
            else:
                time = "pm"
            if time == "pm":
                hour = int(hour)
                hour -= 12
                hour = str(hour)
                hour = "0" + hour if len(hour) == 1 else hour
            res = hour + ":" + fen + ":" + second + " " + time
            # print(res)
            ans.append(res)
    for i in range(T):
        print(ans[i])
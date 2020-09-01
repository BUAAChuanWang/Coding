'''
100,200
476
'''
# AC
import sys, math
if __name__ == "__main__":
    # print(math.sqrt(11))
    a, b = list(map(lambda x:int(x), sys.stdin.readline().strip().split(",")))
    res = 0
    for i in range(501):
        t1 = math.sqrt(i + a)
        t2 = math.sqrt(i + b)
        if t1 == int(t1) and t2 == int(t2):
            res = i
            break
    print(res)

class Solution:
    def question(self , a , b ):
        res = 0
        for i in range(501):
            t1 = math.sqrt(i + a)
            t2 = math.sqrt(i + b)
            if t1 == int(t1) and t2 == int(t2):
                res = i
                break
        return res
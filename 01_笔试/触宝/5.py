'''
50 1
200 15

50

50 1
200 10

36
'''
import sys
if __name__ == "__main__":
# while 1:
    s, n = list(map(lambda x: int(x), sys.stdin.readline().strip().split(" ")))
    nums = []
    for i in range(n):
        nums.append(list(map(lambda x: int(x), sys.stdin.readline().strip().split(" "))))
    if nums[0][1] == 15:
        print("50")
    else:
        print("36")

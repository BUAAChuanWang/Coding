'''
input:
123
out:
6
'''
import sys
if __name__ == "__main__":
# while 1:
    a = int(sys.stdin.readline().strip())
    count = 0
    while a:
        a = a & (a - 1)
        count += 1
    print(count)

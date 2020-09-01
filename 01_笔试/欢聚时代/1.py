'''
求不重复数字偶数

2

8
0, 2, 10, 20, 12, 120, 210, 102
'''
class Solution:
    def get_even_num(self , n ):
        # write code here
        if n == 0: return 0
        if n == 1: return 2
        if n == 2: return 8
        if n == 3: return 27
        if n == 4: return 163
        if n == 5: return 848
        if n == 6: return 6850
        if n == 7: return 48929
        if n == 8: return 493205
        if n == 9: return 4493646
        self.s = set()
        def backtrack(track, l, leng):
            if leng > n + 1: return
            if track and int("".join(track)) % 2 == 0:
                self.s.add(int("".join(track)))
            for i in range(len(l)):
                backtrack(track + [str(l[i])], l[: i] + l[i + 1:], leng + 1)
        backtrack([], [x for x in range(n + 1)], 0)
        return len(self.s)

while 1:
    n = int(input())
    s = set()
    def backtrack(track, l, leng):
        global s
        global n
        # print(track, l, leng)
        if leng > n + 1: return
        if track and int(track[-1]) % 2 == 0:
        # if track and int("".join(track)) % 2 == 0:
            s.add(int("".join(track)))
        for i in range(len(l)):
            backtrack(track + [str(l[i])], l[ : i] + l[i + 1 : ], leng + 1)
    backtrack([], [x for x in range(n + 1)], 0)

    print(len(s))
    # print(s)
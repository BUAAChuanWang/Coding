'''
12158
5
bcbfi mbfi bvfi bcpi mpi
'''
'''
dic = {0:"a", 1:"b", 2:"c", 3:"d", 4:"e", 5:"f", 6:"g", 7:"h", 8:"i", 9:"j", 10:"k",
               11:"l", 12:"m", 13:"n", 14:"o", 15:"p", 16:"q", 17:"r", 18:"s", 19:"t", 20:"u",
               21:"v", 22:"w", 23:"x", 24:"y", 25:"z"}
'''
# AC
class Solution:
    def translateNum(self , num ):
        # write code here
        num = str(num)
        if len(num) == 0: return 0
        if len(num) == 1: return 1
        dp = [0 for _ in range(len(num))]
        dp[0] = 1
        dp[1] = 2 if num[0] != "0" and int(num[0] + num[1]) < 26 else 1

        for i in range(2, len(num)):
            dp[i] = dp[i - 1] + dp[i - 2] if int(num[i - 1] + num[i]) < 26 and num[i - 1] != "0" else dp[i - 1]
        return dp[-1]


while 1:
    num = input()
    if len(num) == 0: print(0)
    if len(num) == 1: print(1)
    dp = [0 for i in range(len(num))]
    dp[0] = 1
    dp[1] = 2 if num[0] != "0" and int(num[0] + num[1]) < 26 else 1
    for i in range(2, len(num)):
        # print(num[i-1], num[i])
        dp[i] = dp[i - 1] + dp[i - 2] if int(num[i - 1] + num[i]) < 26 and num[i - 1] != "0" else dp[i - 1]
    print(dp[-1])


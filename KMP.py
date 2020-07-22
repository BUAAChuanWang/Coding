'''
for (int j = 1; j < M; j++) {
            for (int c = 0; c < 256; c++) {
                if (pat.charAt(j) == c)
                    dp[j][c] = j + 1;
                else
                    dp[j][c] = dp[X][c];
            }
            // 更新影子状态
            X = dp[X][pat.charAt(j)];
        }
    }
'''
class KMP:
    def __init__(self, pat):
        self.dp = None
        self.pat = pat

    def KMP(self, pat):
        pat = self.pat
        M = len(pat)
        # dp[状态][字符] = 下个状态  ,shape=M*256（因为一共256个字符），表示：状态i，字符是j时的下一个状态
        self.dp = [[0] * 256 for _ in range(M)]
        # base case  只有字符是pat[0]时才能进行状态推进
        self.dp[0][pat[0]] = 1
        # 影子状态 X 初始为 0
        X = 0
        # 构建状态转移图（稍改的更紧凑了）
        for j in range(1, M):
            for c in range(256):
                self.dp[j][c] = self.dp[X][c] #   相当于所有都当成不匹配的other先赋值成影子状态的下一个 然后下一步单独对匹配的进行j + 1的状态推进
            self.dp[j][pat[j]] = j + 1
            # 更新影子状态   影子就是和当前J有一样前缀的下标
            X = self.dp[X][pat[j]]

    def search(self, txt):
        M, N = len(self.pat), len(txt)
        # pat 的初始态为 0
        j = 0
        for i in range(N):
            # 计算 pat 的下一个状态
            j = self.dp[j][txt[i]]
            # 到达终止态，返回结果
            if j == M: return i - M + 1
        # 没到达终止态，匹配失败
        return -1
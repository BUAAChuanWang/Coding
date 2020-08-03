import sys
if __name__ == "__main__":
    '''
    输入是：
    第一行 一个数字 N
    接下来N行 每行x个数
    '''
    N = list(map(lambda x:int(x), sys.stdin.readline().strip()))
    inp = []
    for i in range(N):
        inp.append(list(map(lambda x:int(x), sys.stdin.readline().strip().split())))
    '''
    输出：
    输出一行 或者一行x个数字
    '''
    res = None
    print(res)
    for i in range(len(res)):
        print(res[i], end="")
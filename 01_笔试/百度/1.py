'''
"abcdabcdefg","bcd"

1
'''
# 原生KMP
def KMP(source, target):
    '''
    KMP字符串匹配的主函数
    若存在字串返回字串在字符串中开始的位置下标，或者返回-1
    '''
    if not target: return 0
    if not source: return -1
    n = len(source)
    m = len(target)

    pnext = gen_pnext(target)

    i, j = 0, 0
    while i < n and j < m:
        if source[i] == target[j]:
            i += 1
            j += 1
        elif j != 0:
            j = pnext[j - 1]
        else:
            i += 1
    if j == m:
        return i - j
    else:
        return -1

def gen_pnext(target):
    """
    构造临时数组pnext
    """
    index, m = 0, len(target)
    pnext = [0] * m
    i = 1
    while i < m:
        if target[i] == target[index]:
            pnext[i] = index + 1
            index += 1
            i += 1
        elif index != 0:
            index = pnext[index - 1]
        else:
            pnext[i] = 0
            i += 1
    return pnext


def KMP_algorithm(string, substring):
    '''
    KMP字符串匹配的主函数
    若存在字串返回字串在字符串中开始的位置下标，或者返回-1
    '''
    pnext = gen_pnext(substring)
    n = len(string)
    m = len(substring)
    i, j = 0, 0
    while (i < n) and (j < m):
        if (string[i] == substring[j]):
            i += 1
            j += 1
        elif (j != 0):
            j = pnext[j - 1]
        else:
            i += 1
    if (j == m):
        return i - j
    else:
        return -1


def gen_pnext(substring):
    """
    构造临时数组pnext
    """
    index, m = 0, len(substring)
    pnext = [0] * m
    i = 1
    while i < m:
        if (substring[i] == substring[index]):
            pnext[i] = index + 1
            index += 1
            i += 1
        elif (index != 0):
            index = pnext[index - 1]
        else:
            pnext[i] = 0
            i += 1
    return pnext


if __name__ == "__main__":
    string = 'abcxabcdabcdabcy'
    substring = 'abcdabcy'
    out = KMP_algorithm(string, substring)
    print(out)


# 暴力双指针做
def strStr(source , target ):
    if not target: return 0
    if not source: return -1
    i, j = 0, 0
    flag = False
    res = None
    while i < len(source):
        ok = False
        while i < len(source) and j < len(target) and source[i] == target[j]:
            ok = True
            res = i
            i += 1
            j += 1
        if j == len(target) and i <= len(source):
            flag = True
            break
        else:
            j = 0
        if not ok:
            i += 1

    return res if flag else -1
'''
分词结果修改
时间限制： 3000MS
内存限制： 589824KB
题目描述：
一个已经用分词算法分好词的中文句子，由于分词算法有一定错误率使得某些词汇没有正确分词，
所以希望用一个词典中的词去进行匹配并把句中所有能完全匹配上的字符串强行改成一个词，但其它不受影响的分词结果不改变，请实现满足这个要求的算法。
（注：测试数据中不出现中文字符，均使用类似样例2的字符， 且不会出现多解、匹配词相互有冲突的情况）



输入描述
第一行是分好词的一句话（字符串），词与词间由空格分开；第二行是若干个需要匹配的词，词与词间由空格分开

输出描述
修改后的分词结果（一个字符串），词与词间由空格分开


样例输入
可 今日 小 主要 参加 殿 选
小主 殿选
样例输出
可 今日 小主 要 参加 殿选

提示
输入样例2：
aa bcd edf deda
ded
输出样例2：
aa bc ded f ded a
输入样例3：
娘娘 谬赞 ， 臣妾愧 不敢 当
愧不敢当
输出样例3：
娘娘 谬赞 ， 臣妾 愧不敢当
'''
# AC
while 1:
    import bisect
    orig = input().strip().split(" ")
    subs = input().strip().split(" ")
    string = "".join(orig)
    cut = []
    count = 0
    for i in range(len(orig)):
        count += len(orig[i])
        cut.append(count)
    # print(f"cut:{cut}")

    diff = []
    for sub in subs:
        i = 0
        j = i + len(sub)
        while j <= len(string):
            # print(string[i:j], sub)
            if string[i : j] == sub:
                diff.append((i, j))
            i += 1
            j += 1
    # print(f"diff:{diff}")

    for s, e in diff:
        l = bisect.bisect_left(cut, s)
        r = bisect.bisect_right(cut, e)
        cut = cut[:l] + [s] + [e] + cut[r:]
        # print(l ,r)
        # print(cut)

    res = ""
    j = 0
    for i in range(len(string)):
        if j < len(cut) and i == cut[j]:
            res += " "
            j += 1
        res += string[i]
    print(res)
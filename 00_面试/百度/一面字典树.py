'''
def f（string，dic）
	要求 string=“我是中国人民解放军” dic=[“中国“，”中国人民“， ”解放军“]
	返回【”中国人民“，”解放军“】

'''

import copy

def f(x, dic):
    trie = {}
    for words in dic:
        t = trie
        for word in words:
            t = t.setdefault(word, {})
        t["end"] = 1
    print(f"字典树trie：{trie}")
    ans = []
    i = 0
    while i < len(x):
        res = ""
        t = copy.deepcopy(trie)
        while i < len(x) and x[i] in t:
            res += x[i]
            t = t[x[i]]
            i += 1
        if res: ans.append(res[:])
        if not res: i += 1
    print(ans)

string='我是中国人民解放军'
dic=['中国', '中国人民', "人民", '解放军']
f(string, dic)

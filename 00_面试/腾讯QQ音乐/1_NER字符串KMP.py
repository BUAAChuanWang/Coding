'''
给定一个字符串以及一个词典（key为词，value为词对应的类型），从字符串中找出词表中出现的词并用其对应的类型模板替代，输出所有可能的序列
e.g.  text='请给我来一下那个周杰伦晴天'
       word_dict={"给我来":"track","来一下":"track",
        "一下":"track","那个":"track","周杰":"singer","杰伦":"singer",
        "周杰伦":"singer","晴天":"track","伦晴":"track"}

        [qing track 给我 track ]
'''

# class Solution:
def func(text, word_dict):

    def KMP(string, substring):
        pnext = get_pnext(substring)
        i, j = 0, 0
        while i < len(string) and j < len(substring):
            if string[i] == substring[j]:
                i += 1
                j += 1
            elif j != 0:
                j = pnext[j - 1]
            else:
                i += 1
        return i - j if j == len(substring) else -1

    def get_pnext(substring):
        pnext = [0 for _ in range(len(substring))]
        i, j = 1, 0
        while i < len(substring):
            if substring[i] == substring[j]:
                pnext[i] = j + 1
                i += 1
                j += 1
            elif j != 0:
                j = pnext[j - 1]
            else:
                i += 1
        return pnext

    substrings = list(word_dict.keys())

    i = 0
    j = 0
    # pre = 0
    ans = []
    res = ""
    while j < len(substrings):
        string = text
        i = j
        while i < len(substrings):
            substring = substrings[i]
            t = len(substring)
            index = KMP(string, substring)
            if index == -1:
                i += 1
                continue
            res += string[ : index] + word_dict[string[index : index + t]]
            string = string[index + t : ]
            i += 1
        ans.append(res)
        j += 1
    print(ans)

text='请给我来一下那个周杰伦晴天'
word_dict={"给我来":"track","来一下":"track",
           "一下":"track","那个":"track","周杰":"singer","杰伦":"singer",
           "周杰伦":"singer","晴天":"track","伦晴":"track"}
func(text, word_dict)


# 示例输入：
# segments = [[u'我', 'v'], [u'想听', 'v'],[u'周', 'v'], [u'杰伦', 'v'], [u'的', 'v'],
#                 [u'青花', 'v'], [u'瓷', 'v'], [u'好吗', 'v']]
# slots = [(u'singer','周杰伦',3,6),(u'song','青花瓷',7,10)]
# 示例输出：
# O O B-singer I-singer O B-song I-song O

def func(segments, slots):
    res = []
    pre = 0
    count = 0
    for i in range(len(segments)):
        segments[i].append(count)
        count += len(segments[i][0])
    i, j = 0, 0
    while j < len(slots):
        begin = True
        while i < len(segments) and segments[i][2] < slots[j][3]:
            if segments[i][2] < slots[j][2]:
                res += ["O"]
            else:
                if begin:
                    res += ["B-" + slots[j][0]]
                    begin = False
                else:
                    res += ["I-" + slots[j][0]]
            i += 1
        j += 1
    print(res)

func([['我', 'v'], ['想听', 'v'], ['周', 'v'], ['杰伦', 'v'], ['的', 'v'],
      ['青花', 'v'], ['瓷', 'v'], ['好吗', 'v']],
     [('singer', '周杰伦', 3, 6), ('song', '青花瓷', 7, 10)])
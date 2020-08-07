'''
假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来重建这个队列。

注意：
总人数少于1100人。

示例

输入:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

输出:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
'''
# 字典排序
dic = {2:12, 5:10, 4:8}
dic_by_key = sorted(dic.items(), key=lambda x: x[0])
dic_by_value = sorted(dic.items(), key=lambda x: x[1])
print(dic_by_key, dic_by_value)

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 贪心 https://leetcode-cn.com/problems/queue-reconstruction-by-height/solution/gen-ju-shen-gao-zhong-jian-dui-lie-by-leetcode/
        # 自定义排序：people 首先按people[0]降序，再按peolple[1]升序排序
        if not people: return []
        people = sorted(people, key = lambda x: (-x[0], x[1]))
        print(people)
        res = []
        for p in people:
            h, k = p
            res.insert(k, p)
            print(p, res)
        return res

        # 回溯  超时
        if not people: return []
        visited = {}
        self.res = None
        def backtrack(track):
            if not self.flag: return
            if len(track) == len(people):
                self.res = track
                return
            for i in range(len(people)):
                if visited.get(i, 0) == 0:
                    count = 0
                    for t in track:
                        if t[0] >= people[i][0]:
                            count += 1
                    if people[i][1] == count:
                        visited[i] = visited.get(i, 0) + 1
                        backtrack(track + [people[i]])
                        visited[i] = 0
        backtrack([])
        return self.res
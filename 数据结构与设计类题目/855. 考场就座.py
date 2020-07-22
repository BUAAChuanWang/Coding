'''
在考场里，一排有 N 个座位，分别编号为 0, 1, 2, ..., N-1 。

当学生进入考场后，他必须坐在能够使他与离他最近的人之间的距离达到最大化的座位上。如果有多个这样的座位，他会坐在编号最小的座位上。(另外，如果考场里没有人，那么学生就坐在 0 号座位上。)

返回 ExamRoom(int N) 类，它有两个公开的函数：其中，函数 ExamRoom.seat() 会返回一个 int （整型数据），代表学生坐的位置；函数 ExamRoom.leave(int p) 代表坐在座位 p 上的学生现在离开了考场。每次调用 ExamRoom.leave(p) 时都保证有学生坐在座位 p 上。

示例：

输入：["ExamRoom","seat","seat","seat","seat","leave","seat"], [[10],[],[],[],[],[4],[]]
输出：[null,0,9,4,2,null,5]
解释：
ExamRoom(10) -> null
seat() -> 0，没有人在考场里，那么学生坐在 0 号座位上。
seat() -> 9，学生最后坐在 9 号座位上。
seat() -> 4，学生最后坐在 4 号座位上。
seat() -> 2，学生最后坐在 2 号座位上。
leave(4) -> null
seat() -> 5，学生最后坐在 5 号座位上。
'''
import bisect
class ExamRoom(object):
    # 动态问题 一般考虑有序的数据结构 这里用数组加二分插入的方式实现了On的查找与Ologn的插入和删除
    # 如果是平衡二叉搜索树可以实现Ologn的查找删除与插入，不过需要对间隔做单独的处理，这里就算了。
    # https://leetcode-cn.com/problems/exam-room/solution/kao-chang-jiu-zuo-by-leetcode/
    def __init__(self, N):
        self.N = N
        self.students = []

    def seat(self):
        if not self.students:
            student = 0
        else:
            dist, student = self.students[0], 0  # 赋初值直接以最左边情况考虑
            for i, s in enumerate(self.students):  # 顺序遍历可以完成编号最小的要求，
                if i:
                    prev = self.students[i-1]
                    d = (s - prev) // 2
                    if d > dist:    # 因为当两短距离为奇数和偶数时，他们//2结果是一样的，此时dist不会更新
                        dist, student = d, prev + d
            d = self.N - 1 - self.students[-1]  # 额外考虑最右边情况
            if d > dist:
                student = self.N - 1
        bisect.insort_left(self.students, student)  # student 有序插入 self.students列表中 复杂度 Ologn
        return student

    def leave(self, p):
        index = bisect.bisect_left(self.students, p)
        self.students.pop(index)
        # self.students.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
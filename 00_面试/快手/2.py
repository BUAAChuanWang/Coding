#
# return a list for all `peek`
# @param op int整型二维数组 operators
# @return int整型一维数组
#
class Solution:
    def queueFromTwoStack(self, op):
        # write code here
        def __init__(self):
            self.stack1 = []
            self.stack2 = []

        def add(self, val):
            self.stack1.append(val)

        def dele(self, val):
            if self.stack2:
                return self.stack2.pop()
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            if self.stack2:
                return self.stack2.pop()
            else:
                return -1
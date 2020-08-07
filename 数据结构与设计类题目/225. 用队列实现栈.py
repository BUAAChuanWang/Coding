'''
使用队列实现栈的下列操作：

push(x) -- 元素 x 入栈
pop() -- 移除栈顶元素
top() -- 获取栈顶元素
empty() -- 返回栈是否为空

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-stack-using-queues
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = []  # q1永远都是往里面放新元素
        self.q2 = []  # q2永远都是在取栈顶元素时存放原来q1的元素，然后再交换q1q2

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        # 先将q1的前n个数据传到q2,再出队最后一个数据即栈顶。再q1,q2互换
        while self.q1:
            peek = self.q1.pop(0)
            if not self.q1:
                self.q1, self.q2 = self.q2, self.q1
                return peek
            self.q2.append(peek)

    def top(self) -> int:
        """
        Get the top element.
        """
        # 先将q1的前n个数据传到q2,再出队最后一个数据即栈顶。再q1,q2互换
        while self.q1:
            peek = self.q1.pop(0)
            if not self.q1:
                self.q2.append(peek)
                self.q1, self.q2 = self.q2, self.q1
                return peek
            self.q2.append(peek)

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.q1 == [] and self.q2 == []


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
'''
class MyStack:
    # 标准解法 剑指offer
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = collections.deque()
        self.q2 = collections.deque()


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if not self.q1 and not self.q2:
            self.q1.append(x)
        elif self.q1:
            self.q1.append(x)
        elif self.q2:
            self.q2.append(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if not self.q2:
            while self.q1:
                tmp = self.q1.popleft()
                if self.q1:
                    self.q2.append(tmp)
                else:
                    return tmp
        elif not self.q1:
            while self.q2:
                tmp = self.q2.popleft()
                if self.q2:
                    self.q1.append(tmp)
                else:
                    return tmp


    def top(self) -> int:
        """
        Get the top element.
        """
        if not self.q2:
            while self.q1:
                tmp = self.q1.popleft()
                self.q2.append(tmp)
            return tmp
        elif not self.q1:
            while self.q2:
                tmp = self.q2.popleft()
                self.q1.append(tmp)
            return tmp


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.q1 and not self.q2
'''
'''
import queue
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        #定义两个队列，来模拟栈
        self.q1 = queue.Queue()#q1存数据
        self.q2 = queue.Queue()#q2作为辅助队列，在进行出栈操作时，存储数据

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        #进栈操作
        self.q1.put(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        #先将q1的前n个数据传到q2,再出队最后一个数据即栈顶。再q1,q2互换
        while(not self.q1.empty()):#q1非空
            tmp = self.q1.get()
            if(self.q1.empty()):
                self.q1, self.q2 = self.q2, self.q1#q1,q2互换
                return tmp
            self.q2.put(tmp)

    def top(self) -> int:
        """
        Get the top element.
        """
        #栈顶元素及最后一个进入的元素，应该在q1的末尾
        while(not self.q1.empty()):#q1非空
            tmp = self.q1.get()
            self.q2.put(tmp)#与pop操作不同，就在于这个语句的位置。
            if(self.q1.empty()):
                self.q1, self.q2 = self.q2, self.q1#q1,q2互换
                return tmp


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.q1.empty()

'''

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
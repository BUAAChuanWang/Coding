'''
删除最小数量的无效括号，使得输入的字符串有效，返回所有可能的结果。

说明: 输入可能包含了除 ( 和 ) 以外的字符。

示例 1:

输入: "()())()"
输出: ["()()()", "(())()"]
示例 2:

输入: "(a)())()"
输出: ["(a)()()", "(a())()"]
示例 3:

输入: ")("
输出: [""]
'''
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # BFS  自己写的。删除最少的括号，直觉就是BFS
        def check(s):  # 栈模拟括号匹配，返回没有匹配的剩余括号
            stack = []
            for i in range(len(s)):
                if s[i] == "(":
                    stack.append("(")
                elif s[i] == ")":
                    if stack and stack[-1] == "(":
                        stack.pop()
                    else:
                        stack.append(")")
            return stack

        self.res = set()
        stack = check(s)  # stack是原s需要匹配的括号
        queue = [("", 0, 0)]  # cur_s, s_i, stack_j
        while queue:
            cur, idx, j = queue.pop(0)
            if j == len(stack):  # 需要匹配的括号数量 == len(stack)
                new_s = cur[:] + s[idx : ]  # 补全new_s
                if not check(new_s):
                    self.res.add(new_s)

            for i in range(idx, len(s)):  # BFS
                if j < len(stack) and s[i] == stack[j]:
                    queue.append((cur + s[idx : i], i + 1, j + 1))
        return list(self.res)
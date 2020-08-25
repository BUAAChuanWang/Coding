'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

 

参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3
示例 1：

输入: [1,6,3,2,5]
输出: false
示例 2：

输入: [1,3,2,6,5]
输出: true
'''
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        # 后序遍历=逆先序遍历 根右左
        # 利用单调栈 单调递增站  记录每一个右子树的根节点
        stack, root = [], float("+inf")
        for i in range(len(postorder) - 1, -1, -1):
            if postorder[i] > root: return False
            while(stack and postorder[i] < stack[-1]):
                root = stack.pop()
            stack.append(postorder[i])
        return True
'''
        if not postorder:return True
        def rec(postorder):
            if not postorder or len(postorder) == 1:return True
            root = postorder[-1]
            r = 0
            for i in range(len(postorder)):
                if postorder[i] >= root:    # >=是包含了没有有子树的情况，此时r=-1,右子树范围是[-1:-1]为空 如【4，6，7，5
                    r = i
                    break
            for i in range(r, len(postorder) - 1):
                if postorder[i] < root:
                    return False
            return rec(postorder[0 : r]) and rec(postorder[r : -1])
        return rec(postorder)
'''
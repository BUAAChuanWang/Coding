# LC 124 https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/
class Solution:
    def maxPathSum(self, root):
        '''
        衍生题，微软算法，树中最大路径和的路径（该路径不限制根节点到叶子节点，并且可以 左根右 这样子，不要求一定是父节点到子节点）
        '''
        # 递归 可以返回具体路径  Microsoft面试题
        if not root: return 0
        self.path = []
        self.gain = float("-inf")
        def helper(root):
            if not root:
                return 0, []
            left_gain, left_path = helper(root.left)
            right_gain, right_path = helper(root.right)
            root_gain = root.val + max(left_gain, right_gain)
            root_path = left_path + [root.val] if left_gain > right_gain else right_path + [root.val]   # 子路径按从下往上的顺序记录
            self.gain = max(self.gain, left_gain + right_gain + root.val)
            if self.gain == left_gain + right_gain + root.val:
                self.path = left_path + [root.val] + right_path[::-1]   # 右子树逆序，整体路径就顺序了
            return root_gain, root_path
        helper(root)
        print(self.gain, self.path)
        return self.gain, self.path

    def maxPathSum(self, root):
        '''
        LC124原题目，只需要求出最大路径和的值即可（该路径不限制根节点到叶子节点，并且可以 左根右 这样子，不要求一定是父节点到子节点）
        以下有 非递归 和 递归 两种方法
        '''
        # 递归 20200622 容易理解
        # https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/solution/er-cha-shu-zhong-de-zui-da-lu-jing-he-by-leetcode-/
        if not root: return 0
        self.res = float("-inf")
        def helper(root):
            if not root:
                return 0  # 以下后序遍历计算最大和
            left_gain = max(helper(root.left), 0)  # 小于零就不算了，因为有【2，-1，-2】这样的树存在，如果不取0，那么2节点处的贡献就是2-1=1而不是2了
            right_gain = max(helper(root.right), 0)
            root_gain = root.val + max(left_gain, right_gain)  # 一个方向的路径贡献
            self.res = max(self.res, left_gain + right_gain + root.val)
            return root_gain
        helper(root)
        return self.res

        # 非递归 参考评论区的一种解法
        maxSum = float("-inf")
        if not root: return maxSum
        sSum = []
        sTmp = [root]
        while sTmp:
            tmp = sTmp.pop()
            sSum.append(tmp)
            if tmp.left:    # 反先序遍历 即根右左  然后下面的while循环中，pop出来就是左右根的后续遍历，但实际上右左根也可以解决问题，只要是从底向上就行。
                sTmp.append(tmp.left)
            if tmp.right:   
                sTmp.append(tmp.right)
        # print(list(map(lambda x:x.val, sSum)))
        while sSum:
            tmp = sSum.pop()
            maxSum = max(maxSum, tmp.val)
            l = max(tmp.left.val, 0) if tmp.left else 0
            r = max(tmp.right.val, 0) if tmp.right else 0
            tSum = tmp.val + l + r  # 以该节点为跟的路径和
            tmp.val += max(l, r)    # 更改当前值为该节点的当前最大（单向）路径和
            maxSum = max(maxSum, tSum)
            # print(l, r, tSum, maxSum)
        return maxSum


    def maxPathSum(self, root):
        '''
        LC124 题解原答案
        '''
        # 202002
        def max_gain(node):
            nonlocal res # 类似全局变量，相当于在函数外定义了 self.res = float("-inf")
            if not node: return 0

            # 如果左右某一条路径为负数，不取，取0
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # 以这个node为顶点，也就是不走原来经过node上面的路径了，走例一中lchild->node->rchild的路径
            price_newpath = node.val + left_gain + right_gain

            res = max(res, price_newpath)
            # 返回用于递归的，也就是按之前方向的路径，即当前node只选择他的左右孩子中最大的那个作为路径的一部分进行下一次递归
            return node.val + max(left_gain, right_gain)
        res = float('-inf')
        max_gain(root)
        return res
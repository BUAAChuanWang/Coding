class Solution:
    # 非递归
    def preoder(self, root):
        res = []
        stack = []
        while stack or root:
            while root:
                res.append(root.val)    # 修改这一行的位置可变为中序
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = root.right
        return res

    def inorder(self, root):
        res = []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)    # 修改这一行的位置可变为先序
            root = root.right
        return res

    # 后序则是按左右根->逆序为根右左，那么就和先序一样的代码，只不过先右节点，再左节点，最后逆序结果就行
    def postorder(self, root):
        res = []
        stack = []
        while stack or root:
            while root:
                res.append(root.val)    # 和先序一样
                stack.append(root)
                root = root.right   # 根右左
            root = stack.pop()
            root = root.left
        return res[::-1]    # 逆序根右左 -》 左右根 即后序


    # 递归
    def preorder(self, root):
        self.res = []
        def helper(root):
            if not root:
                return
            self.res.append(root.val)   # 变这一行位置
            helper(root.left)
            helper(root.right)
        helper(root)
        return self.res

    def inorder(self, root):
        self.res = []
        def helper(root):
            if not root:
                return
            helper(root.left)
            self.res.append(root.val)
            helper(root.right)

        helper(root)
        return self.res

    def postorder(self, root):
        self.res = []

        def helper(root):
            if not root:
                return
            helper(root.left)
            helper(root.right)
            self.res.append(root.val)

        helper(root)
        return self.res
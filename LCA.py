class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 非递归  先序遍历记录路径
        def findpath(root, p):
            stack = [(root, [root])]
            while stack:
                root, path = stack.pop()
                if root == p:
                    return path
                if root.right:
                    stack.append((root.right, path + [root.right]))
                if root.left:
                    stack.append((root.left, path + [root.left]))
        path_p = findpath(root, p)
        path_q = findpath(root, q)
        i = 0
        while i < min(len(path_p), len(path_q)) and path_p[i] == path_p[i]:
            res = path_p[i]
            i += 1
        return res


        # 递归  先序遍历记录路径
        path_p, path_q = [], []
        def helper(root, p, path):
            if not root:
                return
            path.append(root)
            if root == p:
                return True
            if helper(root.left, p, path) or helper(root.right, p, path):
                return True
            path.pop()
        helper(root, p, path_p)
        helper(root, q, path_q)
        i = 0
        while i < min(len(path_p), len(path_q)) and path_p[i] == path_q[i]:
            res = path_p[i]
            i += 1
        return res


        # 递归 经典递归便利二叉树
        self.res = None
        def helper(root):
            if not root:
                return
            if root == p or root == q:
                cur = True
            else:
                cur = False
            left = helper(root.left)
            right = helper(root.right)
            if cur + left + right == 2:
                self.res = root
            return cur or left or right
        helper(root)
        return self.res
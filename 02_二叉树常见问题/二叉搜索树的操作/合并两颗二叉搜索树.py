# https://blog.csdn.net/qq_28468707/article/details/105298096?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param
class Solution:
    def merge2BST(self, root1, root2):
        def merge(p, q):  # 把节点q插入树p中
            dummy = p
            if not q:
                return
            t = TreeNode(q.val)
            while 1:
                if p.val > q.val:
                    if not p.left:
                        p.left = t
                        break
                    else:
                        p = p.left
                elif p.val < q.val:
                    if not p.right:
                        p.right = t
                        break
                    else:
                        p = p.right
            return dummy

        self.merge2BST(root1, root2.left)
        self.merge2BST(root1, root2)
        self.merge2BST(root1, root2.right)
        return root1


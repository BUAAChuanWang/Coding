'''
https://blog.csdn.net/qq_28468707/article/details/105298096?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param
1.题目描述
试编写程序，将两棵二叉排序树合并为一棵二叉排序树。

2.解题思路
将第二棵树的节点合并到第一棵树上，然后中序遍历第一棵树

递归中序遍历第二棵树的节点，再将节点插入到第一棵树中
'''

'''
5 3 7 1 # # 10
8 2 9 4 # # 12
'''

while 1:
    class TreeNode(object):
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None


    root1 = list(map(str, input().strip().split(" ")))
    root2 = list(map(str, input().strip().split(" ")))
    # root1 = [5, 3, 7, 2, 4, 6, 9]
    # root2 = [8, 1, 10]

    # 递归构建二叉树
    def helper(root, idx):
        if idx - 1 >= len(root): return None
        cur = TreeNode(int(root[idx - 1])) if root[idx - 1] != "#" else None
        if not cur: return
        cur.left = helper(root, 2 * idx)
        cur.right = helper(root, 2 * idx + 1)
        return cur

    cur1 = helper(root1, 1)
    cur2 = helper(root2, 1)
    # print(f"tree1 is :\n{cur1}")
    # print(f"tree2 is :\n{cur2}")


    # 合并两个二叉搜索树
    def merge2BST(root1, root2):
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

        merge(root1, root2.left)
        merge(root1, root2)
        merge(root1, root2.right)
        return root1

    mergedtree = merge2BST(cur1, cur2)

    # 中序遍历输出 查看结果是否正确
    res = []
    def inorder(root):
        global res
        if not root: return
        inorder(root.left)
        res.append(root.val)
        inorder(root.right)
    inorder(mergedtree)
    print(res)

'''
# 根据前序构造二叉树
def CreateBinTree(l):
    if l:
        t = l.pop(0)
    else:
        return
    if t == -1:
        return
    r = TreeNode(t)
    r.left = CreateBinTree(l)
    r.right = CreateBinTree(l)
    return r


# 中序遍历一棵二叉树
def Inorder(r):
    if not r:
        return
    Inorder(r.left)
    print(r.val)
    Inorder(r.right)


# 递归向一棵二叉树中插入节点
def Insert(root, val):
    if root == None:
        return TreeNode(val)

    def insertIntoTree(p, val):
        if p.val > val:
            if p.left == None:
                p.left = TreeNode(val)
            else:
                insertIntoTree(p.left, val)
        else:
            if p.right == None:
                p.right = TreeNode(val)
            else:
                insertIntoTree(p.right, val)

    insertIntoTree(root, val)


# 迭代向一棵二叉树插入节点（可选）
def insertIntoBST(self, root, val):
    if not root: return TreeNode(val)  # 如果没有根就返回这个节点
    temp = root
    while 1:
        if temp.val > val:  # 如果当前节点的值比val要大,那么val应该放在它的左边
            if not temp.left:
                temp.left = TreeNode(val)
                break
            else:
                temp = temp.left
        else:
            if not temp.right:
                temp.right = TreeNode(val)
                break
            else:
                temp = temp.right
    return root


# 中序遍历要插入的节点
def InsertBST(r1, r2):
    if r2:
        InsertBST(r1, r2.left)
        Insert(r1, r2.val)
        InsertBST(r1, r2.right)


if __name__ == '__main__':
    list1 = [12, 8, 4, -1, -1, 10, -1, -1, 16, 13, -1, -1, 18, -1, -1]
    list2 = [17, 6, 2, -1, -1, 9, -1, -1, 24, 19, -1, -1, 26, -1, -1]
    r1 = CreateBinTree(list1)
    r2 = CreateBinTree(list2)
    InsertBST(r1, r2)
    Inorder(r1)

"""
2 4 6 8 9 10 12 13 16 17 18 19 24 26
"""
'''




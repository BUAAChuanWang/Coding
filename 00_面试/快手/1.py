'''
在二叉树中找到一个节点的后继节点
限定语言：C、Python、C++、Javascript、Python 3、Java、Go
二叉树中一个节点的后继节点指的是，二叉树的中序遍历的序列中的下一个节点。(如果 node 是最后一个节点，则输出 0 )
示例1
输入
{6,3,9,1,4,8,10,#,2,#,5,7},10
输出
0
'''

class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def func(root, val):
    if not root: return 0
    root = [str(x) for x in root]

    def helper(idx):
        nonlocal root
        if idx - 1 >= len(root): return None
        cur = Node(root[idx - 1]) if root[idx - 1] != "#" else None
        if not cur: return
        cur.left = helper(2 * idx)
        cur.right = helper(2 * idx + 1)
        return cur
    cur = helper(1)
    # print(cur.val)

    res = []
    def h(cur):
        if not cur: return
        nonlocal res
        h(cur.left)
        res.append(cur.val)
        h(cur.right)

    h(cur)
    # print(res)
    idx = res.index(str(val))
    if idx < len(res) - 1 and res[idx + 1] != "#":
        print(res[idx + 1])
    else:
        print(0)

func([6, 3, 9, 1, 4, 8, 10, "#" ,2, "#", 5, 7], 4)
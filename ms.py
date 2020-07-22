class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def findpath(root):
    def __init__(self):
        self.res = []
        self.maxi = float("-inf")
        self.path = []

    def maxsum(self, root, path):
        if not root:
            return

        if root.left and root.left.val >= 0:
            left = maxsum(root.left, path + [root.left])
        else:
            left = path

        if root.right and root.right.val >= 0:
            right = maxsum(root.right, path + [root.right])
        else:
            right = path

        self.res = left if sum(left) > sum(right) else right

        new = left + [root] + right

        self.maxi = max(sum(list(map(lambda x:x.val, new))), sum(self.res))
        if self.maxi == sum(list(map(lambda x:x.val, new))):
            self.path.append(new)
            return new
        else:
            self.path.append(self.res)
            return self.res

    self.maxsum(root, [])
    findpath(root.left)
    findpath(root.right)
    return self.path
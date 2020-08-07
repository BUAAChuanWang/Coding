class MaxPQ:
    def __init__(self, cap):
        #存储元素的数组
        self.pq = []
        # 当前 Priority Queue 中的元素个数
        self.N = 0

    def max(self):
        # 返回当前队列中最大元素
        return self.pq[1]

    # 插入元素
    def insert(self, e):
        return
    # 删除并返回当前队列中最大元素
    def delMax(self):
        return

    # 上浮第 k 个元素，以维护最大堆性质
    def swim(sefl, k):
        # 如果浮到堆顶，就不能再上浮了
        while k > 1 and less(parent(k), k):
            # 如果第k个元素比上层大
            # 将k换上去
            exch(parent(k), k)
            k = parent(k)
        return

    # 下沉第 k 个元素，以维护最大堆性质
    def sink(self, k):
        # 如果沉到堆底，就沉不下去了
        while (left(k) <= N):
            # 先假设左边节点较大
            older = left(k)
            # 如果右边节点存在，比一下大小
            if right(k) <= N and less(older, right(k)):
                older = right(k)
            # 结点 k 比俩孩子都大，就不必下沉了
            if less(older, k):
                break
            # 否则，不符合最大堆的结构，下沉k节点
            exch(k, older)
            k = older
        return

    # 交换数组的两个元素
    def exch(self, i, j):
        pq[i], pq[j] = pq[j], pq[i]

    # pq[i] 是否比 pq[j] 小？
    def less(self, i, j):
        return pq[i].compareTo(pq[j]) < 0

    /* 还有 left, right, parent 三个方法 */
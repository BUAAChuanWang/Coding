'''
一家快递公司希望在新城市建立新的服务中心。公司统计了该城市所有客户在二维地图上的坐标，并希望能够以此为依据为新的服务中心选址：
使服务中心 到所有客户的欧几里得距离的总和最小 。
给你一个数组 positions ，其中 positions[i] = [xi, yi] 表示第 i 个客户在二维地图上的位置，返回到所有客户的 欧几里得距离的最小总和 。
换句话说，请你为服务中心选址，该位置的坐标 [xcentre, ycentre] 需要使下面的公式取到最小值：
与真实值误差在 10^-5 之内的答案将被视作正确答案。
示例 1：
输入：positions = [[0,1],[1,0],[1,2],[2,1]]
输出：4.00000
解释：如图所示，你可以选 [xcentre, ycentre] = [1, 1] 作为新中心的位置，这样一来到每个客户的距离就都是 1，所有距离之和为 4 ，
这也是可以找到的最小值。

示例 2：
输入：positions = [[1,1],[3,3]]
输出：2.82843
解释：欧几里得距离可能的最小总和为 sqrt(2) + sqrt(2) = 2.82843

示例 3：
输入：positions = [[1,1]]
输出：0.00000

示例 5：
输入：positions = [[0,1],[3,2],[4,5],[7,6],[8,9],[11,1],[2,12]]
输出：32.94036
解释：你可以用 [4.3460852395, 4.9813795505] 作为新中心的位置
'''
class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        if len(positions) == 1: return 0
        n = len(positions)
        # 计算距离
        def get_d(x, y):
            summ = 0.
            for a, b in positions:
                summ += ((x-a)**2 + (y-b)**2) ** 0.5
            return summ

        # loss = sum(delta_x ** 2 + delta_y ** 2) ** 0.5)
        # x = x - lr * dloss/dx = x - lr * sum(delta_x / (delta_x ** 2 + delta_y ** 2) ** 0.5))
        def gradient(x, y):
            dx, dy = 0, 0
            for a, b in positions:
                delta_x = x - a
                delta_y = y - b
                if delta_x ** 2 + delta_y ** 2 == 0:
                    continue
                dx += delta_x / ((delta_x ** 2 + delta_y ** 2) ** 0.5)
                dy += delta_y / ((delta_x ** 2 + delta_y ** 2) ** 0.5)
            return dx, dy

        # 初始化参数
        def init():
            x_ans, y_ans = 0, 0
            for x , y in positions:
                x_ans += x
                y_ans += y
            x0 = x_ans / n
            y0 = y_ans / n
            return x0, y0

        x0, y0 = init()
        lr = 16
        # 迭代更新
        while gradient(x0, y0) != (0.0, 0.0):
            # 不是极值点循环迭代
            dx, dy = gradient(x0, y0)
            x1 = x0 - lr * dx
            y1 = y0 - lr * dy
            while get_d(x1, y1) > get_d(x0, y0): # 步长太大导致错过最优点， 减小步长
                if abs(get_d(x1, y1) -get_d(x0, y0)) < 10 ** -5:
                    return get_d(x0,y0)
                lr /= 4
                x1 = x0 - dx * lr
                y1 = y0 - dy * lr
                # print("lr, x1,y1:", lr, x1, y1)
            x0, y0 = x1, y1
        return get_d(x0, y0)
#  https://blog.csdn.net/cqx2020/article/details/106366744/

import numpy as np


def get_distance(a, b):
    return np.sqrt(np.sum(np.power(a - b, 2)))  # 欧氏距离


def KMeans(X, k, max_iter=10, diff=0.001):
    n, m = X.shape[0], X.shape[1]
    k_index = np.random.randint(0, n, size=k)  # 随机生成k个索引值 [0, n)
    X_Core = X[k_index, :]  # 初始k个质心
    # X_Core = random.sample(X, k)

    old_var = float("-inf")
    distance = np.zeros((n, k))  # 初始化，k个质心到X的距离
    for iter in range(max_iter):  # 控制迭代
        if iter > 0:  # 第二次迭代开始 计算簇集合间的距离累加和的误差
            if new_var - old_var < diff:  # 终止条件
                break
            else:
                old_var = new_var

        for i in range(len(X)):
            for j in range(k):
                distance[i, j] = get_distance(X[i], X_Core[j])  # 计算所有质心到X的距离

        Y = np.array([d.argmin() for d in distance])  # 得到标签
        new_var = 0

        for j in range(k):
            cluster = X[Y == j, :]  # 第j个质心的聚类样本（共有k个）
            X_Core[j, :] = np.mean(cluster, axis=0)  # 计算新的质心   对应每个维度求平均

            new_var += np.sum(distance[Y == j, j], axis=0)  # 将簇类中各个向量与质心的距离进行累加求和

    return Y, X_Core

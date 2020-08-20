'''
主要业务：
搜索
NLP中台：客服智能对话 评论筛选和分类  曲库标签   歌单类型提取
'''
import numpy as np


def get_distance(a, b):
    return np.sqrt(np.sum(np.power(a - b, 2)))


def Kmeans(x, k, max_iter = 10, diff = 0.001):
    x = np.array(x)
    n, m = x.shape[0], x.shape[1]
    k_index = np.random.randint(0, n, size=k)
    x_core = x[k_index, :]

    # old_var =
    distance = np.zeros(((n, k)))
    for iter in range(max_iter):

        for i in range(len(x)):
            for j in range(k):
                distance[i, j] = get_distance(x[i], x_core[j])

        Y = np.array([d.argmin() for d in distance])
        for j in range(k):
            cluster = x[Y == j, :]
            x_core[j, :] = np.mean(cluster, axis=0)  # row

    return Y, x_core




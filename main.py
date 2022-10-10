from dis import dis
from math import dist
import time
from result import *

def linear_dt(arr):
    n = len(arr)
    v, z = np.zeros(n+1), np.zeros(n+1)

    k = 0
    v[0], z[0], z[1] = 0, -10000, 10000

    for q in range(1, n):
        s = ((arr[q] + q**2) - (arr[int(v[k])] + v[k]**2)) / (2*q - 2*v[k])

        while s <= z[k]:
            k -= 1
            s = ((arr[q] + q**2) - (arr[int(v[k])] + v[k]**2)) / (2*q - 2*v[k])

        k += 1
        v[k] = q
        z[k] = s
        z[k+1] = 10000

    k = 0
    dist_trans = np.zeros(n)
    for q in range(n):
        while z[k+1] < q:
            k += 1

        dist_trans[q] = (q - v[k])**2 + arr[int(v[k])]

    return dist_trans

def esdf(M, N, obstacle_list):
    """
    :param M: Row number
    :param N: Column number
    :param obstacle_list: Obstacle list
    :return: An array. The value of each cell means the closest distance to the obstacle
    """
    dist_mat = np.ones((M, N)) * 100
    for (i, j) in obstacle_list:
        dist_mat[i, j] = 0

    for i in range(N):
        dist_mat[:, i] = linear_dt(dist_mat[:, i])

    for i in range(M):
        dist_mat[i, :] = linear_dt(dist_mat[i, :])

    dist_mat = np.sqrt(dist_mat)
    return dist_mat

if __name__ == '__main__':
    st = time.time()
    for _ in range(int(2e4)):
        assert np.array_equal(esdf(M=3, N=3, obstacle_list=[[0, 1], [2, 2]]), res_1)
        assert np.array_equal(esdf(M=4, N=5, obstacle_list=[[0, 1], [2, 2], [3, 1]]), res_2)

    et = time.time()
    print(et-st)

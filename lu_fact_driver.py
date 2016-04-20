import numpy as np
from sys import argv
import util

def lu_fact(a):
    """Computes LU decomposition  for n*n matrix A

    :param a: n*n linearly independent matrix A
    :returns: matrices L, U, and the error ||LU - A||\inf
    """
    n = a.shape[0]
    u = np.copy(a).astype(float)
    transformations = []
    for i in range(n - 1):
        t = util.identity(n)
        pivot = u[i][i]
        if pivot == 0:
            for x in range(i + 1, n):
                if u[x][i] is not 0:
                    t[i] += t[x]
                    u[i] += u[x]
                    pivot = u[i][i]
                    break
        for j in range(i + 1, n):
            if u[j][i] is not 0:
                factor = - u[j][i] / pivot
                u[j] += factor * u[i]
                t[j] += factor * t[i]
        transformations.insert(0, t)
    if len(transformations) > 1:
        l_inv = reduce(np.dot, transformations)
    else:
        l_inv = transformations[0]
    l = np.linalg.inv(l_inv)
    dist = np.dot(l, u) - a
    return l, u, util.norm_inf(dist)


def print_usage():
    print('Sample Usage:')
    print('python lu_driver.py <path_to_matrix_A>')
    print('python lu_driver.py test/1_H.dat')


def main():
    if len(argv) != 2:
        print_usage()
        return
    a = np.loadtxt(argv[1])
    l, u, err = lu_fact(a)
    print "L:", l
    print "U:", u
    print "Error:", err

if __name__ == "__main__":
    main()

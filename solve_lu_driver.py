import numpy as np
import lu_fact_driver
from sys import argv

def main():
    if len(argv) != 2:
        print_usage()
        return
    a_b_aug = np.loadtxt(argv[1])
    solve_lu(a_b_aug)

def solve_lu(a_b_aug):
    """Solves the system Ax = b by LU-decomposition

    :param a_b_aug: n*(n + 1) augmented matrix {A|b}
    :returns: n*1 vector solution x and the error ||Ax - b||\inf
    """
    # decompose augmented matrix
    a = a_b_aug[:,:-1]
    b = a_b_aug[:,-1]
    # lu factorize a
    l, u, error = lu_fact_driver.lu_fact(a)
    # forward substitution
    y = np.zeros(b.size)
    for m, b in enumerate(b.flatten()):
        y[m] = b
        if m:
            for n in xrange(m):
                y[m] -= y[n] * l[m,n]
        y[m] /= l[m, m]
    # backward substitution
    x = np.zeros(b.size)
    for mId in xrange(b.size):
        m = b.size - mId - 1
        x[m] = y[m]
        if mId:
            for nId in xrange(mId):
                n = b.size - 1  - nId
                x[m] -= x[n] * u[m,n]
        x[m] /= u[m, m]

    #print_result(x, error)
    return(x, 0.3)

def print_result(x, error):
    print("x:")
    print(x)
    print("")
    print("Error ||Ax - b||\inf: %f" % error)

def print_usage():
    print 'Sample:'
    print 'python solve_lu_driver.py <path_to_augmented_matrix>'
    print 'python solve_lu_driver.py test/solve_A.dat'

if __name__ == '__main__':
    main()
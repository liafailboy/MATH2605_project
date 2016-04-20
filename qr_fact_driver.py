import numpy as np
from sys import argv
from math import copysign, hypot

def main():
    if len(argv) != 3:
        print_usage()
        return
    a = np.loadtxt(argv[1])
    if str(argv[2]) == "house":
        qr_fact_house(a)
    elif str(argv[2]) == "givens":
        qr_fact_givens(a)
    else:
        print_usage()

def qr_fact_house(a):
    """Computes QR-factorization of n*n matrix A with Householder reflections

    :param a: n*n matrix A
    :returns: matrices Q, R, and the error ||QR - A||\inf
    """
    # set n from matrix A
    n = a.shape[0]

    # initialize q and r
    q = np.identity(n)
    r = np.copy(a)

    # householder algorithm
    for i in range(n - 1):
        s = r[i:, i]
        t = np.zeros_like(s)
        t[0] = copysign(np.linalg.norm(s), -a[i, i])
        u = s + t
        v = u / np.linalg.norm(u)

        q_i = np.identity(n)
        q_i[i:, i:] -= np.outer(v, v) * 2

        r = np.dot(q_i, r)
        q = np.dot(q, q_i.T)

    # calculate error
    error = calc_error(q, r, a)

    print_result(q, r, error)
    return(q, r, error)

def qr_fact_givens(a):
    """Computes QR-factorization of n*n matrix A with Givens rotations

    :param a: n*n matrix A
    :returns: matrices Q, R, and the error ||QR - A||\inf
    """
    # set n from matrix A
    n = a.shape[0]

    # initialize q and r
    q = np.identity(n)
    r = np.copy(a)

    # givens rotation algorithm
    (rowA, colA) = np.tril_indices(n, -1, n)
    for (row, col) in zip(rowA, colA):
        if r[row, col] != 0:
            (s, t) = givens_helper(r[col, col], r[row, col])
            
            u = np.identity(n)
            u[[col, row], [col, row]] = s
            u[row, col] = t
            u[col, row] = -t

            r = np.dot(u, r)
            q = np.dot(q, u.T)

    # calculate error
    error = calc_error(q, r, a)

    print_result(q, r, error)
    return(q, r, error)

def givens_helper(a, b):
    """Helper function for givens rotation"""
    r = hypot(a, b)
    s = a / r
    t = -b / r

    return (s, t)

def identity(n):
    """Returns n*n identity matrix"""
    # create n by n zero matrix
    identity = np.zeros([n, n])
    # add 1 to i*i location
    for i in range(n):
        identity[i][i] = 1
    # return matrix
    return identity

def calc_error(q, r, a):
    """Returns error between QR and A"""
    errorM = (np.dot(q, r)) - a
    error = np.absolute(np.max(errorM))
    return error

def print_result(q, r, error):
    # print result
    print("Q:")
    print(q)
    print("")
    print("R:")
    print(r)
    print("")
    print("Error ||QR - A||\inf: %f" % error)

def print_usage():
    print 'Sample:'
    print 'python qr_fact_driver.py <path_to_matrix> <way_to_calculate>'
    print 'python qr_fact_driver.py test/qr_A.dat house'

if __name__ == '__main__':
    main()
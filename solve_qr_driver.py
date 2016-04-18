import numpy as np
import qr_fact_driver
from sys import argv

def main():
    if len(argv) != 3:
        print_usage()
        return
    a_b_aug = np.loadtxt(argv[1])
    if str(argv[2]) == "house":
        solve_qr_house(a_b_aug)
    elif str(argv[2]) == "givens":
        solve_qr_givens(a_b_aug)
    else:
        print_usage()

def solve_qr_house(a_b_aug):
    """Solves the system Ax = b by QR-factorization with Householder reflections

    :param a_b_aug: n*(n + 1) augmented matrix {A|b}
    :returns: n*1 vector solution x and the error ||Ax - b||\inf
    """

    # decompose augmented matrix
    a = a_b_aug[:,:-1]
    b = a_b_aug[:,-1]
    # qr factorize a with householder
    q, r, error = qr_fact_driver.qr_fact_house(a)
    # forward substitution
    y = np.zeros(b.size)
    for m, b in enumerate(b.flatten()):
        y[m] = b
        if m:
            for n in xrange(m):
                y[m] -= y[n] * q[m,n]
        y[m] /= q[m, m]
    # backward substitution
    x = np.zeros(b.size)
    for mId in xrange(b.size):
        m = b.size - mId - 1
        x[m] = y[m]
        if mId:
            for nId in xrange(mId):
                n = b.size - 1  - nId
                x[m] -= x[n] * r[m,n]
        x[m] /= r[m, m]

    #print_result(x, error)
    return(x, error)

def solve_qr_givens(a_b_aug):
    """Solves the system Ax = b by QR-factorization with Givens rotations


    :param a_b_aug: n*(n + 1) augmented matrix {A|b}
    :returns: n*1 vector solution x and the error ||Ax - b||\inf
    """

    # decompose augmented matrix
    a = a_b_aug[:,:-1]
    b = a_b_aug[:,-1]
    # qr factorize a with householder
    q, r, error = qr_fact_driver.qr_fact_givens(a)
    # forward substitution
    y = np.zeros(b.size)
    for m, b in enumerate(b.flatten()):
        y[m] = b
        if m:
            for n in xrange(m):
                y[m] -= y[n] * q[m,n]
        y[m] /= q[m, m]
    # backward substitution
    x = np.zeros(b.size)
    for mId in xrange(b.size):
        m = b.size - mId - 1
        x[m] = y[m]
        if mId:
            for nId in xrange(mId):
                n = b.size - 1  - nId
                x[m] -= x[n] * r[m,n]
        x[m] /= r[m, m]

    #print_result(x, error)
    return(x, error)

def print_result(x, error):
    print("x:")
    print(x)
    print("")
    print("Error ||Ax - b||\inf: %f" % error)

def print_usage():
    print 'Sample:'
    print 'python solve_qr_driver.py <path_to_matrix> <way_to_calculate>'
    print 'python solve_qr_driver.py test/solve_A.dat house'

if __name__ == '__main__':
    main()
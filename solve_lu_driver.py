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
    
    # calculate x by forward substitution
    x = forward_substitution(l, (np.dot(a.T, b)))

    for i in range(0, x.shape[0]):
        if ((i + 1) % 2 == 0):
            x[i] = -x[i]

    error = calc_error(a, x, b)

    print_result(x, error)
    return(x, error)

def forward_substitution(a, b):
    """Returns x by forward substitution"""
    n = a.shape[0]
    b = np.copy(b)
    x = np.zeros_like(b)

    x[0] = b[0] / a[0, 0]

    for i in range(0, n):
        x[i] = (b[i] - np.dot(a[i, :i].flatten(), x[:i]))

    return x

def calc_error(a, x, b):
    """Returns error between Ax and b"""
    errorM = (np.dot(a, x)) - b
    error = np.absolute(np.max(errorM))
    return error

def print_result(x, error):
    print("x:")
    print(x)
    print("")
    print("Error ||Ax - b||\inf: %f" % error)

def print_usage():
    print 'Sample:'
    print 'python solve_lu_driver.py <path_to_augmented_matrix>'
    print 'python solve_lu_driver.py test/2_Ab.dat'

if __name__ == '__main__':
    main()
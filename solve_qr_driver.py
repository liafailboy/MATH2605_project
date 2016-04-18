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
    
    # calculate x using least square
    x = least_square(a, b, q, r)
    
    # calculate error of x
    error = calc_error(a, x, b)

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
    
    # calculate x using least square
    x = least_square(a, b, q, r)
    
    # calculate error of x
    error = calc_error(a, x, b)

    print_result(x, error)
    return(x, error)

def least_square(a, b, q, r):
    """Returns x value by least square"""
    _, n = r.shape
    x = np.linalg.solve(r[:n, :], np.dot(q.T, b)[:n])
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
    print 'python solve_qr_driver.py <path_to_matrix> <way_to_calculate>'
    print 'python solve_qr_driver.py test/solve_A.dat house'

if __name__ == '__main__':
    main()
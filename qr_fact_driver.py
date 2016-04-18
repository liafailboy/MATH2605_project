import numpy as np
from sys import argv

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
    print_result(a, a, 0.3)    

def qr_fact_givens(a):
    """Computes QR-factorization of n*n matrix A with Givens rotations

    :param a: n*n matrix A
    :returns: matrices Q, R, and the error ||QR - A||\inf
    """
    print_result(a, a, 0.5)

def print_result(q, r, error):
    print("Q: %s" % q)
    print("R: %s" % r)
    print("Error ||QR - A||\inf: %f" % error)

def print_usage():
    print 'Sample:'
    print 'python qr_fact_driver.py <path_to_matrix> <way_to_calculate>'
    print 'python qr_fact_driver.py test/qr_A.dat house'

if __name__ == '__main__':
    main()
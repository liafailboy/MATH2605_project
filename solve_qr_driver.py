import numpy as np
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
	print_result(a_b_aug, 0.3)

def solve_qr_givens(a_b_aug):
	"""Solves the system Ax = b by QR-factorization with Givens rotations


	:param a_b_aug: n*(n + 1) augmented matrix {A|b}
	:returns: n*1 vector solution x and the error ||Ax - b||\inf
	"""
	print_result(a_b_aug, 0.5)

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
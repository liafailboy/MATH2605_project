import numpy as np
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
	print("solve with lu")

def print_usage():
    print 'Sample:'
    print 'python solve_lu_driver.py <path_to_augmented_matrix>'
    print 'python solve_lu_driver.py test/solve_A.dat'

if __name__ == '__main__':
    main()
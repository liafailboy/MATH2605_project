import iterative_methods
import numpy as np
from sys import argv

def jacobi_iter(a_b_aug, u, e, m):
	"""Approximates the solution to the system Ax = b
	using Jacobi iterative method

	:param a_b_aug: n*(n + 1) augmented matrix {A|b}
	:param u: the n*1 vector for the initial guess of x_0
	:param e: tolerance that determines when the approximation is close enough
	"""
	x_n, iterations, error =  iterative_methods.jacobi(a_b_aug, u, e, m)
	print('Closest approximation of x: %s' % x_n)
	print('Number of iterations: %d' % iterations)
	print('Error of ||Ax_n - b||\inf: %f' % error)

def print_usage():
    print 'Sample Usage:'
    print 'python jacobi_driver.py <path_to_augmented_matrix> <path_to_x_0> <e> <m>'
    print 'python jacobi_driver.py test/iter_aug.dat test/iter_x_0.dat 0.0001 30'

def main():
    if len(argv) != 5:
        print_usage()
        return
    a_b_aug = np.loadtxt(argv[1])
    u = np.loadtxt(argv[2])
    e = float(argv[3])
    m = int(argv[4])
    jacobi_iter(a_b_aug, u, e, m)

if __name__ == '__main__':
    main()

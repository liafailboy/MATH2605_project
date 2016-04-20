import iterative_methods
import numpy as np
from sys import argv

def power_method(a, u_0, w, e, m):
	"""Approximates an eigenvalue and associated eigenvector of an n*n matrix
	using the power method. If the procedure iterates M times and has not
	attained an answer with sufficient accuracy, returns tuple (None, None, M)

	:param a: n*n matrix A with floating-point real numbers as entries (n >= 2)
	:param u_0: n*1 vector u_0 of n floating point real numbers that serves as
		initial guess for an eigenvector of A
	:param w: n*1 vector w of n floating point real numbers that serves as an
		auxiliary vector
	:param e: tolerance that determines when the approximation is close enough
	:param m: positive integer M giving the maximum number of times to iterate
		the power method before quitting
	:returns: appriximate largest eigenvalue in view of absolute value,
		corresponding eigenvector, and the iteration number N
	"""
	eigenvalue, eigenvector, iterations =  iterative_methods.power(a, u_0, w, e, m)
	print('Maximum eigenvalue in terms of absolute value: %s' % eigenvalue)
	print('Corresponding eigenvector: %s' % eigenvector)
	print('Number of iterations: %d' % iterations)

def print_usage():
    print('Sample Usage:')
    print('python power_driver.py <path_to_matrix_A> <path_to_x_0> <path_to_w> <e> <m>')
    print('python power_driver.py test/power_A.dat test/power_x_0.dat test/power_w.dat 0.0001 30')

def main():
    if len(argv) != 6:
        print_usage()
        return
    a = np.loadtxt(argv[1])
    u = np.loadtxt(argv[2])
    w = np.loadtxt(argv[3])
    e = float(argv[4])
    m = int(argv[5])
    power_method(a, u, w, e, m)

if __name__ == '__main__':
    main()

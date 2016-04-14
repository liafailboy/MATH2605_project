import numpy as np

def parse(filename):
	return np.loadtxt(filename)

# part a
def lu_fact(a):
	"""Computes LU decomposition  for n*n matrix A

	:param a: n*n matrix A
	:returns: matrices L, U, and the error ||LU - A||\inf
	"""
	pass

# part b
def qr_fact_house(a):
	"""Computes QR-factorization of n*n matrix A with Householder reflections

	:param a: n*n matrix A
	:returns: matrices Q, R, and the error ||QR - A||\inf
	"""
	pass

def qr_fact_givens(a):
	"""Computes QR-factorization of n*n matrix A with Givens rotations

	:param a: n*n matrix A
	:returns: matrices Q, R, and the error ||QR - A||\inf
	"""
	pass

# part c
def solve_lu(a_b_aug):
	"""Solves the system Ax = b by LU-decomposition

	:param a_b_aug: n*(n + 1) augmented matrix {A|b}
	:returns: n*1 vector solution x and the error ||Ax - b||\inf
	"""
	pass

def solve_qr_house(a_b_aug):
	"""Solves the system Ax = b by QR-factorization with Householder reflections

	:param a_b_aug: n*(n + 1) augmented matrix {A|b}
	:returns: n*1 vector solution x and the error ||Ax - b||\inf
	"""
	pass

def solve_qr_givens(a_b_aug):
	"""Solves the system Ax = b by QR-factorization with Givens rotations


	:param a_b_aug: n*(n + 1) augmented matrix {A|b}
	:returns: n*1 vector solution x and the error ||Ax - b||\inf
	"""
	pass

# main
if __name__ == "__main__":
	print parse("test/1_H.dat")

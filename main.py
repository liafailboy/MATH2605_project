import numpy as np


def parse(filename):
	return np.loadtxt(filename)

# part a
def lu_fact(a):
	"""Computes LU decomposition  for n*n matrix A
	
	:param a: n*n linearly independent matrix A
	:returns: matrices L, U, and the error ||LU - A||\inf
	"""
	n = a.shape[0]
	u = np.copy(a).astype(float)
	transformations = []
	for i in range(n - 1):
		t = identity(n)
		pivot = u[i][i]
		if pivot == 0:
			for x in range(i + 1, n):
				if u[x][i] is not 0:
					t[i] += t[x]
					u[i] += u[x]
					pivot = u[i][i]
					break
		for j in range(i + 1, n):
			if u[j][i] is not 0:
				factor = - u[j][i] / pivot
				u[j] += factor * u[i]
				t[j] += factor * t[i]
		transformations.insert(0, t)
	if len(transformations) > 1:
		l_inv = reduce(np.dot, transformations)
	else:
		l_inv = transformations[0]
	l = np.linalg.inv(l_inv)
	dist = np.dot(l, u) - a
	return l, u, np.max(np.absolute(dist))


def identity(n):
	"""Returns n*n identity matrix"""
	identity = np.zeros([n, n])
	for i in range(n):
		identity[i][i] = 1
	return identity





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



# part d
def jacobi_iter(a_b_aug, e, m):
	"""Approximates the solution to the system Ax = b
	using Jacobi iterative method

	:param a_b_aug: n*(n + 1) augmented matrix {A|b}
	:param e: tolerance that determines when the approximation is close enough
	:returns: approximate solution x_n, number of iterations n, and the error
		||Ax_n - b||\inf
	"""
	pass

def gs_iter(a_b_aug, e, m):
	"""Approximates the solution to the system Ax = b
	using Gauss-Seidel iterative method

	:param a_b_aug: n*(n + 1) augmented matrix {A|b}
	:param e: tolerance that determines when the approximation is close enough
	:returns: approximate solution x_n, number of iterations n, and the error
		||Ax_n - b||\inf
	"""
	pass



# part e
def power_method(a, u_0, w, e, m):
	"""Approximates an eigenvalue and associated eigenvector of an n*n matrix
	using the power method. If the procedure iterates M times and has not
	attained an answer with sufficient accuracy, returns tuple (None, M)

	:param a: n*n matrix A with floating-point real numbers as entries (n >= 2)
	:param u_0: n*1 vector u_0 of n floating point real numbers that serves as
		initial guess for an eigenvector of A
	:param w: n*1 vector w of n floating point real numbers that serves as an
		auxiliary vector
	:param e: tolerance that determines when the approximation is close enough
	:param m: positive integer M giving the maximum number of times to iterate 
		the power method before quitting
	:returns: approximate largest eigenvalu lambda_N in view of absolute value,
		the corresponding eigenvector u_N, and the iteration number N
	"""
	pass

# main
if __name__ == "__main__":
	print parse("test/1_H.dat")

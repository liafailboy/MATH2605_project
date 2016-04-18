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

# main
if __name__ == "__main__":
	print parse("test/1_H.dat")

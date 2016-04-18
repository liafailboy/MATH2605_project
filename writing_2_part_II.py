# This file was used to generate the data for Writing 2: Convergence of Iterative Methods
import numpy as np

import iterative_methods
import util

gs_results = []
gs_iterations = []

initial_errors = []

jacobi_results = []
jacobi_iterations = []

A_b_aug = np.array([[1., 2., 3.], [2., 1., 3.]])
e = 0.00005
exact_x = np.array([1., 1.])
u = np.zeros(2)

max_iters = []
gs_errors = []
jacobi_errors = []

for m in range(2, 10 + 1):
    gs_x_n, gs_iteration, gs_error = iterative_methods.gauss_seidel(A_b_aug, u, e, m)
    j_x_n, j_iteration, j_error = iterative_methods.jacobi(A_b_aug, u, e, m)

    max_iters.append(m)
    gs_errors.append(gs_error)
    jacobi_errors.append(j_error)

print('Iterations, Gauss-Seidel Error, Jacobi Error')
for m, gs_error, j_error in zip(max_iters, gs_errors, jacobi_errors):
    print('%d, %f, %f' % (m, gs_error, j_error))

# This file was used to generate the data for Writing 2: Convergence of Iterative Methods
import numpy as np

import iterative_methods
import util

gs_results = []
gs_iterations = []

initial_errors = []

jacobi_results = []
jacobi_iterations = []

A_b_aug = np.loadtxt('test/2_Ab.dat')
e = 0.00005
m = 100

exact_x = np.array([39.0 / 40, -13.0 / 40, 12.0 / 40])

for i in range(100):
    u = np.random.uniform(-10, 10, 3)
    gs_x_n, gs_iteration, gs_error = iterative_methods.gauss_seidel(A_b_aug, u, e, m)
    j_x_n, j_iteration, j_error = iterative_methods.jacobi(A_b_aug, u, e, m)
    gs_results.append(gs_x_n)
    gs_iterations.append(gs_iteration)

    initial_errors.append(util.norm_inf(u - exact_x))

    jacobi_results.append(j_x_n)
    jacobi_iterations.append(j_iteration)

gs_approx_x = util.average(gs_results)
jacobi_approx_x = util.average(jacobi_results)

gs_error = util.norm_inf(gs_approx_x - exact_x)
jacobi_error = util.norm_inf(jacobi_approx_x - exact_x)

jacobi_gs_ratios = [float(j) / gs for j, gs in zip(gs_iterations, jacobi_iterations)]
average_ratio = sum(jacobi_gs_ratios) / len(jacobi_gs_ratios)

for error, gs_iteration, j_iteration in zip(initial_errors, gs_iterations, jacobi_iterations):
    print('%f, %d, %d' % (error, gs_iteration, j_iteration))

print('')

print('Average Gauss-Seidel Error: %f' % gs_error)
print('Average Jacobi Error: %f' % jacobi_error)
print('Ratio of Jacobi iterations / Gauss-Seidel Iterations: %f' % average_ratio)

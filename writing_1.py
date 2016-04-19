import numpy as np

from lu_fact_driver import lu_fact
from qr_fact_driver import qr_fact_givens, qr_fact_house
import util

def gen_hilbert(n):
    A = np.zeros([n, n])
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            A[i - 1, j - 1] = 1. / (i + j - 1)
    b = np.array([0.1 ** ( float(n) / 3)] * n)
    return A, b

print('x_sol, Hilbert Size, LU Error, Givens Error, Householder Error, Inverse Error')
for n in range(2, 20 + 1):
    H, b = gen_hilbert(n)
    # aug = np.c_[H, b]
    l, u, lu_err = lu_fact(H)
    q_givens, r_givens, givens_err = qr_fact_givens(H)
    q_house, r_house, house_err = qr_fact_house(H)

    x_sol = np.linalg.inv(H).dot(b)
    floating_error = util.norm_inf(H.dot(x_sol) - b)

    print('%s, %d, %f, %f, %f, %f' % (x_sol, n, lu_err, givens_err, house_err, floating_error))

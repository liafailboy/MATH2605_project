import numpy as np

from sys import stdout
from iterative_methods import power
import util

A = [-2, 1, 2, 0, 2, 3, 2, 1, -2]
A = np.reshape(A, (3, 3))
P = (1 + 4) / 2.
VECTOR = np.array([1, 0, 0]).reshape((3, 1))


def main(): 
    p1 = -P
    a1 = A - util.identity(3) * p1
    p2 = P
    a1 = np.linalg.inv(a1)
    a2 = A - util.identity(3) * p2
    a2 = np.linalg.inv(a2)
    val, vec, n_iter = power(a1, VECTOR, VECTOR, 0.00005, 100)
    val = val if val is None else 1 / val + p1
    print "eigenvalue for p1: ", val
    val, vec, n_iter = power(a2, VECTOR, VECTOR, 0.00005, 100)
    val = val if val is None else 1 / val + p2
    print "eigenvalue for p2: ", val


if __name__ == "__main__":
    main()

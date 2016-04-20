import numpy as np

from sys import stdout
from iterative_methods import power
import util

VECTORS = [(1., 0.), (0., 1.), (1., 1.)]
for i in range(len(VECTORS)):
    tup = VECTORS[i]
    VECTORS[i] = np.reshape(tup, (len(tup), 1))


def main(): 
    iterations = []
    inv_iterations = []
    dets = []
    traces = []
    total_fails = 0

    for _ in range(200):
        i = 0
        vec = None
        inv_vec = None
        tries = -1
        while vec is None or inv_vec is None:
            i = 0
            a, a_inv = get_matrix()
            while vec is None and i < len(VECTORS):
                val, vec, n_iter = power(a, VECTORS[i], VECTORS[i], 0.00005, 100)
                i += 1
            i = 0
            while inv_vec is None and i < len(VECTORS):
                inv_val, inv_vec, inv_n_iter = power(a_inv, VECTORS[i], VECTORS[i], 0.00005, 100)
                i += 1
            tries += 1
        total_fails += tries
        iterations.append(n_iter / 100.)
        inv_iterations.append(inv_n_iter / 100.)
        traces.append(trace(a))
        dets.append(determinant_2_2(a))
    util.plot([min(dets)-.1, max(dets)+.1, min(traces)-.1, max(traces)+.1],
          dets, 
          traces, 
          iterations, 
          "Determinant", 
          "Trace", 
          "Determinant vs Trace by A Power Iteration", 
          "writing/3/writing_3_a")
    util.plot([min(dets)-.1, max(dets)+.1, min(traces)-.1, max(traces)+.1],
          dets, 
          traces, 
          inv_iterations, 
          "Determinant", 
          "Trace", 
          "Determinant vs Trace by A Inverse Power Iteration",
          "writing/3/writing_3_a_inv")
    print "Number of rejected matrices: ", total_fails



def trace(a):
    """Returns the trace of a 2x2 matrix"""
    return a[0][0] + a[1][1]

def get_matrix():
    """Returns tuple a 2x2 matrix and its inverse"""
    a = np.random.uniform(-2, 2, (2, 2))
    while not (determinant_2_2(a)):
        a = np.random.uniform(-2, 2, (2, 2))
    return a, np.linalg.inv(a)

def determinant_2_2(a):
    """Returns the determinant of a 2x2 matrix"""
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]

if __name__ == "__main__":
    main()

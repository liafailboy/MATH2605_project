import numpy as np
import math

def norm(vector):
    sum_squared = sum([i**2 for i in vector])
    return math.sqrt(sum_squared)

def norm_inf(vector):
    return max([abs(i) for i in vector])

def find_null_space(A):
    pass

def find_eiganvector(A, eiganvalue):
    for i in range(len(A)):
        A[i, i] -= eiganvalue
    return find_null_space(A)[0]

def average(vectors):
    total = np.zeros(len(vectors[0]))
    for vector in vectors:
        total += vector
    total /= len(vectors)
    return total

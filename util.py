import numpy as np
import math

def norm(vector):
    sum_squared = sum([i**2 for i in vector])
    return math.sqrt(sum_squared)

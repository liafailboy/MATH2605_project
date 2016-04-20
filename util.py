import numpy as np
import math
import matplotlib.pyplot as plt

def norm(vector):
    sum_squared = sum([i**2 for i in vector])
    return math.sqrt(sum_squared)


def norm_inf(a):
    return np.max(np.absolute(a))


def average(vectors):
    total = np.zeros(len(vectors[0]))
    for vector in vectors:
        total += vector
    total /= len(vectors)
    return total


def identity(n):
    """Returns n*n identity matrix"""
    identity = np.zeros([n, n])
    for i in range(n):
        identity[i][i] = 1
    return identity


def plot(axes, x, y, t, x_label, y_label, title, name):
    plt.scatter(x, y, c=t, cmap='winter')
    plt.axis(axes)
    plt.title(title)
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    plt.savefig(name+".png", dpi=500)
    # plt.show()
    plt.clf()

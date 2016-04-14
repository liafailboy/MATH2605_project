import numpy as np
import util

def make_s_jacobi(a):
    # S is the diagonal of a
    size = len(a)
    s = np.zeros(shape=(size, size))
    for i in range(size):
        s[i, i] = a[i, i]
    return s

def make_s_gs(a):
    # S is diagonal + lower triangle of a.
    size = len(a)
    s = np.zeros(shape=(size, size))
    for i in range(size):
        s[i, i] = a[i, i]
        for j in range(i):
            s[i, j] = a[i, j]

def _iterate(a, s, t, b, u, e, m):
    # x_n+1 = S^{-1}(X_n T + b)
    s_inverse =  np.linalg.inv(s)
    x_n = u
    for i in range(1, m+1):
        print x_n
        x_next = s_inverse.dot(-t.dot(x_n) + b)
        tolerance = util.norm(x_next - x_n)
        print x_next
        if tolerance <= e:
            error = util.norm(-t.dot(x_next) - b)
            return x_next, i, error
        x_n = x_next
    # A good approximation was not found in a reasonable number of iterations.
    return None, i, m

def jacobi(a_b_aug, u, e, m):
    a = a_b_aug[:, :-1]
    b = a_b_aug[:,-1]
    s = make_s_jacobi(a)
    t = a - s
    return _iterate(a, s, t, b, u, e, m)

def gauss_seidel(a_b_aug, e, m):
    a = a_b_aug[:, :-1]
    b = a_b_aug[:,-1]
    s = make_s_gs(a)
    t = a - s
    return _iterate(a, s, t, b, u, e, m)

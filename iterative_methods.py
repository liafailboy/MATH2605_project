import numpy as np
import util

def _make_s_jacobi(a):
    # S is the diagonal of a
    size = len(a)
    s = np.zeros(shape=(size, size))
    for i in range(size):
        s[i, i] = a[i, i]
    return s

def _make_s_gs(a):
    # S is diagonal + lower triangle of a.
    size = len(a)
    s = np.zeros(shape=(size, size))
    for i in range(size):
        s[i, i] = a[i, i]
        for j in range(i):
            s[i, j] = a[i, j]
    return s

def _iterate(a, s, t, b, u, e, m):
    # x_n+1 = S^{-1}(X_n T + b)
    s_inverse =  np.linalg.inv(s)
    x_n = u
    for i in range(1, m+1):
        x_next = s_inverse.dot(-t.dot(x_n) + b)
        tolerance = util.norm_inf(x_next - x_n)
        if tolerance <= e:
            error = util.norm_inf(a.dot(x_next) - b)
            return x_next, i, error
        x_n = x_next
    # A good approximation was not found in a reasonable number of iterations.
    return None, m, util.norm_inf(a.dot(x_n) - b)

def jacobi(a_b_aug, u, e, m):
    a = a_b_aug[:, :-1]
    b = a_b_aug[:,-1]
    s = _make_s_jacobi(a)
    t = a - s
    return _iterate(a, s, t, b, u, e, m)

def gauss_seidel(a_b_aug, u, e, m):
    a = a_b_aug[:, :-1]
    b = a_b_aug[:,-1]
    s = _make_s_gs(a)
    t = a - s
    return _iterate(a, s, t, b, u, e, m)

def power(a, u_0, w, e, m):
    u_n = u_0
    for i in range(1, m+1):
        u_next = a.dot(u_n)
        u_next /= util.norm(u_next)
        tolerance = util.norm_inf(u_next - u_n)
        if tolerance <= e:
            w_dot_u = np.transpose(w).dot(u_n)
            # if w_dot_u == 0:
            #     return None, None, i
            eigenvalue = np.transpose(w).dot(a.dot(u_n)) / w_dot_u
            eigenvector = u_next
            return eigenvalue, eigenvector, i
        u_n = u_next
    return None, None, m

import numpy as np


def strassens_algorithm(u, v, n):
    if n == 1:
        return u[0, 0] * v[0, 0]
    else:
        n2 = n // 2
        a = u[:n2, :n2]
        b = u[:n2, n2:]
        c = u[n2:, :n2]
        d = u[n2:, n2:]
        e = v[:n2, :n2]
        f = v[:n2, n2:]
        g = v[n2:, :n2]
        h = v[n2:, n2:]
        p1 = strassens_algorithm(a, f-h, n2)
        p2 = strassens_algorithm(a+b, h, n2)
        p3 = strassens_algorithm(c+d, e, n2)
        p4 = strassens_algorithm(d, g-e, n2)
        p5 = strassens_algorithm(a+d, e+h, n2)
        p6 = strassens_algorithm(b-d, g+h, n2)
        p7 = strassens_algorithm(a-c, e+f, n2)
        c11 = p5+p4-p2+p6
        c12 = p1+p2
        c21 = p3+p4
        c22 = p1+p5-p3-p7
        c = np.zeros((n, n))
        c[:n2, :n2] = c11
        c[:n2, n2:] = c12
        c[n2:, :n2] = c21
        c[n2:, n2:] = c22
        return c


def test_strassens_algorithm():
    n = 256
    a = np.random.rand(n, n)
    b = np.random.rand(n, n)
    c = strassens_algorithm(a, b, n)
    assert np.allclose(a.dot(b), c)

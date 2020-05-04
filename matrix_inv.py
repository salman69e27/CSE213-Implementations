import numpy as np
# tol is the threshold under which the number is considered zero.
def inv(A, tol=1e-9):
    m = A.shape[0]
    if A.shape != (m, m):
        raise Exception('Matrix is not square')
    I = np.identity(m)
    A_b = np.c_[A, I]
    for i in range(m):
        if A_b[i, i] == 0:
            p = np.argmax(np.abs( A_b[i:, i])) + i
            A_b[ [i, p], : ] = A_b[ [p, i], : ]
        if abs(A_b[i, i]) < tol:
            raise Exception('Matrix is singular')
        for k in range(m):
            if k != i:
                A_b[k, :] -= A_b[i, :]/A_b[i, i] * A_b[k, i]
    A_b = A_b / np.diag(A_b).reshape(-1, 1)
    return A_b[:, m:]

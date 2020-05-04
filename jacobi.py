import numpy as np
from numpy.linalg import inv

def jacobi(A, b, N):
    '''
    return array S where column k represents x at iteration k
    '''
    diag = np.diag(A)
    T = (A - np.diag(diag))/diag.reshape(-1, 1)
    b_ = b/diag
    x = np.zeros(len(A))
    for i in range(N): x = b_-T@x
    return x

# np.random.seed(42)
# A = 10 * np.eye(10)
# A = A + np.random.rand(10,10)
# b = np.sum(A, axis=1)
# print(jacobi(A, b, 100))

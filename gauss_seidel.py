import numpy as np
from numpy.linalg import inv

def seidel(A, b, N):
    '''
    return array S where column k represents x at iteration k
    '''
    D = np.diag( np.diag(A) )
    L, U = np.tril(A), np.triu(A)-D
    x = np.zeros(len(A))
    for i in range(N): x = inv(L)@(b-U@x)
    return x

# np.random.seed(42)
# A = 10 * np.eye(10)
# A = A + np.random.rand(10,10)
# b = np.sum(A, axis=1)
# print(seidel(A, b, 5))

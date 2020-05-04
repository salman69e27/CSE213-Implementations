class SolveEcholonForm:
    def __init__(self):
        pass
    def solve(self, A, b):
        A_b = np.c_[A, b.reshape(-1, 1)].astype('float64')
        self.exit_flag_ = 1
        ans = -1
        n, m = A.shape
        self.ef_ = None
        if n != m:
            self.message_ = 'Matrix is not square'
            returned_value = (ans, reduced_matrix, exit_flag, message)
            return ans
        for i in range(n-1):
            if A_b[i, i] == 0:
                p = np.argmax(np.abs( A_b[i:, i]))
                p += i
                A_b[[i, p], :] = A_b[[p, i], :]
            if A_b[i, i] == 0:
                self.message_ = 'Can\'t find pivot for column {}'.format(i+1)
                return ans
            for k in range(i+1, n):
                A_b[k, :] -= A_b[i, :]/A_b[i, i] * A_b[k, i]
        if A_b[-1, -2] == 0 and A_b[-1, -1] != 0:
            self.message_ = 'Matrix is not consistent'
            returned_value = (ans, reduced_matrix, exit_flag, message)
            return ans
        if A_b[-1, -2] == 0 and A_b[-1, -1] == 0:
            self.message_ = 'Can\'t find pivot for column {}'.format(n)
            returned_value = (ans, reduced_matrix, exit_flag, message)
            return ans
        x = np.zeros(n)
        for i in range(n-1, -1, -1):
            x[i] = (A_b[i, -1] - A_b[i, i+1:-1].dot(x[i+1:]).flatten()[0])/A_b[i, i]
        ans = x
        self.exit_flag_ = 0
        self.message_ = 'Succeeded!'
        self.ef_ = A_b.copy()
        return ans

class Neville:
    def fit(self, X, Y):
        self.X = X
        self.Y = Y
        return self
    def evaluate(self, x):
        if not (hasattr(self, 'X') and hasattr(self, 'Y')):
            raise Exception('Call fit first')
        N = len(self.X)
        level = 1
        Q = self.Y.copy()
        calc = lambda xi, xj, L, R, x: ( (x-xi)*R - (x-xj)*L ) / (xj-xi)
        while N-level>=1:
            Q = [calc(self.X[i], self.X[i+level], Q[i], Q[i+1], x) for i in range(N-level)]
            level += 1
        return Q[0]

# neville = Neville()
# X = [1, 2, 3]
# Y = [1, 4, 9]
# neville.fit(X, Y)
# print(neville.evaluate(5))

from numpy import product

class LagrangeInterpolation:
    def fit(self, X, Y):
        self.X = X
        self.Y = Y
        return self
    def L(self, ind, x):
        top = product([ x-self.X[i] for i in range( len(self.X) ) if i != ind ])
        bottom = product([ self.X[ind] - self.X[i] for i in range( len(self.X) ) if i != ind ])
        return top/bottom
    def evaluate(self, x):
        if not (hasattr(self, 'X') and hasattr(self, 'Y')):
            raise Exception('Call fit first')
        L_list = [ self.L(ind, x) for ind in range( len(self.X) ) ]
        return sum([ y*l for (y, l) in zip(self.Y, L_list) ])

# lagrange = LagrangeInterpolation()
# X = [1, 2, 3]
# Y = [1, 4, 9]
# lagrange.fit(X, Y)
# print(lagrange.evaluate(5))

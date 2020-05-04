from numpy import hstack, ones
from numpy.linalg import inv
from sklearn.preprocessing import PolynomialFeatures

class LinearRegression:
    def __init__(self, include_bias=True, polynomial_features=None):
        self.include_bias = include_bias
        self.polynomial_features = polynomial_features
    def fit(self, X, y):
        self.X = X
        self.y = y
        if self.polynomial_features is not None:
            self.X = PolynomialFeatures(degree=self.polynomial_features, include_bias=False).fit_transform(X)
        if self.include_bias:
            self.X = hstack( (ones((len(X), 1)), self.X) )
        self.coef_ = (inv(self.X.T@self.X)@self.X.T@self.y).reshape(-1, 1)
        self.intercept_ = None
        if self.include_bias:
            self.intercept_ = self.coef_[0]
            self.coef_ = self.coef_[1:]
        return self
    def predict(self, x):
        if not (hasattr(self, 'coef_') and hasattr(self, 'intercept_')):
            raise Exception('Call fit first')
        if self.polynomial_features is not None:
            x = PolynomialFeatures(degree=self.polynomial_features, include_bias=False).fit_transform(x)
        ans = x @ self.coef_
        if self.include_bias:
            ans += self.intercept_
        return ans

# lin_reg = LinearRegression(include_bias=False)
# from numpy import linspace, cos, pi
# f = lambda x: cos(pi*x)
# x = linspace(0, 1, 21, endpoint=True).reshape(-1, 1)
# lin_reg.fit(x, f(x))
# pred = lin_reg.predict([[0.1]])
# print(pred)

from numpy import array, nan, vstack
from pandas import DataFrame

class FixedPoint:
    def __init__(self, exit_condition=lambda f, p, eps: abs(f(p)-p) < eps, eps=1e-6):
        self.exit_condition = exit_condition
        self.eps = eps
    def solve(self, f, p):
        self.table_ = array( [p, f(p), nan] )
        self.f_ = f
        while not self.exit_condition(f, p, self.eps):
            p = f(p)
            self.table_ = vstack( ( self.table_, array( [ p, f(p), abs(p-f(p)) ] ) ) )
        self.table_ = DataFrame(self.table_, columns=['p', 'f(p)', 'absolute error'])
        return p
    def print_history(self):
        if not hasattr(self, 'table_'):
            raise Exception('Call solve first')
        print(self.table_)

# fixed_point = FixedPoint()
# f = lambda x : 1 + (3*x**3-5*x**2)/4
# p0 = 0
# fixed_point.solve(f, p0)
# fixed_point.print_history()

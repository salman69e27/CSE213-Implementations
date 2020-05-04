from numpy import array, vstack, nan
from pandas import DataFrame
class Bisection:
    def __init__(self, exit_condition = lambda a, b, eps: abs(b-a) <= 2*eps, eps=1e-6):
        self.exit_condition = exit_condition
        self.eps = eps
    def solve(self, f, a, b):
        p = a + (b-a)/2
        fa, fb, fp = f(a), f(b), f(p)
        self.table_ = array( [a, b, p, fa, fp, fb, nan] )
        self.f_ = f
        while not self.exit_condition(a, b, self.eps):
            (a, b) = (p, b) if fp*fa > 0 else (a, p)
            p_old = p
            p = a + (b-a)/2
            fa, fb, fp = f(a), f(b), f(p)
            self.table_ = vstack( (self.table_,
                array( [a, b, p, fa, fp, fb, abs(p-p_old)] )) )
        self.table_ = DataFrame(self.table_, 
            columns=['a', 'b', 'p', 'f(a)', 'f(p)', 'f(b)', 'absolute error'])
        self.p_ = p
        return p
    def print_history(self):
        if not hasattr(self, 'table_'):
            raise Exception('Call solve first')
        print(self.table_)

# f = lambda x : 3*(x+1)*(x-0.5)*(x-1)
# (a, b) = (-1.25, 2.5)
# bisection = Bisection()
# bisection.solve(f, a, b)
# bisection.print_history()

from numpy import array, nan, vstack
from pandas import DataFrame

class Newton:
    def __init__(self, exit_condition=lambda p_old, p_new, eps: abs(p_old-p_new)<eps, eps=1e-6):
        self.exit_condition = exit_condition
        self.eps = eps
    def solve(self, f, df, p_old):
        p_new = p_old - f(p_old) / df(p_old)
        self.table_ = array([ p_old, p_new, abs(p_old-p_new) ])
        self.f_ = f
        while not self.exit_condition(p_old, p_new, self.eps):
            p_old = p_new
            p_new = p_old - f(p_old) / df(p_old)
            self.table_ = vstack( (self.table_, array([ p_old, p_new, abs(p_old-p_new) ])) )
        self.table_ = DataFrame(self.table_, columns=['p_old', 'p_new', 'absolute error'])
        return p_new
    def print_history(self):
        try:
            print(self.table_)
        except:
            raise Exception('Call solve first')

# f = lambda x : 1 + (3*x**3-5*x**2)/4
# df = lambda x : (9*x**2-10*x)/4
# newton = Newton()
# newton.solve(f, df, 0.1)
# newton.print_history()

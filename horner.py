import numpy as np
import pandas as pd

def horner(coef, x):
    n = len(coef)-1
    p = coef[-1]
    for i in range(n-1, -1, -1):
        p = coef[i]+x*p
    return p

# print(horner([2, 3, -2, 10], 2))


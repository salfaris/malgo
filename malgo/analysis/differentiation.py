# System imports
import sys
sys.path.append('.')

from malgo.custom_type import Function, Real
from malgo.test import FunctionTest

def df(f: Function, h: Real, c: Real) -> Real:
    return float(f(c+h)-f(c)) / h

def df_alt(f: Function, h: Real, c: Real) -> Real:
    return float(f(c+h)-f(c-h)) / (2*h)

def ddf(f: Function, h: Real, c: Real) -> Real:
    pass

print(df(lambda x: x**2, 0.0001, 5))
print(ddf(lambda x: x**2, 0.0001, 5))

if __name__ == '__main__':
    for func in FunctionTest().get_functions():
        print(df(func, 0.00001, 5))
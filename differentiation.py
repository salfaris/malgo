from custom_type import Function, Real
from test import FunctionTest

def dif(f: Function, h: Real, c: Real) -> Real:
    return float(f(c+h)-f(c)) / h

def dif_alt(f: Function, h: Real, c: Real) -> Real:
    return float(f(c+h)-f(c-h)) / (2*h)


# print(dif(lambda x: x**2, 0.0001, 5))
# print(two_dif(lambda x: x**2, 0.0001, 5))

# if __name__ == '__main__':
#     for func in FunctionTest().get_functions():
#         print(dif(func, 0.00001, 5))
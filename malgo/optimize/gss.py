# System imports
import sys
sys.path.append('.')

from malgo.custom_type import Real, Function
import numpy as np

def golden_search(a: Real, b: Real, f: Function):
    """Returns the minima of f(x) on the interval [a, b]
    using the golden section search method.
    """

    def choose_sec_points():
        _alpha = (3-np.sqrt(5)) / 2.
        x1 = a + _alpha*(b-a)
        x2 = b - _alpha*(b-a)
        return x1, x2

    x1, x2 = choose_sec_points()

    while abs(f(x1)-f(x2)) > 10**(-12):
        if f(x1) > f(x2):
            a, y = x1, x2
        else:
            b, y = x2, x1
        x1, x2 = choose_sec_points()

    return y
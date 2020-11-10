# System imports
import sys
sys.path.append('.')

import numpy as np
from malgo.custom_type import Function, Real
from malgo.models import IntegralKernel

def trapezoidal(f: Function, a: Real, b: Real, n: int) -> Real:
    """Integration using the trapezoidal rule.
    
    Args:
        f: Function to be integrated.
        a: Interval startpoint.
        b: Interval endpoint.
        n: Number of subintervals to divide the interval [a, b].
    """
    dx = float(b-a) / n
    xs = np.arange(start=a, stop=b+dx, step=dx)
    fs = list(map(lambda x: f(x), xs))  # f(a + ih)
    return (sum(fs) - 0.5*(fs[0] + fs[-1])) * dx
# System imports
import sys
sys.path.append('.')

import numpy as np
from malgo.custom_type import Function, Real
from malgo.models import IntegralKernel

def midpoint(f: Function, a: Real, b: Real, n: int):
    """Integration using the midpoint rule.
    
    Args:
        f: Function to be integrated.
        a: Interval startpoint.
        b: Interval endpoint.
        n: Number of subintervals to divide the interval [a, b].
    """
    dx = float(b-a) / n
    xs = np.arange(start=a+dx/2, stop=b+dx/2, step=dx)
    fs = list(map(lambda x: f(x), xs))
    return sum(fs) * dx


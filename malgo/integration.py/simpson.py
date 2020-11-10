# System imports
import sys
sys.path.append('.')

import numpy as np
from malgo.custom_type import Function, Real
from malgo.models import IntegralKernel

def simpson(f: Function, a: Real, b: Real, n: int) -> Real:
    """Integration using the Simpson's rule."""
    # Step size, h
    dx = float(b-a) / n
    
    # First sum term, f(a + ih)
    xs1 = np.arange(start=a+dx, stop=b, step=dx)
    fs1 = list(map(lambda x: f(x), xs1))
    
    # Second sum term, f(a + h/2 + ih)
    xs2 = np.arange(start=a+dx/2, stop=b+dx/2, step=dx)
    fs2 = list(map(lambda x: f(x), xs2))
    
    total_sum = (sum(fs1) + 2*sum(fs2) + 0.5*(f(a) + f(b))) * dx/3
    return total_sum


# TEST CODE
if __name__ == '__main__':
    func = lambda x: 2./(x**2+1)
    ker = IntegralKernel(func=func,
                         startpoint=-1,
                         endpoint=1)
    ker.add_method([simpson])
    ker.integrate_pretty(subdivisions=100)
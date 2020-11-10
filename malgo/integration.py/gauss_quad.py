# System imports
import sys
sys.path.append('.')

import numpy as np
from malgo.custom_type import Function, Real
from malgo.models import IntegralKernel

def gauss_quadrature(f: Function, a: Real, b: Real, n: int) -> Real:
    """Integration using the Simpson's rule."""
    return


# TEST CODE
if __name__ == '__main__':
    func = lambda x: 2./(x**2+1)
    ker = IntegralKernel(func=func,
                         startpoint=-1,
                         endpoint=1)
    ker.add_method([gauss_quadrature])
    ker.integrate_pretty(subdivisions=100)
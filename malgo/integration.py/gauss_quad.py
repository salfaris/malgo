# System imports
import sys
sys.path.append('.')

import math
from typing import Tuple, List
from malgo.custom_type import Function, Real, Vector
from malgo.models import IntegralKernel

import numpy as np
from scipy.integrate import quad

def gauss_quadrature(f: Function, a: Real, b: Real, n: int) -> Real:
    """Integration using the Gauss's quadrature rule.

    Args:
        f: Function to be integrated. 
        n: Number of nodes and weights to generate.
        a: Lower bound of interval to integrate over.
        b: Upper bound of interval to integrate over.
    """
    nodes, weights = nodes_and_weights(n, a, b)
    return sum(weights * f(nodes))
  
def nodes_and_weights(
    n: int, a: Real, b: Real) -> Tuple[List[Real], List[Real]]:
    """Computes ci, xi and Ai."""

    # STEP 4: Finding ci
    B = np.zeros((n+1, n+1))
    u = np.zeros(n+1)

    # Rewrite as a matrix equation; then solve.
    for k in range(n+1):
        u[k] = - moment(n+1+k, a, b)
        for i in range(n+1):
            B[k,i] = moment(k+i, a, b)
    cs = np.linalg.solve(B, u)

    # c_(n+1) = 1; we assumed the polynomial Phi_(n+1) to be monic.
    cs = np.append(cs, [1])  

    # STEP 5: Finding xi
    xs = np.roots(cs[::-1]).real 
    
    # STEP 6: Finding Ai
    As = np.zeros(n+1)

    # Rewrite as a matrix equation; then solve.
    for k in range(n+1):
        u[k] = moment(k, a, b)
        for i in range(n+1):
            B[k,i] = xs[i]**k
    As = np.linalg.solve(B, u)

    return xs, As

def moment(k: int, a: Real, b: Real) -> Real:
    """The moment at index k."""
    WEIGHT_FUNC = lambda x: 1
    integrand = lambda x: WEIGHT_FUNC(x) * x**k
    return quad(integrand, a, b)[0]

# TEST CODE
if __name__ == '__main__':
    func = lambda x: 2./(x**2+1)
    ker = IntegralKernel(func=func,
                         startpoint=-1,
                         endpoint=1)
    ker.add_method(gauss_quadrature)
    ker.integrate_pretty(subdivisions=10)
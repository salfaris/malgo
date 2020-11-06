from custom_type import Indeterminate, Real, pt_index
from typing import List, Tuple
import numpy as np

def basis_polynomial(x: Indeterminate, i: pt_index, xs: List[Real]) -> Real:
    """The Lagrange basis polynomial.
    
    Args:
        x: Indeterminate.
        i: Index of the basis.
        xs: x-coordinate of known data points to be interpolated.
    """
    xi = xs[i]
    prod = 1
    for xj in xs:
        if xj != xi:
            prod *= float(x-xj) / (xi-xj)
    return prod

def lagrange(x: Indeterminate, xs: List[Real], ys: List[Real]) -> Real:
    """The Lagrange interpolation polynomial.
    
    Args:
        x: Indeterminate.
        xs: The xi values of the known points to be interpolated.
        ys: The yi values of the known points to be interpolated.

    Returns:
        float: A single interpolated point.
    """
    psum = 0
    for i, (_, yi) in enumerate(zip(xs, ys)):
        psum += yi * basis_polynomial(x, i, xs)
    return psum

def chebyshev(a: Real, b: Real, n: int) -> List[Real]:
    """Generates a sequence of `n` Chebyshev points over the interval [a, b].
    
    Args:
        a: The startpoint of [a, b].
        b: The endpoint of [a, b].
        n: The number of Chebyshev points to be generated.
    
    Returns:
        A sequence of Chebyshev points.
    """
    cheb_points = []
    for i in range(n):
        cos_term = np.cos(np.pi*(i+0.5)/(n+1))
        point = float(a+b)/2 - float(a-b)/2*cos_term
        cheb_points.append(point)
    return cheb_points

# # TEST CASE
# if __name__ == '__main__':
#     xs = [1, 2, 3, 4, 5, 6]
#     ys = [0, 0.841471, 0.909297, 0.14122, -0.756802, -0.958924]
    
#     # print(lagrange(1.5, xs, ys))
#     print(chebyshev(a=-5, b=5, n=10))
        
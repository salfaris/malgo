from typing import List, Tuple
from custom_type import Indeterminate, Real, pt_index

def basis_polynomial(x: Indeterminate, i: pt_index, xs: List[Real]):
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

def lagrange(x: Indeterminate, points: List[Tuple[Real, Real]]):
    """The Lagrange interpolation polynomial.
    
    Args:
        x: Indeterminate.
        points: The data points (xi, yi) to be interpolated.
    """
    psum = 0
    xs = [point[0] for point in points]
    for idx, point in enumerate(points):
        yi = point[1]
        psum += yi * basis_polynomial(x, idx, xs)
    return psum


# # TEST CASE
# if __name__ == '__main__':
#     xs = [1, 2, 3, 4, 5, 6]
#     ys = [0, 0.841471, 0.909297, 0.14122, -0.756802, -0.958924]
#     points = [(xi, yi) for xi, yi in zip(xs, ys)]
#     print(lagrange(1.5, points))
        
import sys
sys.path.append('.')

from typing import List
from malgo.custom_type import Function, Real

def modified_secant(f: Function, x0: Real, x1: Real):
    """The improved secant method root-finding algorithm.
    
    Args:
        f: Function to find solution for.
        x0: First point for the secant line approximation.
        x1: Second point for the secant line approximation.
        
    Returns:
        float: The solution to f(x) = 0.
    """
    xs = [x0, x1]  # Sequence of xn.
    tol = 10**(-7)
    while True:
        res = secant_recurrence_formula(f, xs[-1], xs[-2])
        abs_diff = abs(res-xs[-1])
        if abs_diff < tol:
            xs.append(res)
            break
        xs.append(res)
    return xs[-1]

def secant(f: Function, x0: Real, x1: Real):
    """The secant method root-finding algorithm.
    
    Args:
        f: Function to find solution for.
        x0: First point for the secant line approximation.
        x1: Second point for the secant line approximation.
        
    Returns:
        float: The solution to f(x) = 0.
    """
    xs = [x0, x1]  # Sequence of xn.
    for _ in range(10):
        res = secant_recurrence_formula(f, xs[-1], xs[-2])
        xs.append(res)
    return xs[-1]

def secant_recurrence_formula(f: Function, x0: Real, x1: Real):
    """The secant recurrence formula."""
    dx = float(x1 - x0)
    df = float(f(x1) - f(x0))
    return x1 - f(x1) * dx/df


# # TEST CASE
# if __name__ == '__main__':
#     f = lambda x: x**3/3 - 2*x**2 + x - 4
#     df = lambda x: x**2 - 4*x + 1

#     for method in [secant]:
#         res = method(f, 4, 9)
#         print(res)
#         print(f(res))
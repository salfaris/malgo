"""
All functions below has arguments as follows:
    f: Function to be integrated.
    a: Interval startpoint.
    b: Interval endpoint.
    n: Number of subintervals to divide the interval [a, b].
"""

import numpy as np
from custom_type import Function, Real

def midpoint(f: Function, a: Real, b: Real, n: int):
    """Integration using the midpoint rule."""
    dx = float(b-a) / n
    xs = np.arange(start=a+dx/2, stop=b+dx/2, step=dx)
    fs = list(map(lambda x: f(x), xs))
    return sum(fs) * dx

def trapezoidal(f: Function, a: Real, b: Real, n: int) -> Real:
    """Integration using the trapezoidal rule."""
    dx = float(b-a) / n
    xs = np.arange(start=a, stop=b+dx, step=dx)
    fs = list(map(lambda x: f(x), xs))  # f(a + ih)
    return (sum(fs) - 0.5*(fs[0] + fs[-1])) * dx

def simpson(f: Function, a: Real, b: Real, n: int) -> Real:
    """Integration using the Simpson's rule."""
    dx = float(b-a) / n
    xs1 = np.arange(start=a+dx, stop=b, step=dx)
    xs2 = np.arange(start=a+dx/2, stop=b+dx/2, step=dx)
    fs1 = list(map(lambda x: f(x), xs1))  # f(a + ih)
    fs2 = list(map(lambda x: f(x), xs2))  # f(a + h/2 + ih)
    return (sum(fs1) + 2*sum(fs2) + 0.5*(f(a) + f(b))) * dx/3


# func = lambda x: 2./(x**2+1)
# func = lambda x: x**2
# startpoint = -1
# endpoint = 1
# ran_intervals = 100

# trap = trapezoidal(func, startpoint, endpoint, ran_intervals)
# mp = midpoint(func, startpoint, endpoint, ran_intervals)
# sp = simpson(func, startpoint, endpoint, ran_intervals)

# ls = [trap, mp, sp]

# def diff_pi(x):
#     diff = abs(x - np.pi)
#     print(diff)
    
# for i in ls:
#     print(i)
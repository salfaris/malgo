from custom_type import Function, Real
import numpy as np

def midpoint(f: Function, a: Real, b: Real, n: int):
    dx = float(b-a) / n
    xs = np.arange(start=a+dx/2, stop=b+dx/2, step=dx)
    fs = list(map(lambda x: f(x), xs))
    return sum(fs) * dx

def trapezoidal(f: Function, a: Real, b: Real, n: int) -> Real:
    """Integration using the trapezoidal rule.
    
    Args:
        f: Function to be integrated
        a: Interval startpoint
        b: Interval endpoint
        n: Number of subintervals to divide the interval [a, b]
    """
    dx = float(b-a) / n
    xs = np.arange(start=a, stop=b+dx, step=dx)
    fs = list(map(lambda x: f(x), xs))
    return (sum(fs) - 0.5*(fs[0] + fs[-1])) * dx

f = lambda x: 2./(x**2+1)

print(trapezoidal(f, -1, 1, 100))
print(midpoint(f, -1, 1, 100))
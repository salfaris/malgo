import sys
sys.path.append('.')

from malgo.custom_type import Function, Real

def newton(f: Function, df: Function, x0: Real):
    """The Newton method root-finding algorithm.
    
    Args:
        f: Function to find solution for.
        df: Derivative of f.
        x0: Initial starting point.
        
    Returns:
        float: The solution to f(x) = 0.
    """
    xs = [x0]  # Sequence of xn.
    for _ in range(10):
        xs.append(newton_recurrence_formula(f, df, xs[-1]))
    return xs[-1]

def improved_newton(f: Function, df: Function, x0: Real, n: int = 10):
    # Sequence of x
    xs = [x0]  
    
    # Get latest x value in sequence and apply formula.
    for _ in range(n):
        xs.append(newton_recurrence_formula(f, df, xs[-1]))
        
    return xs[-1]

def newton_recurrence_formula(f: Function, df: Function, x0: Real):
    """The Newton recurrence formula."""
    return x0 - float(f(x0))/df(x0)

def recursive_newton(f: Function, df: Function, x0: Real, n: int = 10):
    return x0 if n <=0 else recursive_newton(
                                f, df, x0 - f(x0)/df(x0), n-1)


# # TEST CASE
# if __name__ == '__main__':
#     f = lambda x: x**3/3 - 2*x**2 + x - 4
#     df = lambda x: x**2 - 4*x + 1

#     for method in [improved_newton, recursive_newton]:
#         res = method(f, df, 7, 100)
#         print(res)
#         # print(f(res))
    
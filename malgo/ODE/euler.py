import sys
sys.path.append('.')

import numpy as np
from typing import List
from malgo.custom_type import Function, Real, Vector

def euler(init_conds: List[Real], a: Real, b: Real, N: int, f: Function):
    """Solves an ODE using the Euler method.
    
    Args:
       init_conds: List of initial value conditions.
       a: Initial value of x, also used as startpoint of interval.
       b: Endpoint of interval.
       N: Number of subintervals.
       f: The n-1 th order system if this is an n-th 
            order ODE. It admits the form f(x, y_vec).
    """
    h = float(b-a) / N
    ys = np.zeros((N+1, len(init_conds)))
    ys[0] = init_conds
    xs = np.arange(start=a, stop=b+h, step=h)
    for i in range(N):
        xi, yi = a + i*h, ys[i]
        ys[i+1] = yi + h*F_vec(xi, yi, f)
    return xs, ys

def F_vec(x: Real, y_vec: Vector, f: Function):
    """Pops and append to transform y_vec into F_vec.
    
    Args:
        x: Indeterminate
        y_vec: The n-vector (y0, y1, ..., y(n-1))
        f: The function to append; it defines the ODE. It 
            admits the form f(x, y_vec).
        
    Returns:
        F_vec, a vector of the form (y1, y2, ..., f(x, y_vec))
    """
    F_res = y_vec.tolist()
    F_res.pop(0)
    F_res.append(f(x, y_vec))
    return np.array(F_res)

def F_vec_benj(x: Real, y_vec: Vector, f: Function):
    """This is Benjamin's implementation of popping and
    transforming y_vec into F_vec.
    
    Args:
        x: Indeterminate
        y_vec: The n-vector (y0, y1, ..., y(n-1))
        f: The function to append; it defines the ODE. It 
            admits the form f(x, y_vec).
        
    Returns:
        F_vec, a vector of the form (y1, y2, ..., f(x, y_vec))
    """
    y_len = len(y_vec)
    F_res = np.zeros(y_len)
    for i in range(y_len-1):
        F_res[i] = y_vec[i+1]
    F_res[-1] = f(x, y_vec)
    return F_res


if __name__ == '__main__':
    def func(x, yvec):
        return x

    init_conds = [1.]
    xs, ys = euler(init_conds, a=0, b=1, N=1000, f=func)
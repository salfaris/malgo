import sys
sys.path.append('.')

import numpy as np
from typing import List
from malgo.custom_type import Function, Real, Vector
from malgo.roots.secant import modified_secant
from malgo.ODE.runge_kutta import runge_kutta_4th

def shooting(a: Real, b: Real, alpha_cond: Real, beta_cond: Real, f: Function):
    """Solves the boundary value problem for second-order ODE.
    
    Args:
       a: Initial value of x, also used as startpoint of interval.
       b: Endpoint of interval.
       alpha_cond: Initial alpha condition so that y(a) = alpha_cond
       beta_cond: Initial beta condition so that y(b) = beta_cond
       f: The n-1 th order system if this is an n-th 
            order ODE. It admits the form f(x, y_vec).
    """
    PARTITION_LEN = 2000
    def Phi(u: Real):
        """The function y(b) - beta_cond."""
        _, ys = runge_kutta_4th(
            init_conds=[alpha_cond, u], a=a, b=b, N=PARTITION_LEN, f=f)
        last_ys = ys[-1]
        last_y = last_ys[0]
        return last_y - beta_cond
    
    root = modified_secant(Phi, a, b)
    
    xs, ys = runge_kutta_4th(
        init_conds=[alpha_cond, root], a=a, b=b, N=PARTITION_LEN, f=f)
    
    return xs, ys[:,0]
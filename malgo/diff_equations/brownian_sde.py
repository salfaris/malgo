import sys
sys.path.append('.')

import numpy as np
from typing import List
from malgo.custom_type import Function, Real, Indeterminate, Vector

def brownian(x_init: Real, 
             t_init: Real,
             t_end: Real,
             N: int,
             sigma: Real):
    """
    Solves an SDE using the Euler-Maruyama method.
    
    Args:
        x_init: Initial starting point of stochastic process.
        t_init: Initial time of evolution, expect > 0.
        t_end: Total time of evolution, expect > 0.
        N: Number of subintervals to partition [0, t_end].
        sigma: A real constant value.
    """
    # Initial values of t, ts.
    dt = (t_end-t_init) / float(N)
    ts = np.arange(start=t_init, stop=t_end, step=dt)
    N = ts.size
    
    # Initialize sequence of solution, xs.
    xs = np.zeros(N)
    xs[0] = x_init
    
    # Solve using Euler-Maruyama method.
    for i in range(1, N):
        dW = np.random.normal(loc=0., scale=np.sqrt(dt))
        xs[i] = xs[i-1] + sigma * dW
        
    return ts, xs
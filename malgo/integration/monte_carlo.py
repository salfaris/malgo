# System imports
import sys
sys.path.append('.')

import random
import numpy as np
from malgo.custom_type import Function, Real
from malgo.models import IntegralKernel

def monte_carlo():    
    n = 0
    N = 10000

    for _ in range(N):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        
        if (x**2 + y**2 < 1):
            n += 1

    p1 = n/N
    S1 = p1*2*2
    error = 2*2*np.sqrt(p1*(1-p1))/(np.sqrt(N))

    return S1, error

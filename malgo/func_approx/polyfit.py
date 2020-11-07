# System imports
import os
import sys
sys.path.append('.')
from typing import List
from PIL import Image

# Local imports
from malgo.custom_type import Indeterminate, Function, Real

# Third-party imports
import numpy as np

def find_coeff_ai(m: int, xs: List[Real], ys: List[Real]) -> Function:
    """Find the coefficients, ai, for the polynomial fit.
    
    Args:
        m: Number of coefficients ai we want to find.
        xs: The xi values of the known points to be fitted.
        ys: The yi values of the known points to be fitted.
    
    Remark:
        Note that len(xs), len(ys) can be >= m as per the theory.
    
    Returns:
        A polynomial fit of the data points (xs, ys). 
    """
    # Create a zero (m+1) * (m+1) matrix and a zero (m+1) vector.
    A = np.zeros((m+1, m+1))
    b = np.zeros(m+1)
    for k in range(m+1):
        b[k] = sum(xs**k * ys)
        for i in range(m+1):
            A[k, i] = sum(xs**(k+i))
    
    # Solve the equation Ax = b.
    coefs: List[Real] = np.linalg.solve(A, b)
    
    def polyfit(x: Indeterminate) -> List[Real]:
        monomial_basis: List[Real] = x**np.array(range(m+1))
        return sum(coefs*monomial_basis)
    
    return polyfit
    

# # TEST CASE
# if __name__ == '__main__':
#     xs = np.array([1, 2, 3, 4, 5, 6])
#     ys = np.array([-5.21659, 2.53152, 2.05687, 14.1135, 20.9673, 33.5652])
#     fit = find_coeff_ai(2, xs, ys)
    
#     import matplotlib.pyplot as plt
#     xdense = np.arange(start=0, stop=7, step=0.1)
#     fitlist = [fit(x) for x in xdense]
#     fig, ax = plt.subplots()
#     ax.plot(xs, ys, 'ro')
#     ax.plot(xdense, fitlist)
    
#     path = 'malgo/func_approx/Figures'
#     if not os.path.exists(path):
#         os.makedirs(path)
    
#     image_name = 'polyfit.png'
#     fig.savefig(os.path.join(path, image_name), bbox_inches='tight')
#     Image.open(os.path.join(path, image_name)).show()
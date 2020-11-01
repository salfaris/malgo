import numpy as np
from typing import List

# Define type aliases
Matrix = np.array
Vector = np.array
index = int

def find_maximal(row):
    absrow = [abs(r) for r in row]
    return absrow.index(max(absrow))

def swap(A: Matrix, b: Vector, i: index, j: index):
    """Swaps in-place"""
    A[i], A[j] = A[j], np.array(A[i])
    b[i], b[j] = b[j], b[i]

def gauss(A: Matrix, b: Vector):
    A = A.copy()
    b = b.copy()
    n = len(b)

    # 1. Elimination phase

    # Iterate through all 'pivots'. We iterate up until n-2 because the
    # n-1th line (which is the last line: we counted from zero!) will
    # not be a pivot.
    for j in range(0, n-1):
        # Iterate through all the rows below the j up until n
        # which is the last row (we counted from zero).
        for i in range(j+1, n):
            elim_param = A[i, j] / A[j, j]

            # Update the current i of matrix A and vector b.
            A[i] = A[i] - elim_param * A[j]
            b[i] = b[i] - elim_param * b[j]

    # 2. (Backward) Substitution phase
    x = np.zeros(n)
    for j in range(n-1, -1, -1):
        x[j] = b[j] / A[j, j]
        b = b - x[j] * A[:, j]
    return x

def gaussPivot(A: Matrix, b: Vector):
    A = A.copy()
    b = b.copy()
    n = len(b)

    # 1. Elimination phase

    # Iterate through all 'pivots'. We iterate up until n-2 because the
    # n-1th line (which is the last line: we counted from zero!) will
    # not be a pivot.
    for j in range(0, n-1):
        maximal_row = j + find_maximal(A[j:, j])
        swap(A, b, maximal_row, j)
        # Iterate through all the rows below the j up until n
        # which is the last row (we counted from zero).
        for i in range(j + 1, n):
            elim_param = A[i, j] / A[j, j]

            # Update the current i of matrix A and vector b.
            A[i] = A[i] - elim_param * A[j]
            b[i] = b[i] - elim_param * b[j]

    # 2. (Backward) Substitution phase
    x = np.zeros(n)
    for j in range(n - 1, -1, -1):
        x[j] = b[j] / A[j, j]
        b = b - x[j] * A[:, j]
    return x

A = np.array([
    [0, 1., 1.],
    [1., 5., 4.],
    [5., 4., 1.]
])

b = np.array([3., 23., 16.])

soln = gaussPivot(A, b)
print(soln)
print(f"Original b: {b}")
print("Gaussed b: {}".format(np.dot(A, soln)))

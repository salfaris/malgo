# System imports
import sys
sys.path.append('.')

from malgo.custom_type import Matrix, Vector, List, mat_index
import numpy as np

def gauss(A: Matrix, b: Vector):
    """Executes Gaussian elimination on the augmented matrix [A|b].

    Returns:
      A vector x such that Ax = b.
    """
    n = len(b)
    A, b = A.copy(), b.copy()
    A, b = row_echelon_pivot(A, b)

    # Backward substitution phase
    x = np.zeros(n)
    for j in range(n-1, -1, -1):
        x[j] = b[j] / A[j, j]
        b = b - x[j]*A[:, j]
    return x

def row_echelon_pivot(A: Matrix, b: Vector):
    """Put the augmented matrix [A|b] into 
    row echelon form using the pivot technique.
    """
    n = len(b)
    A, b = A.copy(), b.copy()

    # Iterate through all pivots.
    for j in range(0, n-1):
        
        # <--- Pivot technique applied --->
        leading_entries = A[j:, j]
        idx_maximal_leading_entry = find_maximal_row(leading_entries)
        idx_maximal_row = j + idx_maximal_leading_entry
        swap_two_rows(A, b, idx_maximal_row, j)

        # Kill all the terms below the leading entry of pivot.
        for i in range(j+1, n):
            elim_param = A[i, j] / A[j, j]

            A[i] = A[i] - elim_param * A[j]
            b[i] = b[i] - elim_param * b[j]

    return A, b

def find_maximal_row(mat_column: List[float]):
    """Finds the row (element) with maximal value in `mat_column'
    and returns its index.
    
    Args:
        mat_column: A matrix column, viewed as n * 1 column vector.
    """
    abs_col = [abs(entry) for entry in mat_column]
    max_entry = max(abs_col)
    idx_max_entry = abs_col.index(max_entry)
    return idx_max_entry

def swap_two_rows(A: Matrix, b: Vector, i: mat_index, j: mat_index):
    """Swaps in-place the i-th and j-th row of A and b."""
    A[i], A[j] = A[j].copy(), A[i].copy()
    b[i], b[j] = b[j], b[i]

# def row_echelon(A: Matrix, b: Vector):
#     """Put the augmented matrix [A|b] into row echelon form.
    
#     Args:
#         A: An n*n matrix
#         b: An n*1 vector 

#     Returns:
#         An upper triangular matrix A and an updated vector b
#         such that [A|b] is in row echelon form.
#     """
#     n = len(b)
#     A, b = A.copy(), b.copy()

#     # 1. Elimination phase

#     # Iterate through all 'pivots'. We iterate up until n-2 because the
#     # n-1th line (which is the last line: we counted from zero!) will
#     # not be a pivot.
#     for j in range(0, n-1):
        
#         # Kill all the terms below the leading entry of pivot.
#         # Iterate through all the rows below the j up until n
#         # which is the last row (we counted from zero).
#         for i in range(j+1, n):
#             elim_param = A[i, j] / A[j, j]

#             A[i] = A[i] - elim_param * A[j]
#             b[i] = b[i] - elim_param * b[j]

#     return A, b


# # TEST CASE
# if __name__ == '__main__':
#     A = np.array([
#         [0, 2., 2.],
#         [4., -1., 3.],
#         [5., 4., 1.]
#     ])

#     b = np.array([3., 23., 16.])

#     print(A[2:, 2])
    
#     soln = gauss(A, b)
#     print(f"Our solution: {soln}")
#     print(f"Numpy solution: {np.linalg.solve(A, b)}")
#     print()
#     print(f"Original b: {b}")
#     print("Gaussed b: {}".format(np.dot(A, soln)))
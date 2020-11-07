import numpy as np
from typing import Callable, List, TypeVar

# Local type aliases
KernelMethod = Callable

# General type aliases
Indeterminate = float

# Numerical type aliases
pt_index = int

# Analysis type aliases
Function = Callable
Real = TypeVar('Real', int, float)

# Linear Algebra type aliases
Matrix = np.array
Vector = np.array
mat_index = int
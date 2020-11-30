import sys
sys.path.append('.')

import numpy as np
from malgo.custom_type import Matrix

def relaxation(init_config: Matrix):
    """Solves the Laplace equation in two variables using
    the relaxation method.
    
    Args:
        init_config: The initial discretised configuration.
    """
    res = init_config.copy()
    sizex, sizey = res.shape
    for x in range(1, sizex-1):
        for y in range(1, sizey-1):
            res[x, y] = (init_config[x+1, y] 
                        + init_config[x-1, y]
                        + init_config[x, y+1]
                        + init_config[x, y-1])
            res[x, y] /= 4
    return res

# if __name__ == "__main__":
#     init_mat = np.full(shape=(14, 16), fill_value=20.)

#     for i in range(1, 5):
#         init_mat[0, i] = 10.
#     for i in range(6, 9):
#         init_mat[init_mat.shape[0]-1,13-i] = 5.
        
#     for _ in range(12):
#         init_mat = relaxation(init_mat)
#         plt.matshow(init_mat)
#         plt.colorbar()
from forma_optima import *
import numpy as np
matrix = np.array([
    [0, 16, 45, 32],
    [16, 0, 18, 21],
    [45, 18, 0, 7],
    [32, 21, 7, 0]
])

result = min_span_tree(matrix)
print(result)
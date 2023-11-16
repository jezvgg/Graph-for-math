import numpy as np
from itertools import permutations

matrix = np.array([
    [0,1,1,0,1,1],
    [1,0,0,1,1,1],
    [1,0,0,1,1,1],
    [0,1,1,0,1,1],
    [1,1,1,1,0,0],
    [1,1,1,1,0,0]
])

our_matrix = np.array([
    [0,1,1,0,1,1],
    [1,0,1,1,0,1],
    [1,1,0,1,1,0],
    [0,1,1,0,1,1],
    [1,0,1,1,0,1],
    [1,1,0,1,1,1]
])

for combo in permutations(range(6)):
    new_matrix = matrix[list(combo)]
    new_matrix = new_matrix[:, list(combo)]
    if np.array_equal(our_matrix, new_matrix):
        print(combo)
        print(new_matrix)
        print(our_matrix)
        break
else:
    print("Matrix not isometric")
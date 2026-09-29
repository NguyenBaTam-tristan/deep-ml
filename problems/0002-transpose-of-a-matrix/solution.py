import numpy as np
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    if not a: return []
    rows = len(a) # 2: 0, 1
    cols = len(a[0]) # 3: 0 1 2 

    transpose = []
    for i in range(cols):
        new_rows = []
        for j in range(rows):
            new_rows.append(a[j][i])
        transpose.append(new_rows)
    return transpose


import numpy as np

def cross_product(a, b):
    # Your code here
    a_arr = np.array(a)
    b_arr = np.array(b)
    cross_product = np.cross(a_arr, b_arr)
    return cross_product
import numpy as np

def k_nearest_neighbors(points, query_point, k):
    """
    Find k nearest neighbors to a query point
    
    Args:
        points: List of tuples representing points [(x1, y1), (x2, y2), ...]
        query_point: Tuple representing query point (x, y)
        k: Number of nearest neighbors to return
    
    Returns:
        List of k nearest neighbor points as tuples
        When distances are tied, points appearing earlier in the input list come first.
    """
    my_list = []
    for p in points:
        distance = (p[0]-query_point[0])**2 + (p[1]-query_point[1])**2
        my_list.append([distance, p])
    my_list.sort()

    result = []
    for i in range(k):
        chosen = my_list[i][1]
        result.append(chosen)
    return result

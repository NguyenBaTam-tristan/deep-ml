import numpy as np

def k_nearest_neighbors(points, query_point, k):
    all_points = []
    for p in points:
        distance = sum((a-b)**2 for a, b in zip(p, query_point))
        all_points.append([distance, p])
    all_points.sort(key = lambda x: x[0])
    result = []
    for i in range(k):
        chosen = all_points[i][1]
        result.append(chosen)
    return result













   
    

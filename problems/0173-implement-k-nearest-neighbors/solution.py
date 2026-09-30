import numpy as np

def k_nearest_neighbors(points, query_point, k):
    all_points = []
    for p in points:
        distance = (p[0]-query_point[0])**2 + (p[1]-query_point[1])**2
        all_points.append([distance, p])
    all_points.sort(key = lambda item: item[0])
    result = []
    for i in range(k):
        chosen = all_points[i][1]
        result.append(chosen)
    return result







   
    

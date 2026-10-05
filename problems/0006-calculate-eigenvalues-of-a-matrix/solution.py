import numpy as np
import math
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	arr = np.array(matrix, dtype = float)
	det = np.linalg.det(arr)
	trace = np.trace(arr)
	delta = trace ** 2 - 4*det
	if delta < 0: return []
	elif delta == 0:
		return [trace/2, trace/2]
	else:
		x1 = (trace + math.sqrt(trace**2 - 4*det)) / 2
		x2 = (trace - math.sqrt(trace**2 - 4*det)) / 2
		return [x1, x2]

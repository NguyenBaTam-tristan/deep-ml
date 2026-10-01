import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	def invertible(X):
		if len(X) == len(X[0]):
			det_X = np.linalg.det(X)
			if det_X != 0: return True  
			return False
		return False
	if invertible(T) and invertible(S):
		transformed_matrix = np.linalg.inv(T) @ A @ S
		return transformed_matrix
	return -1
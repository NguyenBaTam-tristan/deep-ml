import numpy as np
def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
	mat_B = np.array(B, dtype = float)
	mat_C = np.array(C, dtype = float)
	P = np.linalg.inv(mat_C) @ mat_B
	return P
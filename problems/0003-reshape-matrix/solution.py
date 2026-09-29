import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	if not a:
		return []
	A = np.array(a)
	if A.size != new_shape[0] * new_shape[1]:
		return []
	return np.reshape(A, new_shape).tolist()
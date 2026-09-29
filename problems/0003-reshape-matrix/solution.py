import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	if not a: 
		return []
	A = np.array(a)
	if len(A) == new_shape[0] and len(A[0]) == new_shape[1]:
		return A
	elif len(A) != new_shape[1] or len(A[0]) != new_shape[0]:
		return []
	new_matrix = np.reshape(A, (new_shape[0], new_shape[1]))
	return new_matrix

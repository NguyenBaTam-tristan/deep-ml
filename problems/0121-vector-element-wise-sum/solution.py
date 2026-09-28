import numpy as np
def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	# Return the element-wise sum of vectors 'a' and 'b'.
	# If vectors have different lengths, return -1.
	if len(a) != len(b):
		return -1
	arr_a = np.array(a)
	arr_b = np.array(b)

	sum_arr = (arr_a+arr_b).tolist()
	return sum_arr

def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	if not a or not b or not a[0]:
		return -1
	elif len(a[0]) != len(b):
		return -1
	result = []
	for i in range(len(a)):
		sum_num = 0
		for j in range(len(b)):
			sum_num += a[i][j] * b[j]
		result.append(sum_num)
	return result



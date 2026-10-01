def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	result = []
	for i in range(len(matrix)):
		result.append([num * scalar for num in matrix[i]])
	return result

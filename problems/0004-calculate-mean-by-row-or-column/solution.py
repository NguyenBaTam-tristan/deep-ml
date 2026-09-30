def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if not matrix or not matrix[0]:
		return []
	elif mode == 'row':
		means = []
		for row in matrix:
			means.append(sum(row)/len(row))
		return means
	elif mode == 'column':
		means = []
		for col in range(len(matrix[0])):
			sum_col = 0
			for row in range(len(matrix)):
				sum_col += matrix[row][col]
			means.append(sum_col/len(matrix))
		return means
	raise ValueError('Invalid')
			





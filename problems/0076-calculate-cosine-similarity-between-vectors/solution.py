import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	u = np.array(v1)
	v = np.array(v2)
	numerator = u @ v
	denominator = np.sqrt(np.sum(u**2)) * np.sqrt(np.sum(v**2))
	result = numerator / denominator
	return result

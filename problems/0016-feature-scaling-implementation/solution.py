import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	mean = np.mean(data, axis = 0)
	std = np.std(data, axis = 0)
	standardized = (data - mean) / std

	min_val = np.min(data, axis = 0)
	max_val = np.max(data, axis = 0)
	normalized = (data - min_val) / (max_val - min_val)

	return np.round(standardized, 4), np.round(normalized, 4)

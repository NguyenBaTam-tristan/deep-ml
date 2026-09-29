import numpy as np

def to_categorical(x, n_col=None):
	if n_col is None:
		n_col = np.max(x) + 1
	matrix = np.zeros((len(x), n_col))
	matrix[np.arange(len(x)), x] = 1.0
	return matrix
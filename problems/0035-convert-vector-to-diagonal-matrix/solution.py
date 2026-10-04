import numpy as np

def make_diagonal(x):
	# Your code here
	zeros = np.zeros((len(x), len(x)))
	for i in range(len(x)):
		zeros[i][i] = x[i]
		
	return zeros

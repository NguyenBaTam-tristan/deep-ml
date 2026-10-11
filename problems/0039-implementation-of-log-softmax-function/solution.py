import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	# Your code here
	shifted_scores = scores - np.max(scores)
	return shifted_scores - np.log(np.sum(np.exp(shifted_scores)))
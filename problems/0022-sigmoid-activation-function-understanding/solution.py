import math

def sigmoid(z: float) -> float:
	#Your code here
	sigmoid = 1 / (1 + math.exp(-z))
	return sigmoid
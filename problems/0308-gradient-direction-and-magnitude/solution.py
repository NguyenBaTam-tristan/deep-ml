import numpy as np
import math
def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	# Your code here
	magnitude = math.sqrt(sum(x**2 for x in gradient))
	if magnitude == 0:
		ascent_dir = [0 for _ in gradient]
		descent_dir = [0 for _ in gradient]
	else:
		ascent_dir = [x/magnitude for x in gradient]
		descent_dir = [-x for x in ascent_dir]
	return {'magnitude': magnitude, 'direction': ascent_dir, 'descent_direction': descent_dir}
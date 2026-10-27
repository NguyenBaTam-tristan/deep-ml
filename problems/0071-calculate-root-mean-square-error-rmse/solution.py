
import numpy as np

def rmse(y_true, y_pred):
	# Write your code here
	y_true_arr = np.array(y_true)
	y_pred_arr = np.array(y_pred)
	rmse_res = np.sqrt(np.mean((y_true_arr-y_pred_arr) ** 2))
	return round(rmse_res,3)

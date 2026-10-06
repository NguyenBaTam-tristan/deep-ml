def calculate_f1_score(y_true, y_pred):
	"""
	Calculate the F1 score based on true and predicted labels.

	Args:
		y_true (list): True labels (ground truth).
		y_pred (list): Predicted labels.

	Returns:
		float: The F1 score rounded to three decimal places.
	"""
	# Your code here
	TP = 0
	FP = 0
	TN = 0
	FN = 0
	
	for i in range(len(y_true)):
		if y_true[i] == 1 and y_pred[i] == 1:
			TP += 1
		elif y_true[i] == 1 and y_pred[i] == 0:
			FN += 1
		elif y_true[i] == 0 and y_pred[i] == 0:
			TN += 1
		else:
			FP += 1
	if TP + FN == 0 or TP + FP == 0: return 0.0
	recall = TP/(TP+FN)
	precision = TP/(TP+FP)
	f1 = 2 * (precision * recall) / (precision + recall)
	return round(f1,3)
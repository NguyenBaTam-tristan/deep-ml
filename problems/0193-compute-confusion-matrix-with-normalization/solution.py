import numpy as np

def compute_confusion_matrix(y_true, y_pred, num_classes, normalize=None, round_decimals=4):
    """
    Compute a KxK confusion matrix with optional normalization.

    Args:
        y_true: Iterable of true labels in [0, K-1]
        y_pred: Iterable of predicted labels in [0, K-1]
        num_classes: K, number of classes
        normalize: None | 'true' | 'pred' | 'all'
        round_decimals: decimals to round when normalization is applied

    Returns:
        list[list[int|float]] confusion matrix
    """
    # Your implementation here
    cm = np.zeros((num_classes, num_classes), dtype=float)
    for t, p in zip(y_true, y_pred):
        cm[t, p] += 1
    if normalize == 'true':
        row_sums = cm.sum(axis = 1, keepdims = True)
        cm = np.divide(cm, row_sums, out = np.zeros_like(cm), where = row_sums != 0)
    elif normalize == 'pred':
        col_sums = cm.sum(axis = 0, keepdims = True)
        cm = np.divide(cm, col_sums, out = np.zeros_like(cm), where = col_sums != 0)
    elif normalize == 'all':
        total = cm.sum()
        if total != 0:
            cm = cm/total
    
    return np.round(cm, round_decimals).tolist()
    


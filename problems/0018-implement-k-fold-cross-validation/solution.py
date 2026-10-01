import numpy as np
from typing import List, Tuple

def k_fold_cross_validation(n_samples: int, k: int = 5, shuffle: bool = True) -> List[Tuple[List[int], List[int]]]:
    """
    Generate train/test index splits for k-fold cross-validation.
    
    Args:
        n_samples: Total number of samples in the dataset
        k: Number of folds (default 5)
        shuffle: Whether to shuffle indices before splitting (default True)
    
    Returns:
        List of (train_indices, test_indices) tuples
    """
    # Your code here
    # split n_samples into an array of numbers
    indices = np.arange(n_samples)
    # shuffle
    if shuffle:
        np.random.shuffle(indices)
    # calculate fold_sizes
    base_size = n_samples // k 
    remainder = n_samples % k 
    fold_sizes = []
    for i in range(k):
        if i < remainder:
            fold_sizes.append(base_size + 1)
        fold_sizes.append(base_size)
    # calculate where to cut the array of n_samples
    split_indices = np.cumsum(fold_sizes)[:-1]
    # split the folds at where to cut
    folds = np.split(indices, split_indices)
    # create a loop to determine test set and merge the remaining set as train test then return the result 
    result = []
    for i in range(k):
        test_indices = folds[i].tolist()
        train_folds = []
        for j in range(k):
            if j != i:
                train_folds.append(folds[j])
        train_indices = np.concatenate(train_folds).tolist()
        result.append((train_indices, test_indices))
    return result 






    
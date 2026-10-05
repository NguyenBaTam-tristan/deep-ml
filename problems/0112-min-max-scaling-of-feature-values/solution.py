def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    
    Args:
        x: A list of numerical values
    
    Returns:
        A new list with values normalized to [0, 1]
    """
    # Your code here
    result = []
    for num in x:
        min_max_scale = (num - min(x)) / (max(x) - min(x))
        result.append(min_max_scale)
    return result 
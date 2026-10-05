from collections import Counter
def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    if not samples: 
        return []
    count = Counter(samples)
    result = []
    for num, freq in count.items():
        result.append((num, freq/len(samples)))
    return result


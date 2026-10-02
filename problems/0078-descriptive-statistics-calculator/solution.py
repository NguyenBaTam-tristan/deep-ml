import numpy as np
from collections import Counter

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    # Your code here
    result = {}
    def find_mean(data):   
        return sum(data) / len(data)

    def find_median(data):   
        if len(sorted(data)) % 2 == 0: 
            return (sorted(data)[len(data) // 2 - 1] + sorted(data)[len(data) // 2]) / 2
        return sorted(data)[len(data) // 2]
    
    def find_mode(data):
        if not data: return None
        counts = Counter(data)
        max_freq = max(counts.values())
        mode = [num for num, freq in counts.items() if freq == max_freq]
        return mode[0]
    
    def find_variance(data):
        up = 0
        for i in range(len(data)):
            up += (data[i] - find_mean(data)) ** 2
        down = len(data)
        variance = up / down
        return variance 

    def percentile(data):
        p25 = np.percentile(data, 25)
        p50 = np.percentile(data, 50)
        p75 = np.percentile(data, 75)
        return p25, p50, p75

    def interquartile_range(data):
        p25 = np.percentile(data, 25)
        p75 = np.percentile(data, 75)
        return p75 - p25

    p25, p50, p75 = percentile(data)
    variance_val = find_variance(data)

    result['mean'] = round(float(find_mean(data)), 4)
    result['median'] = round(float(find_median(data)), 4)
    result['mode'] = find_mode(data)
    result['variance'] = round(float(variance_val), 4)
    result['standard_deviation'] = round(float(variance_val ** 0.5), 4)
    result['25th_percentile'] = round(float(p25), 4)
    result['50th_percentile'] = round(float(p50), 4)
    result['75th_percentile'] = round(float(p75), 4)
    result['interquartile_range'] = round(float(interquartile_range(data)), 4)

    return result



        
        

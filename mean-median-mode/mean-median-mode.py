from collections import Counter
import numpy as np
import statistics as stats
def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    x=np.array(x)
    return {"mean":float(np.mean(x)),"median":float(np.median(x)),"mode":float(stats.mode(x))}
    pass
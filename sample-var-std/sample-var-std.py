import numpy as np
import statistics as stats
def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    x=np.array(x)
    return {"variance":float(np.var(x,ddof=1)),"standard_deviation":float(np.std(x,ddof=1))}
    pass
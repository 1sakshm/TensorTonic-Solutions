import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    # Write code here
    X=np.array(X)
    return np.atleast_2d(np.cov(X,rowvar=False))
    pass
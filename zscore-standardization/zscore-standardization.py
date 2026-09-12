import numpy as np

def zscore_standardize(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    """
    Returns population Z-scores as a NumPy array matching the shape of X.
    """
    # Write code here
    c=np.array(X)
    mean=np.mean(c,axis=axis,keepdims=True)
    std=np.std(c,axis=axis,keepdims=True)
    z=(c-mean)/np.maximum(std,eps)
    return z
    pass
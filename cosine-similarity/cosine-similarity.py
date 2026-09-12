import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    a=np.array(a)
    b=np.array(b)
    dot=np.dot(a,b)
    a1=np.linalg.norm(a)
    b1=np.linalg.norm(b)
    return float(np.nan_to_num(dot/(a1*b1)))
    # Write code here
    return np.cos(a,b)
    pass
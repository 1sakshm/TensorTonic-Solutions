import math
from scipy.stats import binom
def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Write code here
    return {"pmf":float(binom.pmf(k,n,p)),"cdf":float(binom.cdf(k,n,p))}
    pass
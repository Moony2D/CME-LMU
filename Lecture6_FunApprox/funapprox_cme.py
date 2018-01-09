import numpy as np
import scipy.optimize
import scipy.linalg

def chebnodes(m):
    """ 
    Computes m Chebyshev nodes between -1 and 1.
    """
    i = np.array(list(range(1, m+1)))
    return -np.cos(0.5 * np.pi * (2 * i - 1) / m)

def chebgrid(a, b, m):
    """ 
    Computes num Chebyshev nodes on the interval [a,b].
    """
    z = chebnodes(m)
    return (b - a) * 0.5 * (z + 1) + a 

def chebconvert(x, a, b):
    """
    Transforms nodes between [a,b] to the interval [-1,1].
    """
    return 2. * (x - a) / (b - a) - 1


def chebmatrix(deg, m = None, x = None):
    """
    Computes the m-by-(deg+1) matrix with Chebyshev basis functions of degree deg for m Chebyshev nodes.
    """
    ## check if a second argument is provided
    assert (m != None or np.sum(x) != None), "Please provide the number of grid points or an input vector/scalar x!"
    
    ## check if x values are provided
    if x is None: # default: Chebyshev nodes between -1 and 1 (for interpolation/regression) 
        z = chebnodes(m)
    elif isinstance(x, (list, tuple, np.ndarray)):    # arbitrary vector (for approximation)
        z, m  = x, len(x) 
    else:    # arbitrary scalar (for approximation)
        z, m = x, 1 

    ## define numpy array and fill second column     
    T = np.ones((m, deg + 1))
    T[:,1] = z
    
    ## loop over columns in T; each column corresponds to the Chebyshev basis functions for deg col_idx
    for col_idx in range(1, deg):
        T[:,col_idx+1] = 2 * z * T[:,col_idx] - T[:,col_idx - 1]
    return T

def chebapprox(y, deg, v = None):
    """
    Function to compute the Chebyshev coefficients using interpolation or regression
    """
    m = len(y)
    if v == None:
        T = chebmatrix(deg, m)
    else:
        z = convert(v[0], v[1], v[2]) 
        T = chebmatrix(deg, x = z)

    
    if deg == m-1: # interpolation (default)
        coef = np.linalg.solve(T,y)
    else:
        coef = np.ones(deg + 1)
        for idx_deg in range(deg + 1):
            coef[idx_deg] = sum(y * T[:,idx_deg]) / sum(T[:,idx_deg]**2)
            
    return coef 
import numpy as np

def B(eps):
    norm_eps = np.linalg.norm(eps)
    skew_eps = np.array([[0, -eps[2], eps[1]], [eps[2], 0, -eps[0]], [-eps[1], eps[0], 0]], np.float64)
    alpha = (norm_eps/2)/np.tan(norm_eps/2)
    return np.eye(3) + skew_eps/2 + ((1-alpha)/(norm_eps**2)) * (skew_eps@skew_eps)

def hat(w):
    assert w.shape[0] == 3, "It is not a 3D vector."
    return np.array([[0., -w[2], w[1]], [w[3], 0., -w[0]], [-w[1], w[0], 0]], np.float64)

def vee(W):
    assert W.shape == (3,3), "It is not a 3x3 matrix."
    return np.array([W[2,1], W[0,2], W[1,0]], np.float64)
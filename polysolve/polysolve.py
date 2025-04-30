import numpy as np

CBRT_UNITY_IM = np.sqrt(3)/2 * 1j


def quadratic_solve(a: float, b: float, c: float) -> tuple[float, float]:
    '''
    Solves the roots of a quadratic equation.
    Uses the quadratic formula. 
    
    Examples
    --------
    >>> quadratic_solve(1., 0., 0.)
    (0.0, -0.0)
    >>> quadratic_solve(3., 0., -1.)
    (0.5773502691896257, -0.5773502691896257)

    '''

    det = b**2 - (4*a*c)


    return ((-b + np.sqrt(det)) / (2*a),
            (-b - np.sqrt(det)) / (2*a))

def cubic_solve(a, b, c, d):
    q = (3*a*c - b**2) / (9*a**2)
    r = (9*a*b*c - 27*a**2*d - 2*b**3) / (54*a**3)

    s = np.cbrt(r + np.sqrt(q**3 + r**2))
    t = np.cbrt(r - np.sqrt(q**3 + r**2))

    x1 = s + t - (b/3*a)
    x2 = -(s + t)/2 - (b/3*a) + CBRT_UNITY_IM * (s - t)
    x3 = -(s + t)/2 - (b/3*a) - CBRT_UNITY_IM * (s - t)
    return x1, x2, x3

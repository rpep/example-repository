import math

import numpy as np

x = np.array([2.0, 3.0, 5.0])

def potential(r):
    R = np.linalg.norm(r)

    return 1 / R


print("potential(x) = ", potential(x))




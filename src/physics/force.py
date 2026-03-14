import numpy as np

def acceleration(px, py, q, x, y, Ex, Ey):

    ix = np.argmin(abs(x - px))
    iy = np.argmin(abs(y - py))

    Ex_local = Ex[iy][ix]
    Ey_local = Ey[iy][ix]

    ax = q * Ex_local
    ay = q * Ey_local

    return ax, ay

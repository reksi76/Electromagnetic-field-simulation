import numpy as np

def acceleration(state, field, grid, q):

    ix = np.argmin(abs(grid.x - state.x))
    iy = np.argmin(abs(grid.y - state.y))

    Ex_local = field.Ex[iy, ix]
    Ey_local = field.Ey[iy, ix]

    ax = q * Ex_local
    ay = q * Ey_local

    return ax, ay

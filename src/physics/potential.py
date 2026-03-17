import numpy as np 

def electrical_potential(field, charges, k, grid):
    V_total = np.zeros_like(grid.X)

    for charge in charges:
        q = charge['q']
        x0, y0 = charge['pos']

        dx = grid.X - x0
        dy = grid.Y - y0

        r = np.sqrt(dx**2 + dy**2 + field.epsilon**2)
        V_total += k * q / r

    return V_total

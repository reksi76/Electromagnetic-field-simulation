import numpy as np 

def electrical_potential(epsilon, charges, k, X, Y):
    V_total = np.zeros_like(X)

    for charge in charges:
        q = charge['q']
        x0, y0 = charge['pos']

        dx = X - x0
        dy = Y - y0

        r = np.sqrt(dx**2 + dy**2 + epsilon**2)
        V_total += k * q / r

    return V_total

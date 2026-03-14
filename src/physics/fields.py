import numpy as np 

def setup_grid(xmin=-5, xmax=5, n=400):
    k = 1.0
    x = np.linspace(xmin, xmax, n)
    y = np.linspace(xmin, xmax, n)

    X, Y = np.meshgrid(x, y)

    return k, x, y, X, Y 

def electric_field(charges, k, X, Y):
    Ex = np.zeros_like(X)
    Ey = np.zeros_like(Y)

    for charge in charges:
        q = charge['q']
        x0, y0 = charge['pos']

        dx = X - x0
        dy = Y - y0

        epsilon = 0.2
        r = np.sqrt(dx**2 + dy**2 + epsilon**2)
        Ex += (k * q * dx) / r**3
        Ey += (k * q * dy) / r**3

    return Ex, Ey, epsilon



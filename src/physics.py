import matplotlib.pyplot as plt 
import numpy as np 

def setup_charges():
    charges = [
            {'q': -1.0, 'pos': (-1.0, 0)},
            {'q' : 1.0, 'pos': (1.0, 0)}
            ]

    return charges

def setup_grid(xmin=-5, xmax=5, n=400):
    k = 1.0

    x = np.linspace(xmin, xmax, n)
    y = np.linspace(xmin, xmax, n)

    X, Y = np.meshgrid(x, y)

    return k, x, y, X, Y

# Electrical Field
def electrical_field(charges, k, X, Y):
    Ex = np.zeros_like(X)
    Ey = np.zeros_like(Y)

    for charge in charges:
        q = charge['q']
        x0, y0 = charge['pos']

        dx = X - x0
        dy = Y - y0

        epsilon = 0.2
        r  = np.sqrt(dx**2 + dy**2 + epsilon**2) 

        Ex += (k * q * dx) / r**3
        Ey += (k * q * dy) / r**3

    return  Ex, Ey

def electrical_potential(charges, k, X, Y):
    V_total = np.zeros_like(X)

    for charge in charges:
        q = charge['q']
        x0, y0 = charge['pos']

        dx = X - x0
        dy = Y - y0
        
        epsilon = 0.2
        r = np.sqrt(dx**2 + dy**2 + epsilon**2)
        V_total += k * q / r 

    return V_total

def particle_sim(x, y, Ex, Ey):
    dt = 0.01
    px, py = -4, 2 
    px_list = []
    py_list = []
    vx = 0 
    vy = 0 

    for t in range(5000):
        ix = np.argmin(abs(x - px))
        iy = np.argmin(abs(y - py))

        Ex_local = Ex[iy][ix]
        Ey_local = Ey[iy][ix]
        
        k = 1.0
        m = 1.0

        # F = q * E and a = F / m, if m = 1, a = F*E
        ax = Ex_local
        ay = Ey_local

        vx += ax * dt
        vy += ay * dt

        px += vx * dt 
        py += vy * dt

        px_list.append(px)
        py_list.append(py)

    return px_list, py_list





      

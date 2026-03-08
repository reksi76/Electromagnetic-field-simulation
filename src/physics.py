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

def acceleration(px, py, q, x, y, Ex, Ey):
    ix = np.argmin(abs(x - px))
    iy = np.argmin(abs(y - py))
    Ex_local = Ex[iy][ix]
    Ey_local = Ey[iy][ix]
    
    ax = q * Ex_local 
    ay = q * Ey_local

def particle_sim(x, y, Ex, Ey, q):
    dt = 0.02
    px, py = -4, 2 
    vx, vy = 0, 0
    px_list = []
    py_list = []

    # Runge-Kutta 4 (RK4) Numerical method
    for t in range(5000):
        # k1
        ax1, ax2 = acceleration(px, py, x, y, Ex, Ey)
        k1_vx, k1_vy = ax1 * dt, ax2 * dt
        k1_px, k1_py = vx * dt, vy * dt

        # k2
        ax2, ay2 = acceleration(px + 0.5 * k1_px, py + 0.5 * k1_py, x, y, Ex, Ey)
        k2_vx, k2_vy = ax2 * dt, ax2 * dt
        k2_px, k2_py = (v + 0.5 * k1_vx) * dt, (v+ 0.5 * k1_vy)

        # k3
        ax3, ax3 = acceleration(px + 0.5 * k2_px, py + 0.5 * k2_py, x, y, Ex, Ey)
        k3_vx, k2_vy = ax3 * dt, ay3 * dt
        k3_px, k3_py = (v + 0.5 * k2_vx) * dt, (v + 0.5 * k2_vy) * dt

        # k4
        ax4, ay4 = acceleration(px + k3_px, px + k3_py, x, y, Ex, Ey) 
        k4_vx, k4_vy = ax4 * dt, ay4 * dt
        k4_px, k4_py = (v + k3_vx) * dt, (v+ k3_py)

        vx += 1/6 * (k1_vx + 2 * k2_vx + 2 * k3_vx + k4_vx)
        vy += 1/6 * (k1_vy + 2 * k2_vy + 2 * k3_vy + k4_vy)
        px += 1/6 * (k1_px + 2 * k2_px + 2 * k3_px + k4_px)
        py += 1/6 * (k1_py + 2 * k2_py + 2 * k3_py + k4_py)


        
    return px_list, py_list





       

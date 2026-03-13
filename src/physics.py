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

    return  Ex, Ey, epsilon

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

def acceleration(px, py, q, x, y, Ex, Ey):
    ix = np.argmin(abs(x - px))
    iy = np.argmin(abs(y - py))
    Ex_local = Ex[iy][ix]
    Ey_local = Ey[iy][ix]
    
    ax = q * Ex_local 
    ay = q * Ey_local
    return ax, ay

def particle_sim(x, y, Ex, Ey, q):
    dt = 0.1
    px, py = -4, 2 
    vx, vy = 0, 0
    px_list = []
    py_list = []
    vx_list = []
    vy_list = []

    # Runge-Kutta 4 (RK4) Numerical method
    for t in range(3000):
        # k1
        ax1, ay1 = acceleration(px, py, q, x, y, Ex, Ey)
        k1_vx, k1_vy = ax1 * dt, ay1 * dt
        k1_px, k1_py = vx * dt, vy * dt

        # k2
        ax2, ay2 = acceleration(px + 0.5 * k1_px, py + 0.5 * k1_py, q, x, y, Ex, Ey)
        k2_vx, k2_vy = ax2 * dt, ay2 * dt
        k2_px, k2_py = (vx + 0.5 * k1_vx) * dt, (vy + 0.5 * k1_vy) * dt

        # k3
        ax3, ay3 = acceleration(px + 0.5 * k2_px, py + 0.5 * k2_py, q, x, y, Ex, Ey)
        k3_vx, k3_vy = ax3 * dt, ay3 * dt
        k3_px, k3_py = (vx + 0.5 * k2_vx) * dt, (vy + 0.5 * k2_vy) * dt

        # k4
        ax4, ay4 = acceleration(px + k3_px, py + k3_py, q, x, y, Ex, Ey) 
        k4_vx, k4_vy = ax4 * dt, ay4 * dt
        k4_px, k4_py = (vx + k3_vx) * dt, (vy + k3_vy) * dt

        vx += 1/6 * (k1_vx + 2 * k2_vx + 2 * k3_vx + k4_vx)
        vy += 1/6 * (k1_vy + 2 * k2_vy + 2 * k3_vy + k4_vy)
        px += 1/6 * (k1_px + 2 * k2_px + 2 * k3_px + k4_px)
        py += 1/6 * (k1_py + 2 * k2_py + 2 * k3_py + k4_py)
        
        px_list.append(px)
        py_list.append(py)
        vx_list.append(vx)
        vy_list.append(vy)
        
    return px_list, py_list, vx_list, vy_list

# Energy calculation (E = 1/2 * m * v^2 + q * V)
def particle_energy(epsilon, charges, k, px_list, py_list, vx_list, vy_list, q):
    energy_list = []

    for px, py, vx, vy in zip(px_list, py_list, vx_list, vy_list):
        RE = 0.5 * (vx**2 + vy**2)
        V = 0 

        for charge in charges:
            q_source = charge['q']
            x0, y0 = charge['pos']

            dx = px - x0 
            dy = py - y0

            r = np.sqrt(dx**2 + dy**2 + epsilon**2)
            V += (k * q_source)/r 

        PE = q * V

        energy_list.append(RE + PE)

    return energy_list




       

import numpy as np 


def rk4_step(x, y, Ex, Ey, q, charges, k, epsilon):
    # K1
    ax1, ay1 = acceleration(px, py, q, x, y, Ex, Ey)
    k1_vx, k1_vy = ax1 * dt, ay1 * dt
    k1_px, k1_py = vx * dt, vy * dt

    # K2
    ax2, ay2 = acceleration(px + 0.5 * k1_px, py + 0.5 * k1_py, x, y, Ex, Ey)
    k2_vx, k2_vy = ax2 * dt, ay2 * dt
    k2_px, k2_py = (vx + 0.5 * k1_px) * dt, (vy + 0.5 * k1_py) * dt

    # K3
    ax3, ay3 = acceleration(px + 0.5 * k2_px, py + 0.5 * k2_py, x, y, Ex, Ey)
    k3_vx, k3_vy = ax3 ** dt, ay3**dt
    k3_px, k3_py = (vx + 0.5 * k2_vx) * dt, (vy + 0.5 * k2_vy) * dt

    # K4
    ax4, ay4 = acceleration(px + k3_px, py + k3_py, x, y, Ex, Ey)
    k4_vx, k4_vy = ax4 * dt, ay4 * dt
    k4_px, k4_py = (vx + K3) * dt, (vy + K3) * dt

    px += 1/6 * (k1_px + 2 * k2_px + 2 * k3_px + k4_px)
    py += 1/6 * (k1_py + 2 * k2_py + 2 * k3_py + k4_py)
    vx += 1/6 * (k1_vx + 2 * k2_vx + 2 * k3_vx + k4_vx)
    vy += 1/6 * (k1_vy + 2 * k2_vy + 2 * k3_vy + k4_vy)
        
    px_list[t] = px 
    py_list[t] = py
    vx_list[t] = vx
    vy_list[t] = vy

    return px_list, py_list, vx_list, vy_list





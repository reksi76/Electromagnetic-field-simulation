# Integrators for the particle simulation

def euler_step(px, py, vx, vy, dt, acceleration):
    ax, ay = acceleration(px, py)

    vx_new = vx + ax * dt
    vy_new = vy + ay * dt

    px_new = px + vx * dt
    py_new = py + vy * dt

    return px_new, py_new, vx_new, vy_new

def rk4_step(px, py, vx, vy, dt, accel_func):
    # K1
    ax1, ay1 = accel_func(px, py)
    k1_vx, k1_vy = ax1 * dt, ay1 * dt
    k1_px, k1_py = vx * dt, vy * dt 

    # K2
    ax2, ay2 = accel_func(px + 0.5 * k1_px, py + 0.5 * k1_py)
    k2_vx, k2_vy = ax2 * dt, ay2 * dt
    k2_px, k2_py = (vx + 0.5 * k1_vx) * dt, (vy + 0.5 * k1_vy) * dt

    # K3
    ax3, ay3 = accel_func(px + 0.5 * k2_px, py + 0.5 * k2_py)
    k3_vx, k3_vy = ax3 * dt, ay3 * dt
    k3_px, k3_py = (vx + 0.5 * k2_vx) * dt, (vy + 0.5 * k2_vy) * dt

    # K4
    ax4, ay4 = accel_func(px + k3_px, py + k3_py)
    k4_vx, k4_vy = ax4 * dt, ay4 * dt
    k4_px, k4_py = (vx + k3_vx) * dt, (vy + k3_vy) * dt

    px += 1/6 * (k1_px + 2 * k2_px + 2 * k3_px + k4_px)
    py += 1/6 * (k1_py + 2 * k2_py + 2 * k3_py + k4_py)
    vx += 1/6 * (k1_vx + 2 * k2_vx + 2 * k3_vx + k4_vx)
    vy += 1/6 * (k1_vy + 2 * k2_vy + 2 * k3_vy + k4_vy)

    return px, py, vx, vy

def velocity_verlet_step(px, py, vx, vy, dt, acceleration):
    ax, ay = acceleration(px, py)

    px_new = px + vx * dt + 0.5 * ax * dt**2 
    py_new = py + vy * dt + 0.5 * ay * dt**2

    ax_new, ay_new = acceleration(px_new, py_new)

    vx_new = vx + 0.5 * (ax + ax_new) * dt
    vy_new = vy + 0.5 * (ay + ay_new) * dt
    
    # print (px_new, py_new, vx_new, vy_new)

    return px_new, py_new, vx_new, vy_new





# Integrators for the particle simulation

def euler_step(state, dt, acceleration):
    
    ax, ay = acceleration(state.px, state.py)

    vx_new = state.vx + ax * dt
    vy_new = state.vy + ay * dt

    px_new = state.px + state.vx * dt
    py_new = state.py + state.vy * dt

    return Particle_State(vx_new, vy_new, px_new, py_new) 

def rk4_step(state, dt, accel_func):
    # K1
    ax1, ay1 = accel_func(state.px, state.py)
    k1_vx, k1_vy = ax1 * dt, ay1 * dt
    k1_px, k1_py = state.vx * dt, state.vy * dt 

    # K2
    ax2, ay2 = accel_func(state.px + 0.5 * k1_px, state.py + 0.5 * k1_py)
    k2_vx, k2_vy = ax2 * dt, ay2 * dt
    k2_px, k2_py = (state.vx + 0.5 * k1_vx) * dt, (state.vy + 0.5 * k1_vy) * dt

    # K3
    ax3, ay3 = accel_func(state.px + 0.5 * k2_px, state.py + 0.5 * k2_py)
    k3_vx, k3_vy = ax3 * dt, ay3 * dt
    k3_px, k3_py = (state.vx + 0.5 * k2_vx) * dt, (state.vy + 0.5 * k2_vy) * dt

    # K4
    ax4, ay4 = accel_func(state.px + k3_px, state.py + k3_py)
    k4_vx, k4_vy = ax4 * dt, ay4 * dt
    k4_px, k4_py = (state.vx + k3_vx) * dt, (state.vy + k3_vy) * dt

    px_new += 1/6 * (k1_px + 2 * k2_px + 2 * k3_px + k4_px)
    py_new += 1/6 * (k1_py + 2 * k2_py + 2 * k3_py + k4_py)
    vx_new += 1/6 * (k1_vx + 2 * k2_vx + 2 * k3_vx + k4_vx)
    vy_new += 1/6 * (k1_vy + 2 * k2_vy + 2 * k3_vy + k4_vy)

    return Particle_State(vx_new, vy_new, px_new, py_new) 

def velocity_verlet_step(state, dt, acceleration):

    ax, ay = acceleration(state.px, state.py)

    px_new = state.px + state.vx * dt + 0.5 * ax * dt**2
    py_new = state.py + state.vy * dt + 0.5 * ay * dt**2

    ax_new, ay_new = acceleration(px_new, py_new)

    vx_new = state.vx + 0.5 * (ax + ax_new) * dt
    vy_new = state.vy + 0.5 * (ay + ay_new) * dt


    return Particle_State(vx_new, vy_new, px_new, py_new) 





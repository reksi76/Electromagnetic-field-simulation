import numpy as np
from simulation.state import ParticleState

def boris_step(state, dt, field, grid, q, mode):

    # posisi
    x, y = state.x, state.y
    vx, vy = state.vx, state.vy

    # ambil field lokal (sama seperti acceleration)
    ix = np.argmin(abs(grid.x - x))
    iy = np.argmin(abs(grid.y - y))

    Ex_local = field.Ex[iy, ix]
    Ey_local = field.Ey[iy, ix]

    E0 = 1.0
    B0 = 1.0

    # mode
    if mode == 'Electrostatic':
        Ex, Ey = Ex_local, Ey_local
        Bz = 0

    elif mode == 'Magnetic_only':
        Ex, Ey = 0, 0
        Bz = B0

    elif mode == 'Electric_const':
        Ex, Ey = E0, 0
        Bz = 0

    elif mode == 'Electromagnetic':
        Ex = Ex_local + E0
        Ey = Ey_local
        Bz = B0

    else:
        raise ValueError("Unknown mode")

    # --- Boris algorithm ---

    # half acceleration by E
    vx_minus = vx + q * Ex * dt / 2
    vy_minus = vy + q * Ey * dt / 2

    # rotation due to B
    t = q * Bz * dt / 2
    s = 2 * t / (1 + t**2)

    # rotate velocity
    v_prime_x = vx_minus + vy_minus * t
    v_prime_y = vy_minus - vx_minus * t

    vx_plus = vx_minus + v_prime_y * s
    vy_plus = vy_minus - v_prime_x * s

    # second half E
    vx_new = vx_plus + q * Ex * dt / 2
    vy_new = vy_plus + q * Ey * dt / 2

    # update posisi
    x_new = x + vx_new * dt
    y_new = y + vy_new * dt

    return ParticleState(x_new, y_new, vx_new, vy_new)

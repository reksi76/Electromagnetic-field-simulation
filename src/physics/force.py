import numpy as np

# Lorentz Law:
# F = q(E + v x B)
def acceleration(state, field, grid, field_mode):

    ix = np.argmin(abs(grid.x - state.x))
    iy = np.argmin(abs(grid.y - state.y))
    
    E0 = 1.0
    B0 = 1.0
    # Electric Field 
    Ex_local = field.Ex[iy, ix]
    Ey_local = field.Ey[iy, ix]
    
    # Magnetic field
    
    if field_mode == 'Electrostatic':
        Ex, Ey = field.Ex[iy, ix], field.Ey[iy, ix]
        Bz = 0

    elif field_mode == 'Magnetic_only':
        Ex, Ey = 0, 0
        Bz = B0

    elif field_mode == 'Electric_const':
        Ex, Ey = E0, 0
        Bz = 0

    elif field_mode == 'Electromagnetic':
        Ex = Ex_local + E0
        Ey = Ey_local
        Bz = B0
    
    else:
        raise ValueError('Unknown Value_mode')

    # ax = q/m * (Ex - vy x Bz)
    # ay = q/m * (Ey + vx x Bz)
    # m = 1
    ax = state.q * (Ex + state.vy * Bz)
    ay = state.q * (Ey - state.vx * Bz)

    return ax, ay

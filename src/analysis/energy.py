import numpy  as np

# Energy calculation (E = 1/2 * m * v^2 + q * V)
def compute_energy(traj, field, q, charges, k):
    N = len(traj.px_list)
    energy_list = np.zeros(N)

    for t in range(N):
        # Kinetic energy 
        KE = 0.5 * (traj.vx_list[t]**2 + traj.vy_list[t]**2)


        # Electric potential
        V = 0 

        for charge in charges:
            q_source = charge['q']
            x0, y0 = charge['pos']

            dx = traj.px_list[t] - x0
            dy = traj.py_list[t] - y0

            r = np.sqrt(dx**2 + dy**2 + field.epsilon**2)

            V += (k * q_source) / r
            # Potential Energy
            PE = q * V
            energy_list[t] = KE + PE
    
    return energy_list

def energy_error(energy_list):

    E0 = energy_list[0]
    if abs(E0) < 1e-12:
        return np.zeros_like(energy_list)
    energy_list = np.array(energy_list)

    error = (energy_list - E0) / E0

    return error




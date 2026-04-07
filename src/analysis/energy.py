import numpy  as np

# Energy calculation (E = 1/2 * m * v^2 + q * V)
def compute_energy(trajectories, field, q, charges, k):
    for traj in trajectories:
        # print(traj)
        qi = traj.q
        N = len(traj.px_list)
        energy_list = np.zeros(N)
        all_energies = []

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
            PE = qi * V
            energy_list[t] = KE + PE
    all_energies.append(energy_list)
    return all_energies

def energy_error(energy_list):
    all_errors = []

    for energy in energy_list:
        E0 = energy[0]

        if abs(E0) < 1e-12:
            error = np.zeros_like(energy)
        else:
            error = (energy - E0) / E0

        all_errors.append(error)

        return all_errors




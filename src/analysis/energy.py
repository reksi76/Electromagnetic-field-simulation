import numpy  as np

# Energy calculation (E = 1/2 * m * v^2 + q * V)
def compute_energy(px, py, vx, vy, q, charges, k, epsilon):
    
    # Kinetic energy 
    KE = 0.5 * (vx**2 + vy**2)


    # Electric potential
    V = 0 

    for charge in charges:
        q_source = charge['q']
        x0, y0 = charge['pos']

        dx = px - x0
        dy = py - y0

        r = np.sqrt(dx**2 + dy**2 + epsilon**2)

        V += (k * q_source) / r
    # Potential Energy
    PE = q * V

    return KE + PE

def energy_error(energy_list):

    E0 = energy_list[0]
    energy_list = np.array(energy_list)

    error = (energy_list - E0) / E0

    return error




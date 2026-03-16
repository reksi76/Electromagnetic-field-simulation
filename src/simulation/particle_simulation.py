import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
from integrators.methods import (
        rk4_step, 
        euler_step,
        velocity_verlet_step
        )
from physics.force import acceleration
from analysis.energy import compute_energy

def particle_sim(step_function, x, y, Ex, Ey, q, charges, k, epsilon):
    dt = 0.002
    px, py = -4, 2 
    vx, vy = 0, 0
    N = 7000
    px_list = np.zeros(N)
    py_list = np.zeros(N)
    vx_list = np.zeros(N)
    vy_list = np.zeros(N)
    energy_list = np.zeros(N)
    
    def accel(px, py):
        return acceleration(px, py, q, x, y, Ex, Ey)

    for t in range(N):
        
        # 3 Integrators: rk4_step, euler_step, velocity_verlet_step

        px, py, vx, vy = step_function(
            px, py, vx, vy, dt, accel
        )

        px_list[t] = px
        py_list[t] = py
        vx_list[t] = vx 
        vy_list[t] = vy 

        energy_list[t] = compute_energy(
                px, py, vx, vy, q, charges, k, epsilon
                )

    return px_list, py_list, vx_list, vy_list, energy_list

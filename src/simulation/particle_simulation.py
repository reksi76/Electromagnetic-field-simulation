import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
from state import Trajectory
from integrators.methods import (
        rk4_step, 
        euler_step,
        velocity_verlet_step
        )
from physics.force import acceleration
from analysis.energy import compute_energy

def particle_sim(step_function, state, field, grid, q):
    dt = 0.002
    N = 7000

    traj = Trajectory(
            px_list = np.zeros(N)
            py_list = np.zeros(N)
            vx_list = np.zeros(N)
            vy_list = np.zeros(N)
            energy_list = np.zeros(N)
            )
    
    def accel(state.px, state.py):  
        return acceleration(state, field, grid, q)

    for t in range(N):
        
        # 3 Integrators: rk4_step, euler_step, velocity_verlet_step

        state.px, state.py, state.vx, state.vy = step_function(
            state, dt, accel
        )

        traj.px_list[t] = px
        traj.py_list[t] = py
        traj.vx_list[t] = vx 
        traj.vy_list[t] = vy 

        traj.energy_list[t] = compute_energy(
                state, field, q, charges, k
                )

    return traj

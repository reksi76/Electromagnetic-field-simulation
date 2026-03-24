import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np 
from simulation.state import Trajectory
from integrators.methods import (
        rk4_step, 
        euler_step,
        velocity_verlet_step
        )
from physics.force import acceleration

def make_accel(field, grid, q, mode):

    def accel(state):
        return acceleration(state, field, grid, q, mode)

    return accel    

def particle_sim(
        step_function, state,
        accel, N, dt
        ):

    traj = Trajectory(
            px_list = np.zeros(N),
            py_list = np.zeros(N),
            vx_list = np.zeros(N),
            vy_list = np.zeros(N),
            )
    
    traj.px_list[0] = state.x
    traj.py_list[0] = state.y
    traj.vx_list[0] = state.vx
    traj.vy_list[0] = state.vy

    for t in range(1, N):
        
        # 3 Integrators: rk4_step, euler_step, velocity_verlet_step

        state = step_function(
            state, dt, accel
        )

        traj.px_list[t] = state.x
        traj.py_list[t] = state.y
        traj.vx_list[t] = state.vx 
        traj.vy_list[t] = state.vy 

    return traj

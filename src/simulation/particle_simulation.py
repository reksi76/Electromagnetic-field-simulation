import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np 
from dataclasses import replace
from simulation.state import Trajectory
from integrators.methods import (
        rk4_step, 
        euler_step,
        velocity_verlet_step
        )
from physics.force import acceleration

def particle_sim(
        step_function, state, field, 
        grid, q, N=10000, dt=0.002
        ):

    traj = Trajectory(
            px_list = np.zeros(N),
            py_list = np.zeros(N),
            vx_list = np.zeros(N),
            vy_list = np.zeros(N),
            )
    
    def accel(x, y):  
        temp_state = replace(state, x=x, y=y)
        return acceleration(temp_state, field, grid, q, field_mode='Electromagnetic')

    for t in range(N):
        
        # 3 Integrators: rk4_step, euler_step, velocity_verlet_step

        state = step_function(
            state, dt, accel
        )

        traj.px_list[t] = state.x
        traj.py_list[t] = state.y
        traj.vx_list[t] = state.vx 
        traj.vy_list[t] = state.vy 

    return traj

import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from simulation.particle_simulation import particle_sim 
from simulation.state import ParticleState 
from integrators.methods import rk4_step
from physics.fields import electric_field
from physics.charges import setup_charges
from physics.grid import setup_grid
from physics.accel_func import make_accel

q = 1.0
dt = 0.01
N = 1000
k=1

charges = setup_charges()
grid = setup_grid()
field = electric_field(charges, k, grid)
print(field)

def run_simulation(field):
    accel = make_accel(field, grid, q, mode='Electrostatic')
    state = ParticleState(x=0, y=0, vx=1, vy=0)
    traj = particle_sim(rk4_step, state, field, grid, q, N, dt)
    return traj

def analytic_solution(t, state, E, q):
    x0, y0 = state.x, state.y
    vx0, vy0 = state.vx, state.vy

    x = x0 + vx0 * t 
    y = y0 + vy0 * t + 0.5 * q * E * t**2

    return x, y

def test_uniform_field(field):
    field.Ex[:] = 0 
    field.Ey[:] = -1.0 

    traj = run_simulation(field)
    t = np.arange(len(traj.px_list)) * dt
    x_sim = np.array(traj.px_list)
    y_sim = np.array(traj.py_list)

    init_state = ParticleState(x=0, y=0, vx=1, vy=0)
    x_exact, y_exact = analytic_solution(
            t=t,
            q=q,
            state=init_state,
            E=-1.0
            )
    error = np.sqrt((x_sim - x_exact)**2 + (y_sim - y_exact)**2)

    print('Max Error:', np.max(error))

test_uniform_field(field)

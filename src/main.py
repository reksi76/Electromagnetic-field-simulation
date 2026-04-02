import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import matplotlib.pyplot as plt 
import numpy as np 

from physics.charges import setup_charges 
from physics.fields import electric_field
from physics.potential import  electrical_potential
from physics.grid import setup_grid
from simulation.state import ParticleState, Trajectory
from simulation.particle_simulation import make_accel, particle_sim
from analysis.energy import compute_energy, energy_error
from integrators.methods import euler_step, rk4_step, velocity_verlet_step
from integrators.boris import boris_step


from visualization.visualize import (
        vis_charges,
        vis_electrical_field,
        vis_potential, 
        vis_particle_sim,
        vis_energy,
        vis_energy_error
        )

SHOW_FIELD = False 
SHOW_POTENTIAL = False 
SHOW_PARTICLE_SIM = False
SHOW_ENERGY = True
SHOW_ENERGY_ERROR = True

integrators = {
        'Euler': euler_step, 
        'RK4': rk4_step,
        'Velocity Verlet': velocity_verlet_step
        }

# Physics function

# grid:
# grid.x, grid.y, grid.X, grid.Y 

# field:
# field.Ex, field.Ey, field.epsilon

# --- CONFIG ---
q = 1.0
k = 1
N = 10000
dt = 0.02
mode = 'Electromagnetic'

# ---SETUP PHYSICS---
def init_simulation():
    charges = setup_charges()
    grid = setup_grid()
    field = electric_field(charges, k, grid)
    V_total = electrical_potential(field, charges, k, grid)
    state = ParticleState(
            x = -4,
            y = 2,
            vx = 1.0, 
            vy = 0
            )
    return charges, grid, field, V_total, state

charges, grid, field, V_total, state = init_simulation()

# --- CHOOSE SOLVER ---
if mode == 'Electromagnetic':
    integrators['Boris'] = boris_step

def run_all_integrators(integrators, state, field, grid, q, mode, N, dt):
    # particle_sim
    results = {}
    for name, method in integrators.items():

        if name == 'Boris':
            accel = None
            step = lambda s, dt, a: boris_step(s, dt, field, grid, q, mode)
        else:
            accel = make_accel(field, grid, q, mode)
            step = method

        sim = particle_sim(step, state, accel, N, dt) # return traj dataclass
        results[name]= sim
      
      # traj:
    # traj.px_list, traj.py_list, traj.vx_list, traj.vy_list, traj.energy_list
    return results

results = run_all_integrators(integrators, state, field, grid, q, mode, N, dt)

if SHOW_FIELD:
    # Electrical field
    fig, ax = plt.subplots(figsize=(6,4))
    vis_electrical_field(ax, grid, field)
    vis_charges(ax, charges)

# Electrical potential
if SHOW_POTENTIAL:
    fig, ax = plt.subplots(figsize=(6,4))
    cf = vis_potential(ax, grid, field, V_total)
    vis_charges(ax, charges)


if SHOW_PARTICLE_SIM: 
    # Visualization
    fig, ax = plt.subplots(figsize=(6,6))
    
    ani = vis_particle_sim(ax, results)
    vis_charges(ax, charges)

def energy_func(results, field, q, charges, k, mode):
    if mode == 'Electromagnetic':
        selected = {'Boris' : results['Boris']}
    else:
        selected = results

    energies = {
            name: compute_energy(res, field, q, charges, k)
            for name, res in selected.items() 
            }

    energy_errors = {
            name: energy_error(energy)
            for name, energy in energies.items()
            }
    return energies, energy_errors

energies, energy_errors = energy_func(results, field, q, charges, k, mode)

if SHOW_ENERGY:
    # Energy calculation
    fig, ax = plt.subplots(figsize=(6,4))
    for name, energy in energies.items():
        vis_energy(ax, energy, label=name)

# Energy energy_error
if SHOW_ENERGY_ERROR:
    fig, ax = plt.subplots(figsize=(6,4))
    for name, energy_error in energy_errors.items():
        vis_energy_error(ax, energy_error, label=name)

plt.show()


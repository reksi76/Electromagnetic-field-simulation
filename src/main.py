import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import matplotlib.pyplot as plt 
import numpy as np 
from dataclasses import replace

from physics.charges import setup_charges 
from physics.fields import electric_field
from physics.potential import  electrical_potential
from physics.grid import setup_grid
from simulation.state import ParticleState, Trajectory
from simulation.particle_simulation import particle_sim
from analysis.energy import compute_energy, energy_error
from integrators.methods import euler_step, rk4_step, velocity_verlet_step
from physics.accel_func import make_accel

from visualization.visualize import (
        vis_charges,
        vis_electrical_field,
        vis_potential, 
        vis_particle_sim,
        vis_energy,
        vis_energy_error
        )


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
q = 1.0
k = 1 
charges = setup_charges()
grid = setup_grid()
field = electric_field(charges, k, grid)
V_total = electrical_potential(field, charges, k, grid)
accel = make_accel(field, grid, q, mode='Electrostatic')
state = ParticleState(
        x = -4,
        y = 2,
        vx = 1.0, 
        vy = 0
        )

SHOW_FIELD = False 
SHOW_POTENTIAL = False 
SHOW_PARTICLE_SIM = True
SHOW_ENERGY = False
SHOW_ENERGY_ERROR = False

# Visualization
if SHOW_FIELD:
    # Electrical field
    fig, ax = plt.subplots(figsize= (6,4))
    vis_electrical_field(ax, grid, field)
    vis_charges(ax, charges)
    ax.set_title('Electrical Field')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid(True)

# Electrical potential
if SHOW_POTENTIAL:
    fig, ax = plt.subplots(figsize=(6,4))

    cf = vis_potential(ax, grid, field, V_total)
    vis_charges(ax, charges)
    ax.set_title('Electrical Potential')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid(True)
    fig.colorbar(cf, ax=ax)

if SHOW_PARTICLE_SIM: 
    # particle_sim
    results = {}
    for name, method in integrators.items():
        particle_result = []
        sim = particle_sim(method, replace(state), field, grid, q, N, dt) # return traj dataclass
        results[name]= sim
      
      # traj:
    # traj.px_list, traj.py_list, traj.vx_list, traj.vy_list, traj.energy_list
    
    # Visualization
    fig, ax = plt.subplots(figsize=(6, 6))
    ani = vis_particle_sim(ax, results)

    vis_charges(ax, charges)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_title(
        r"Particle Motion in Electric Field: $ \vec{F}=q\vec{E}, \; \vec{a}=\frac{q\vec{E}}{m} $)"
    )

euler_energy = compute_energy(results['Euler'], field, q, charges, k)
rk4_energy = compute_energy(results['RK4'], field, q, charges, k)
velocity_verlet_energy = compute_energy(results['Velocity Verlet'], field, q, charges, k)

if SHOW_ENERGY:
    # Energy calculation
    fig, ax = plt.subplots(figsize=(6,4))
    vis_energy(ax, euler_energy, label='Euler')
    vis_energy(ax, rk4_energy, label='RK4')
    vis_energy(ax, velocity_verlet_energy, label='Velocity Verlet ')

    
# Energy energy_error
if SHOW_ENERGY_ERROR:
    fig, ax = plt.subplots(figsize=(6,4))
    euler_error = energy_error(euler_energy)
    rk4_error = energy_error(rk4_energy)
    velocity_verlet_error = energy_error(velocity_verlet_energy)
    vis_energy_error(ax, euler_error, label='Euler')
    vis_energy_error(ax, rk4_error, label='RK4')
    vis_energy_error(ax, velocity_verlet_error, label='Velocity Verlet')


plt.show()


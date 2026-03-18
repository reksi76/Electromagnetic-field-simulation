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

from visualization.visualize import (
        vis_charges,
        vis_electrical_field,
        vis_potential, 
        vis_particle_sim,
        vis_energy
        )


integrators = {
        'Euler': euler_step, 
        'RK4': rk4_step,
        'Velocity Verlet': velocity_verlet_step
        }
particle_charges = [1.0, -1.0]

# Physics function

# grid:
# grid.x, grid.y, grid.X, grid.Y 

# field:
# field.Ex, field.Ey, field.epsilon

k = 1 
charges = setup_charges()
grid = setup_grid()
field = electric_field(charges, k, grid)
V_total = electrical_potential(field, charges, k, grid)
state = ParticleState(
        x = -4,
        y = 2,
        vx = 0, 
        vy = 0
        )

SHOW_FIELD = False
SHOW_POTENTIAL = False
SHOW_PARTICLE_SIM = True
SHOW_ENERGY = True

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

# particle_sim
results = {}
for name, method in integrators.items():
    particle_result = []
    for q in particle_charges:
        sim = particle_sim(method, replace(state), field, grid, q) # return traj dataclass
        particle_result.append(sim)
    results[name]= particle_result

# traj:
# traj.px_list, traj.py_list, traj.vx_list, traj.vy_list, traj.energy_list

euler1, euler2 = results["Euler"]
rk4_1, rk4_2 = results["RK4"]
verlet1, verlet2 = results["Velocity Verlet"]

if SHOW_PARTICLE_SIM: 
    fig, ax = plt.subplots(figsize=(6, 6))
    ani = vis_particle_sim(ax, euler1, euler2)

    vis_charges(ax, charges)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_title(
        r"Particle Motion in Electric Field: $ \vec{F}=q\vec{E}, \; \vec{a}=\frac{q\vec{E}}{m} $ (RK4 Integration)"
    )

if SHOW_ENERGY:
    # Energy calculation

    energy1 = compute_energy(euler1, field, 1, charges, k)
    energy2 = compute_energy(euler2, field, -1, charges, k)

    fig, ax = plt.subplots(figsize=(6,4))
    vis_energy(ax, energy1, energy2)
plt.show()






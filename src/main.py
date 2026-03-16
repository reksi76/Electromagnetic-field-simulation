import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import matplotlib.pyplot as plt 
import numpy as np 

from physics.charges import setup_charges 
from physics.fields import setup_grid, electric_field
from physics.potential import  electrical_potential
from simulation.particle_simulation import particle_sim
from analysis.energy import energy_error

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
charges = setup_charges()
k, x, y, X, Y = setup_grid()
Ex, Ey, epsilon = electric_field(charges, k, X, Y)
V_total = electrical_potential(epsilon, charges, k, X, Y)

SHOW_FIELD = False
SHOW_POTENTIAL = False
SHOW_PARTICLE_SIM = True
SHOW_ENERGY = True

# Visualization
if SHOW_FIELD:
    # Electrical field
    fig, ax = plt.subplots(figsize= (6,4))
    vis_electrical_field(ax, x, y, Ex, Ey)
    vis_charges(ax, charges)
    ax.set_title('Electrical Field')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid(True)

# Electrical potential
if SHOW_POTENTIAL:
    fig, ax = plt.subplots(figsize=(6,4))

    cf = vis_potential(ax, X, Y, Ex, Ey, V_total)
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
        sim = particle_sim(method, x, y, Ex, Ey, q, charges,k, epsilon)
        particle_result.append(sim)
    result[name]= particle_result

e_px1, e_py1, e_vx1, e_vy1, e_energy1 = results["Euler"][0]
e_px2, e_py2, e_vx2, e_vy2, e_energy2 = results["Euler"][1]
k_px1, k_py1, k_vx1, k_vy1, k_energy1 = results["RK4"][0]
k_px2, k_py2, k_vx2, k_vy2, k_energy2 = results["RK4"][1]
v_px1, v_py1, v_vx1, v_vy1, v_energy1 = results["Velocity Verlet"][0]
v_px2, v_py2, v_vx2, v_vy2, v_energy2 = results["Velocity Verlet"][1]


if SHOW_PARTICLE_SIM: 
    fig, ax = plt.subplots(figsize=(6, 6))
    ani = vis_particle_sim(ax, e_px1, e_py1, e_px2, e_py2)
    vis_charges(ax, charges)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_title(
        r"Particle Motion in Electric Field: $ \vec{F}=q\vec{E}, \; \vec{a}=\frac{q\vec{E}}{m} $ (RK4 Integration)"
    )

if SHOW_ENERGY:
    # Energy calculation

    fig, ax = plt.subplots(figsize=(6,4))
    vis_energy(ax, e_energy1, e_energy2)
plt.show()






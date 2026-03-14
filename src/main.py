import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import matplotlib.pyplot as plt 
import numpy as np 

from physics.charges import setup_charges 
from physics.fields import setup_grid, electric_field
from physics.potential import  electrical_potential
from simulation.particle_simulation import particle_sim

from visualization.visualize import (
        vis_charges,
        vis_electrical_field,
        vis_potential, 
        vis_particle_sim,
        vis_energy
        )

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
px1, py1, vx_list1, vy_list1 = particle_sim(x, y, Ex, Ey, 1.0)
px2, py2, vx_list2, vy_list2 = particle_sim(x, y, Ex, Ey, -1.0)

if SHOW_PARTICLE_SIM: 
    fig, ax = plt.subplots(figsize=(6, 6))
    ani = vis_particle_sim(ax, px1, py1, px2, py2)
    vis_charges(ax, charges)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_title(
        r"Particle Motion in Electric Field: $ \vec{F}=q\vec{E}, \; \vec{a}=\frac{q\vec{E}}{m} $ (RK4 Integration)"
    )

if SHOW_ENERGY:
    # Energy calculation

    fig, ax = plt.subplots(figsize=(6,4))
    vis_energy(ax, energy_list1, energy_list2)

plt.show()






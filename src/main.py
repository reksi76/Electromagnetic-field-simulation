import matplotlib.pyplot as plt 
import numpy as np 

from physics import (
        setup_charges, 
        setup_grid,
        electrical_field,
        electrical_potential,
        particle_sim
        )
from visualize import (
        vis_charges,
        vis_electrical_field,
        vis_potential, 
        vis_particle_sim
        )

charges = setup_charges()
k, x, y, X, Y = setup_grid()
Ex, Ey = electrical_field(charges, k, X, Y)
V_total = electrical_potential(charges, k, X, Y)
px_list, py_list = particle_sim(x, y, Ex, Ey)



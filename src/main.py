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

# Physics function
charges = setup_charges()
k, x, y, X, Y = setup_grid()
Ex, Ey = electrical_field(charges, k, X, Y)
V_total = electrical_potential(charges, k, X, Y)
px_list, py_list = particle_sim(x, y, Ex, Ey)

# Visualization
# Electrical field
fig1, ax1 = plt.subplots(figsize= (6,4))
vis_electrical_field(ax1, x, y, Ex, Ey)
vis_charges(ax1, charges)
ax1.set_title('Electrical Field')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.grid('True')
plt.show()

# Electrical potential
fig2, ax2 = plt.subplots(figsize=(6,4))

cf = vis_potential(ax2, X, Y, Ex, Ey, V_total)
vis_charges(ax2, charges)
ax2.set_title('Electrical Potential')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.grid('True')
fig2.colorbar(cf, ax=ax2)
plt.show()




import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from integrators.rk4 import rk4_step
from physics.force import acceleration

def particle_sim(x, y, Ex, Ey, q):
    dt = 0.002
    px, py = -4, 2 
    vx, vy = 0, 0
    N = 3000
    px_list = np.zeros(N)
    py_list = np.zeros(N)
    vx_list = np.zeros(N)
    vy_list = np.zeros(N)
    energy_list = np.zeros(N)

    for t in range(N):

        px, py, vx, vy = rk4_step(
            px, py, vx, vy, dt,
            lambda px,py: acceleration(px,py,q,x,y,Ex,Ey)
        )

        px_list[t] = px
        py_list[t] = py
        vx_list[t] = vx 
        vy_list[t] = vy 

    return px_list, py_list, vx_list, vy_list

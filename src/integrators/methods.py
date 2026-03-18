# Integrators for the particle simulation
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from simulation.state import ParticleState

def euler_step(state, dt, acceleration):
    
    ax, ay = acceleration(state.x, state.y)

    vx_new = state.vx + ax * dt
    vy_new = state.vy + ay * dt

    px_new = state.x + state.vx * dt
    py_new = state.y + state.vy * dt

    return ParticleState(px_new, py_new, vx_new, vy_new) 

def rk4_step(state, dt, acceleration):
    # K1
    ax1, ay1 = acceleration(state.x, state.y)
    k1_vx, k1_vy = ax1 * dt, ay1 * dt
    k1_px, k1_py = state.vx * dt, state.vy * dt 

    # K2
    ax2, ay2 = acceleration(state.x + 0.5 * k1_px, state.y + 0.5 * k1_py)
    k2_vx, k2_vy = ax2 * dt, ay2 * dt
    k2_px, k2_py = (state.vx + 0.5 * k1_vx) * dt, (state.vy + 0.5 * k1_vy) * dt

    # K3
    ax3, ay3 = acceleration(state.x + 0.5 * k2_px, state.y + 0.5 * k2_py)
    k3_vx, k3_vy = ax3 * dt, ay3 * dt
    k3_px, k3_py = (state.vx + 0.5 * k2_vx) * dt, (state.vy + 0.5 * k2_vy) * dt

    # K4
    ax4, ay4 = acceleration(state.x + k3_px, state.y + k3_py)
    k4_vx, k4_vy = ax4 * dt, ay4 * dt
    k4_px, k4_py = (state.vx + k3_vx) * dt, (state.vy + k3_vy) * dt

    px_new = state.x + 1/6 * (k1_px + 2 * k2_px + 2 * k3_px + k4_px)
    py_new = state.y + 1/6 * (k1_py + 2 * k2_py + 2 * k3_py + k4_py)
    vx_new = state.vx + 1/6 * (k1_vx + 2 * k2_vx + 2 * k3_vx + k4_vx)
    vy_new = state.vy + 1/6 * (k1_vy + 2 * k2_vy + 2 * k3_vy + k4_vy)

    return ParticleState(px_new, py_new, vx_new, vy_new) 

def velocity_verlet_step(state, dt, acceleration):

    ax, ay = acceleration(state.x, state.y)

    px_new = state.x + state.vx * dt + 0.5 * ax * dt**2
    py_new = state.y + state.vy * dt + 0.5 * ay * dt**2

    ax_new, ay_new = acceleration(px_new, py_new)

    vx_new = state.vx + 0.5 * (ax + ax_new) * dt
    vy_new = state.vy + 0.5 * (ay + ay_new) * dt


    return ParticleState(px_new, py_new, vx_new, vy_new) 





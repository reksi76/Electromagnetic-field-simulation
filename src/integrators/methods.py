# Integrators for the particle simulation
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from simulation.state import ParticleState

def euler_step(state, dt, acceleration):
    
    ax, ay = acceleration(state)

    vx_new = state.vx + ax * dt
    vy_new = state.vy + ay * dt

    px_new = state.x + state.vx * dt
    py_new = state.y + state.vy * dt

    return ParticleState(px_new, py_new, vx_new, vy_new, state.q) 

def rk4_step(state, dt, acceleration):
    # K1
    ax1, ay1 = acceleration(state)
    k1_vx, k1_vy = ax1 * dt, ay1 * dt
    k1_px, k1_py = state.vx * dt, state.vy * dt 

    # K2
    s2 = ParticleState(
            state.x + 0.5 * k1_px,
            state.y  + 0.5 * k1_py,
            state.vx + 0.5 * k1_vx,
            state.vy + 0.5 * k1_vy,
            state.q
            )
    ax2, ay2 = acceleration(s2)
    k2_vx, k2_vy = ax2 * dt, ay2 * dt
    k2_px, k2_py = s2.vx * dt, s2.vy * dt

    # K3
    s3 = ParticleState(
            state.x + 0.5 * k2_px,
            state.y + 0.5 * k2_py,
            state.vx + 0.5 * k2_vx,
            state.vy + 0.5 * k2_vy,
            state.q
            )
    ax3, ay3 = acceleration(s3)
    k3_vx, k3_vy = ax3 * dt, ay3 * dt
    k3_px, k3_py = s3.vx * dt, s3.vy * dt

    # K4
    s4 = ParticleState(
            state.x + k3_px, 
            state.y + k3_py,
            state.vx + k3_vx,
            state.vy + k3_vy,
            state.q
            )
    ax4, ay4 = acceleration(s4)
    k4_vx, k4_vy = ax4 * dt, ay4 * dt
    k4_px, k4_py = s4.vx * dt, s4.vy * dt

    px_new = state.x + 1/6 * (k1_px + 2 * k2_px + 2 * k3_px + k4_px)
    py_new = state.y + 1/6 * (k1_py + 2 * k2_py + 2 * k3_py + k4_py)
    vx_new = state.vx + 1/6 * (k1_vx + 2 * k2_vx + 2 * k3_vx + k4_vx)
    vy_new = state.vy + 1/6 * (k1_vy + 2 * k2_vy + 2 * k3_vy + k4_vy)

    return ParticleState(px_new, py_new, vx_new, vy_new, state.q) 

def velocity_verlet_step(state, dt, acceleration):
    ax, ay = acceleration(state)

    px_new = state.x + state.vx * dt + 0.5 * ax * dt**2
    py_new = state.y + state.vy * dt + 0.5 * ay * dt**2

    temp_state = ParticleState(px_new, py_new, state.vx, state.vy, state.q)
    ax_new, ay_new = acceleration(temp_state)

    vx_new = state.vx + 0.5 * (ax + ax_new) * dt
    vy_new = state.vy + 0.5 * (ay + ay_new) * dt

    return ParticleState(px_new, py_new, vx_new, vy_new, state.q)

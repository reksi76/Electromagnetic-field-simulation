from dataclasses import dataclass 
import numpy as np 

@dataclass
class ParticleState:
    x: float
    y: float
    vx: float
    vy: float
    q: float

@dataclass
class Trajectory:
    px_list: np.ndarray
    py_list: np.ndarray
    vx_list: np.ndarray
    vy_list: np.ndarray
    q: float


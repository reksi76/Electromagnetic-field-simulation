from dataclasses import dataclass 
import numpy as np 

@dataclass
class ParticleState:
    x: float
    y: float
    vx: float
    vy: float

@dataclass
class Trajectory:
    px: np.ndarray
    py: np.ndarray
    vx: np.ndarray
    vy: np.ndarray
    energy: np.ndarray


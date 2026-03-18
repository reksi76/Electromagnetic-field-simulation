from dataclasses import dataclass
import numpy as np 

@dataclass
class ElectricField:
    Ex: np.ndarray
    Ey: np.ndarray
    epsilon: float

def electric_field(charges, k, grid):
    Ex = np.zeros_like(grid.X)
    Ey = np.zeros_like(grid.Y)

    for charge in charges:
        q = charge['q']
        x0, y0 = charge['pos']

        dx = grid.X - x0
        dy = grid.Y - y0

        epsilon = 0.2
        r = np.sqrt(dx**2 + dy**2 + epsilon**2)
        Ex += (k * q * dx) / r**3
        Ey += (k * q * dy) / r**3

    return ElectricField(Ex, Ey, epsilon)



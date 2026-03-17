import numpy as np
from dataclasses import dataclass

@dataclass
class Grid:
    x: np.ndarray
    y: np.ndarray
    X: np.ndarray
    Y: np.ndarray

def setup_grid(xmin=-5, xmax=5, n=400):
    k = 1.0
    x = np.linspace(xmin, xmax, n)
    y = np.linspace(xmin, xmax, n)

    X, Y = np.meshgrid(x, y)

    return Grid(x, y, X, Y) 

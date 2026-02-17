import numpy as np 
import matplotlib.pyplot as plt

charges = [
        {'q': (1.0), 'pos': (-1.0, 0.0)},
        {'q': (-1.0), 'pos': (1.0, 0.0)}
        ]

k = 1.0

# Electric field
x = np.linspace(-5, 5, 40)
y = np.linspace(-5, 5, 40)
X, Y = np.meshgrid(x, y)

Ey = np.zeros_like(Y)
Ex = np.zeros_like(X)


for charge in charges:
    q = charge['q']
    x0, y0 = charge['pos']

    dx = X - x0
    dy = Y - y0

    r = np.sqrt(dx**2 + dy**2) + 1e-10
   
    r_min = 0.4
    mask = r >= r_min

    Ex[mask] += k * q * dx[mask] / r[mask]**3
    Ey[mask] += k * q * dy[mask] / r[mask]**3

plt.figure(figsize=(6,4))
plt.streamplot(X, Y, Ex, Ey)

for charge in charges:
    x0, y0 = charge['pos']

    if charge['q'] < 0:
        plt.scatter(x0, y0, color='b', s=100)

    else:
        plt.scatter(x0, y0, c='r', s=100)
plt.axis('equal')
plt.show()
    

# Electric potential (V = kq/r)
V_total = np.zeros_like(X)

for charge in charges:
    q = charge['q']
    x0, y0 = charge['pos']

    dx = X - x0
    dy = Y - y0

    r = np.sqrt(dx**2 + dy**2) + 1e-5

    r_min = 0.5
    mask = r >= r_min
    
    V_total[mask] += k * q / r[mask]

plt.figure(figsize=(6,4))
plt.contour(X, Y, V_total, cmap='inferno')
plt.colorbar()
plt.show()

plt.figure(figsize=(6,4))
plt.contourf(X, Y, V_total, cmap='inferno')
plt.colorbar()
plt.show()

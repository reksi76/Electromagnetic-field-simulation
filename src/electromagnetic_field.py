import numpy as np 
import matplotlib.pyplot as plt

charges = [
        {'q': (1.0), 'pos': (-1.0, 0.0)},
        {'q': (-1.0), 'pos': (1.0, 0.0)}
        ]

k = 1.0


x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)
X, Y = np.meshgrid(x, y)

# Electric field
def electric_field(charges, k):
    Ey = np.zeros_like(Y)
    Ex = np.zeros_like(X)

    
    for charge in charges:
        q = charge['q']
        x0, y0 = charge['pos']

        dx = X - x0
        dy = Y - y0

        epsilon = 0.2
        r = np.sqrt(dx**2 + dy**2 + epsilon**2)

        Ex += k * q * dx / r**3
        Ey += k * q * dy / r**3

    plt.figure(figsize=(6,4))
    plt.streamplot(X, Y, Ex, Ey)

    for charge in charges:
        x0, y0 = charge['pos']

        if charge['q'] < 0:
            plt.scatter(x0, y0, color='b', s=100)

        else:
            plt.scatter(x0, y0, c='r', s=100)
    plt.axis('equal')
    # plt.show()

    return Ex, Ey
    

# Electric potential (V = kq/r)
def electric_potential(charges, X, Y):
    V_total = np.zeros_like(X)

    for charge in charges:
        q = charge['q']
        x0, y0 = charge['pos']

        dx = X - x0
        dy = Y - y0

        epsilon = 0.2
        r = np.sqrt(dx**2 + dy**2 + epsilon**2)

        V_total += k * q / r

    plt.figure(figsize=(6,4))
    plt.contour(X, Y, V_total, cmap='inferno')
    plt.colorbar()
    # plt.show()

    plt.figure(figsize=(6,4))
    plt.contourf(X, Y, V_total, cmap='inferno')
    plt.colorbar()
    plt.show()

    # Overly
    fig, ax = plt.subplots(figsize=(6,4))

    # streamplot
    ax.streamplot(X, Y, Ex, Ey, color='b', density=1.5)

    # Contourf
    cf = ax.contourf(X, Y, V_total, cmap='inferno', alpha=0.8)

    fig.colorbar(cf, ax=ax)
    # plt.show()

    # Simulation
def particle_sim(x, y, Ex, Ey):

    dt = 0.01
    px, py = -4, 2 
    px_list = []
    py_list = []
    vx = 0.0
    vy = 0.0

    for t in range(5000):
        ix = round(np.argmin(abs(x - px)))
        iy = round(np.argmin(abs(y - py)))

        Ex_local = Ex[ix][iy]
        Ey_local = Ey[ix][iy]

        q_test = 1.0 
        m = 1.0

        ax = Ex_local
        ay = Ey_local

        vx += ax * dt 
        vy += ay * dt 

        px += vx * dt 
        py += vx * dt 

        px_list.append(px)
        py_list.append(py)

    plt.figure(figsize=(10, 4))



    







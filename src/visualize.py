import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

def vis_charges(ax, charges):
    for charge in charges:
        x0, y0 = charge['pos']

        if charge['q'] < 0:
            ax.scatter(x0, y0, color='b', s=200)
        else:
            ax.scatter(x0, y0, color='r', s=200)

def vis_electrical_field(ax, x, y, Ex, Ey):
    ax.streamplot(x, y, Ex, Ey, color='blue')

def vis_potential(ax, X, Y, Ex, Ey, V_total):
    ax.streamplot(X, Y, Ex, Ey,color='blue', density=1.5)
    cf = ax.contourf(X, Y, V_total, cmap='inferno', alpha=0.8)
    return cf 

def vis_particle_sim(ax, px1, px2, py1, py2):
    fig = ax.figure
    ax.set_aspect('equal')


    xmin = min(px1+px2)
    xmax = max(px1+px2)
    ymin = min(py1+py2)
    ymax = max(py1+py2)

    ax.set_xlim(xmin-1, xmax+1)
    ax.set_ylim(ymin-1, ymax+1)

    dot1, = ax.plot([], [], 'o', color='orange')
    dot2, = ax.plot([], [], 'o', color='cyan')


    def update(frame):
        dot1.set_data(px1[frame], py1[frame])
        dot2.set_data(px2[frame], py2[frame])
        return dot1, dot2 

    ani = FuncAnimation(
            fig, 
            update, 
            frames = len(px1),
            interval = 100
            )
    return ani

    

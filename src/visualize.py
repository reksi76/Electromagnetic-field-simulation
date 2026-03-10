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

def vis_particle_sim(ax, px1, py1, px2, py2):
    fig = ax.figure
    ax.set_aspect('equal')

    all_x = px1 + px2
    all_y = py1 + py2
    
    xmin, xmax = min(all_x), max(all_x)
    ymin, ymax = min(all_y), max(all_y)

    x_center = (xmin + xmax)/2 
    y_center = (ymin + ymax)/2 
    max_range = max(xmax - xmin, ymax - ymin)

    ax.set_xlim(x_center - max_range/2, x_center + max_range/2)
    ax.set_ylim(y_center - max_range/2, y_center + max_range/2)
    
    # Particle position
    dot1, = ax.plot([], [], 'o', color='orange')
    dot2, = ax.plot([], [], 'o', color='cyan')

    # Tranjectory trails
    trail1, = ax.plot([], [], '-', color='orange', linewidth=1)
    trail2, = ax.plot([], [], '-', color='cyan', linewidth=1)

    def update(frame):
        dot1.set_data(px1[frame], py1[frame])
        dot2.set_data(px2[frame], py2[frame])

        trail1.set_data(px1[:frame], py1[:frame])
        trail2.set_data(px2[:frame], py2[:frame])
        return dot1, dot2, trail1, trail2 

    ani = FuncAnimation(
            fig, 
            update, 
            frames = len(px1),
            interval = 10
            )
    ani.save('../plots/particle_simulation.gif')

    return ani

    

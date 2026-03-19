import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def vis_charges(ax, charges):
    for charge in charges:
        x0, y0 = charge['pos']

        if charge['q'] < 0:
            ax.scatter(x0, y0, color='b', s=200)
        else:
            ax.scatter(x0, y0, color='r', s=200)

def vis_electrical_field(ax, grid, field):
    ax.streamplot(grid.x, grid.y, field.Ex, field.Ey, color='blue')

def vis_potential(ax, grid, field, V_total):
    ax.streamplot(grid.X, grid.Y, field.Ex, field.Ey, color='blue', density=1.5)
    cf = ax.contourf(grid.X, grid.Y, V_total, cmap='inferno', alpha=0.8)
    return cf 

def vis_particle_sim(ax, trajectories):
    fig = ax.figure
    ax.set_aspect('equal')

    all_x = np.concatenate([traj.px_list for traj in trajectories.values()])
    all_y = np.concatenate([traj.py_list for traj in trajectories.values()])
    
    xmin, xmax = min(all_x), max(all_x)
    ymin, ymax = min(all_y), max(all_y)

    x_center = (xmin + xmax)/2 
    y_center = (ymin + ymax)/2 
    max_range = max(xmax - xmin, ymax - ymin)

    ax.set_xlim(x_center - max_range/2, x_center + max_range/2)
    ax.set_ylim(y_center - max_range/2, y_center + max_range/2)
    frame_skip = 10
    
    dots = [] 
    trails = []
    colors = ['orange', 'cyan', 'green', 'red', 'purple']

    for i, (name, traj) in enumerate(trajectories.items()):
        dot, = ax.plot([], [], 'o', color= colors[i], label=name)
        trail, = ax.plot([], [], '-', color=colors[i], label=name)
        dots.append(dot)
        trails.append(trail)
    ax.legend()

    
    num_frames = 400
    indices = np.linspace(0, len(traj.px_list) - 1, num_frames).astype(int)
    def update(frame):
        for i, traj in enumerate(trajectories.values()):
            dots[i].set_data(traj.px_list[frame], traj.py_list[frame])
            trail[i].set_data(traj.px_list[frame, traj.py_list[frame]])

        return dots + trails 

    ani = FuncAnimation(
            fig, 
            update, 
            frames = indices, 
            interval = 10
            )
    # ani.save('../plots/particle_simulation.gif', writer='pillow', fps=40)

    return ani

def vis_energy(ax, energy, label):
    ax.plot(energy, label=f'{label}Integrator Energy')
    ax.set_xlabel('Time step')
    ax.set_ylabel('Energy')
    ax.set_title('Energy vs Time')
    ax.legend()
    ax.grid(True)

def vis_energy_error(ax, error, label):
    ax.plot(error, label=f'{label} Error')
    ax.set_title('Energy Error')
    ax.set_xlabel("Time step")
    ax.set_ylabel("Relative Energy Error")
    ax.legend()
    ax.grid(True)

    

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def vis_charges(ax, charges):
    for charge in charges:
        x0, y0 = charge['pos']

        if charge['q'] < 0:
            ax.scatter(x0, y0, color='b', s=200)
            ax.text(x0, y0, '-', color='white', ha='center', va='center', fontsize=14, weight='bold')
        else:
            ax.scatter(x0, y0, color='r', s=200)
            ax.text(x0, y0, '+', color='white', ha='center', va='center', fontsize=14, weight='bold')

def vis_electrical_field(ax, grid, field):
    ax.set_title('Electrical Field')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid(True)
    ax.streamplot(grid.x, grid.y, field.Ex, field.Ey, color='blue')

def vis_potential(ax, grid, field, V_total):
    ax.streamplot(grid.X, grid.Y, field.Ex, field.Ey, color='blue', density=1.5)
    ax.set_title('Electrical Potential')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid(True)

    cf = ax.contourf(grid.X, grid.Y, V_total, cmap='inferno', alpha=0.8)

def vis_particle_sim(ax, trajectories):
    # print(trajectories)
    all_traj = [traj for traj_list in trajectories.values() for traj in traj_list]
    
    all_x = np.concatenate([t.px_list for t in all_traj])
    all_y = np.concatenate([t.py_list for t in all_traj])
    
    xmin, xmax = min(all_x), max(all_x)
    ymin, ymax = min(all_y), max(all_y)

    x_center = (xmin + xmax)/2 
    y_center = (ymin + ymax)/2 
    max_range = max(xmax - xmin, ymax - ymin)

    ax.set_xlim(x_center - max_range/2, x_center + max_range/2)
    ax.set_ylim(y_center - max_range/2, y_center + max_range/2)     
    ax.set_title(
        r"Particle Motion in Electric Field: $ \vec{F}=q\vec{E}, \; \vec{a}=\frac{q\vec{E}}{m} $)"
    )
    fig = ax.figure
    ax.set_aspect('equal')
    frame_skip = 10
    
    dots = [] 
    trails = []
    traj_refs = []
    colors = ['orange', 'cyan', 'green', 'red', 'purple']

    for i, (method_name, traj_list) in enumerate(trajectories.items()):
        color = colors[i % len(colors)]
        for traj in traj_list:
            dot, = ax.plot([], [], 'o', color= colors[i], label=method_name)
            trail, = ax.plot([], [], '-', color=colors[i], label='_nolegend_')
            dots.append(dot)
            trails.append(trail)
            traj_refs.append(traj)
            
            ax.plot([], [], color=colors[i % len(colors)], label=method_name)
    ax.legend()

    
    num_frames = 400
    indices = np.linspace(0, len(traj_refs[0].px_list) - 1, num_frames).astype(int)
    def update(frame_idx):
        idx = indices[frame_idx]

        for i, traj in enumerate(trajectories.values()):
            dots[i].set_data(traj.px_list[dx], traj.py_list[dx])
            trails[i].set_data(traj.px_list[:idx], traj.py_list[:idx])

        return dots + trails 

    ani = FuncAnimation(
            fig, 
            update, 
            frames = len(indices), 
            interval = 10
            )
    # ani.save('../plots/particle_simulation.gif', writer='pillow', fps=40)

    return ani

def vis_energy(ax, energy, label):
    ax.plot(energy, label=f'{label} Integrator Energy')
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

    

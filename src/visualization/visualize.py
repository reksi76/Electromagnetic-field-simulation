import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter

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

def vis_particle_sim(ax, charges, trajectories):
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
    ax.set_aspect('equal')
    ax.set_title(
        r"Particle Motion in Electric Field: $ \vec{F}=q\vec{E}, \; \vec{a}=\frac{q\vec{E}}{m} $"
        )

    vis_charges(ax, charges)
    fig = ax.figure
    ax.set_aspect('equal')
    frame_skip = 10
    
    dots = [] 
    trails = []
    traj_refs = []
    colors = {'Euler':'orange', 'RK4':'cyan', 'Velocity Verlet':'green', 'Boris':'red'}

    for i, (method_name, traj_list) in enumerate(trajectories.items()):
        # color = colors[i % len(colors)]
        for traj in traj_list:
            dot, = ax.plot([], [], 'o', color= colors[method_name])
            trail, = ax.plot([], [], '-', color=colors[method_name], label='_nolegend_')
            dots.append(dot)
            trails.append(trail)
            traj_refs.append(traj)
            
    for method_name, color in colors.items():
        ax.plot([], [], color=color, label=method_name)

    ax.legend()

    
    num_frames = 400
    indices = np.linspace(0, len(traj_refs[0].px_list) - 1, num_frames).astype(int)
    def update(frame_idx):
        idx = indices[frame_idx]

        for i, traj in enumerate(traj_refs):
            dots[i].set_data(traj.px_list[idx], traj.py_list[idx])
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

def vis_energy(ax, energy_list, label):
    for i, energy in enumerate(energy_list):
        if i == 0:
            ax.plot(energy, label=f'{label} Integrator Energy')
        else:
            ax.plot(energy)

    ax.set_xlabel('Time step')
    ax.set_ylabel('Energy')
    ax.set_title('Energy vs Time')
    ax.legend()
    ax.grid(True)

def vis_energy_error(ax, error_list, label):
    for i, err in enumerate(error_list):
        if i == 0:
            ax.plot(err, label=f'{label} Error')
        else:
            ax.plot(err)

    ax.set_title('Energy Error')
    ax.set_xlabel("Time step")
    ax.set_ylabel("Relative Energy Error")
    ax.legend()
    ax.grid(True)

    

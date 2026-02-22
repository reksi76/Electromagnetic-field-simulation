import matplotlib.pyplot as plt 

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

def vis_particle_sim(ax, px_list, py_list):
    ax.plot(px_list, py_list)



    

import matplotlib.pyplot as plt 

def vis_charges(charges):
    for charge in charges:
        x0, y0 = charge['pos']

        if charge['q'] < 0:
            plt.scatter(x0, y0, color='b', s=200)
        else:
            plt.scatter(x0, y0, color='r', s=200)

    

def vis_electrical_field(x, y, Ex, Ey):
    plt.figure(figsize=(6,4))
    plt.streamplot(Ex, Ey, x, y)

def vis_potential(X, Y, V_total):
    fig, ax = plt.subplots(figsize=(6,4))

    ax.streamplot(X, Y, Ex, Ey, density=1.5)
    cf = conrourf(X, Y, V_total, cmap='inferno', alpha=0.8)
    fig.colorbar(cf, ax=ax)

def vis_particle_sim(px_list, py_list):
    plt.figure(figsize=(10,4))
    plt.plot(px_list, py_list)



    

import numpy as np 

def run_experiment(init_simulation, run_all_integrators, energy_func, 
                   integrators, config, dt_list, integrators_names, N, mode, k):

    summary = {}
    for dt in dt_list:
        charges, grid, field, V_total, particles = init_simulation(config=config)
        q = [state.q for state in particles]

        selected_integrators = {
                name: integrators[name] for name in integrators_names
                }

        results = run_all_integrators(
                selected_integrators, particles, field, grid, q, mode, N, dt
                )

        energies, errors = energy_func(results, field, q, charges, k, mode)

        summary[dt] = {
                name: {
                    'max_error' : max(err), 
                    'mean_error' : np.mean(err)
                    }
                for name, err in errors.items()
                }

        return summary

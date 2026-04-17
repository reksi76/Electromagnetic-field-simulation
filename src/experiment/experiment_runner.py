import numpy as np 

def run_experiment(init_simulation, run_all_integrators, energy_func, 
                   integrators, config, dt_list, integrators_names, N, mode, k):
        charges, grid, field, V_total, particles = init_simulation(config=config)
        q = [state.q for state in particles]

        summary = {}
        for dt in dt_list:
            selected_integrators = {
                    name: integrators[name] for name in integrators_names
                }

        results = run_all_integrators(
                selected_integrators, particles, field, grid, q, mode, N, dt
                )

        energies, errors = energy_func(results, field, q, charges, k, mode)

        summary[dt] = {
                name : {
                        'max_error' : float(np.max(err)),
                        'mean_error' : float(np.min(err))
                    }
                for name, err in errors.items()
                }

        return summary

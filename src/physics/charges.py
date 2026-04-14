def setup_charges(config):
    if config == 'dipole':

        charges = [
                {'q' : -1.0, 'pos' : (-1.0, 0)},
                {'q' : 1.0, 'pos' : (1.0, 0)}
                ]
    elif config == 'asymetric_dipole':
        charges = [
                {'q' : -1, 'pos' : (-1, 0)},
                {'q' : 1, 'pos' : (2, 0.5)}
                ]
    elif config == 'multi_source':
        charges = [
                {'q' : -1, 'pos' : (-1, 0)},
                {'q' : 1, 'pos' : (1, 0)},
                {'q' : 1, 'pos' : (0, 1.5)},
                ]

    elif config == 'perturbed':
        charges = [
                {'q' : -1, 'pos': (-1, 0)},
                {'q' : 1, 'pos': (1, 0)},
                {'q' : -1, 'pos': (0.3, 0.3)},
                ]
    else:
        raise ValueError(
                f'Unknown config: {config}'
                'Available config:  dipole, asymetric_dipole, multi_source, perturbed'
                         )


    return charges

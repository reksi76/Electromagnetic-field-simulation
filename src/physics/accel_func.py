from physics.force import acceleration

def make_accel(field, grid, q, mode):

    def accel(state):
        return acceleration(state, field, grid, q, field_mode=mode)

    return accel

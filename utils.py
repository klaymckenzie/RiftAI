def validate_energy_input(user_input):
    try:
        energy = int(user_input)
        if 0 <= energy <= 100:
            return energy
    except ValueError:
        pass
    return None
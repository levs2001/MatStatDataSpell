import numpy as np


def get_with_noise(x_mass, noise_func):
    y_mass = []
    epsilon = 0.1
    for el in x_mass:
        y_mass.append(el + epsilon * noise_func())
    return np.array(y_mass)

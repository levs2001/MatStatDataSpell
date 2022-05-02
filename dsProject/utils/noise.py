import numpy as np


def get_with_noise(x_mass, noise_func, epsilon=0.1, factor=1):
    y_mass = []
    for el in x_mass:
        y_mass.append(factor * el + epsilon * noise_func())
    return np.array(y_mass)

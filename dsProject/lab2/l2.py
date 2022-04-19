from math import pi, exp
import numpy as np
import scipy.stats as st
from matplotlib import pyplot as plt


def gauss_kernel(x):
    g_k = lambda t: exp(-t ** 2 / 2) / (2 * pi) ** 0.5
    return (np.vectorize(g_k))(x)


def get_window(distr):
    # h = (1.06 * s_n) / n ** 0.5
    # Посчитаем корень из исправленной выборочной дисперсии:
    sample_mean = sum(distr) / distr.size
    correction = distr.size / (distr.size - 1)
    s_n = correction * sum((distr - sample_mean) ** 2) / distr.size
    return (1.06 * s_n) / distr.size ** (1 / 5)


class KernelMarker:
    def __init__(self, distr):
        self.distr = distr
        self.h = get_window(self.distr)

    # Возвращает ядерную оценку плотности
    def get_f(self, x):
        kern_sum = 0
        for el in self.distr:
            kern_sum += gauss_kernel((x - el) / self.h)
        return 1 / (self.distr.size * self.h) * kern_sum


distr_size = 200
gauss_distr = np.random.normal(size=distr_size)
for i in range(len(gauss_distr)):
    gauss_distr[i] = 9 + 14 ** 0.5 * gauss_distr[i]

gauss_marker = KernelMarker(gauss_distr)
x = np.linspace(-100, 100, 200)
# print(gauss_marker.get_f(1))
plt.plot(x, gauss_marker.get_f(x))
plt.show()

import numpy as np
import scipy.stats as st
import math


def get_gauss_quantile(q):
    return st.norm.ppf(q)


def get_chi2_quantile(q, freedom_c):
    return st.chi2.ppf(q, freedom_c)


def get_students_quantile(q, freedom_c):
    return st.t.ppf(q, freedom_c)


class Section:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.frequency = 0

    def set_frequency(self, dots: []):
        """dots should be sorted."""
        for dot in dots:
            if dot >= self.b:
                break
            if self.a <= dot < self.b:
                self.frequency += 1

    def __str__(self):
        return f"[{self.a}; {self.b}] - {self.frequency}"


dots_c = 200
gauss = np.random.normal(size=dots_c)
dispersion = 9
mean = 4
error = 0.05

for i in range(len(gauss)):
    gauss[i] = mean + dispersion ** 0.5 * gauss[i]

# Посчитаем выборочное среднее:
sample_mean = sum(gauss) / dots_c

# Посчитаем доверительный интервал для мат ожидания (с настоящим СКО, уточнить у Владимира Юрьевича):
deviation = dispersion ** 0.5 / dots_c ** 0.5 * get_gauss_quantile(1 - error / 2)
a_mean = sample_mean - deviation
b_mean = sample_mean + deviation
print("Interval for mean: [", a_mean, "; ", b_mean, "]")

# Посчитаем несмещенную выборочную дисперсию:
sample_dispersion = sum((gauss - sample_mean) ** 2) / dots_c

# Посчитаем доверительный интервал для дисперсии
counter = (dots_c - 1) * sample_dispersion
a_disp = counter / get_chi2_quantile(1 - error / 2, dots_c - 1)
b_disp = counter / get_chi2_quantile(error / 2, dots_c - 1)
print("Interval for dispersion: [", a_disp, "; ", b_disp, "]")

# Теперь будем считать оценки с группированием, для этого сделаем наш ряд вариационным и разделим на 8 частей
# Вычислим начальную и конечную точку
gauss.sort()
a_gauss = math.floor(gauss[0])
b_gauss = math.ceil(gauss[dots_c - 1])

# Найдем границы отрезков
sect_count = 8
sect_size = (b_gauss - a_gauss) / sect_count
borders = [a_gauss + i * sect_size for i in range(sect_count + 1)]

# Создадим отрезки
sections = []
for i in range(sect_count):
    sections.append(Section(borders[i], borders[i + 1]))
    sections[i].set_frequency(gauss)
print("Group sections: ")
for sect in sections:
    print(sect)

# Посчитаем выборочное среднее группированного распределения
group_mean = 0
for sect in sections:
    group_mean += (sect.a + sect.b) / 2 * sect.frequency
group_mean /= dots_c
print("Group mean: ", group_mean)

# Посчитаем неисправленную дисперсию:
group_disp = 0
for sect in sections:
    group_disp += ((sect.a + sect.b) / 2 - group_mean) ** 2 * sect.frequency
group_disp /= dots_c
print("Group dispesion: ", group_disp)

# Посчитаем исправленную дисперсию
group_corr_disp = group_disp * dots_c / (dots_c - 1)
print("Group corrected dispersion: ", group_corr_disp)

# Теперь будем считать доверительные интервалы для данного распределения, пользуясь распределением стьюдента и хи квадрат
# Найдем доверительный интервал для математического ожидания (Спросить у Владимира Юрьевича на счет квантиля здесь, какое q)
deviation = (group_corr_disp / sect_count) ** 0.5 * get_students_quantile((1 + error) / 2, sect_count - 1)
a_group_mean = group_mean - deviation
b_group_mean = group_mean + deviation
print(f"[{a_group_mean}; {b_group_mean}]")

# Найдем интервал для дисперсии (?????):
counter = (sect_count - 1) * group_corr_disp
a_group_disp = counter / get_chi2_quantile(1 - error / 2, sect_count - 1)
b_group_disp = counter / get_chi2_quantile(error / 2, sect_count - 1)
print(f"[{a_group_disp}; {b_group_disp}]")

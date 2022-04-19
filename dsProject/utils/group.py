import math


def group(dots: [], sect_count: int) -> []:
    a = math.floor(dots.min())
    b = math.ceil(dots.max())

    # Найдем границы отрезков
    sect_size = (b - a) / sect_count
    borders = [a + i * sect_size for i in range(sect_count + 1)]

    # Создадим отрезки
    sections = []
    for i in range(sect_count):
        sections.append(Section(borders[i], borders[i + 1]))
        sections[i].set_frequency(dots)

    return sections


def get_mean(sections, dots_c):
    # Посчитаем выборочное среднее группированного распределения
    group_mean = 0
    for sect in sections:
        group_mean += (sect.a + sect.b) / 2 * sect.frequency
    group_mean /= dots_c
    return group_mean


def get_dispersion(sections, dots_c):
    # Посчитаем неисправленную дисперсию:
    group_disp = 0
    group_mean = get_mean(sections, dots_c)
    for sect in sections:
        group_disp += ((sect.a + sect.b) / 2 - group_mean) ** 2 * sect.frequency
    group_disp /= dots_c
    return group_disp


def get_corr_disp(sections, dots_c):
    # Посчитаем исправленную дисперсию
    return get_dispersion(sections, dots_c) * dots_c / (dots_c - 1)


class Section:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        # Attention: Frequency is just a count of dots in this section
        self.frequency = 0
        # frequency / all dots count
        self.rel_frequency = 0

    def set_frequency(self, dots: []):
        for dot in dots:
            if self.a <= dot < self.b:
                self.frequency += 1
        self.rel_frequency = self.frequency / len(dots)

    def __str__(self):
        return f"[{self.a}; {self.b}] - Freq: {self.frequency}, Relative freq: {self.rel_frequency}"

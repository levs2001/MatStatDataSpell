import numpy as np
import scipy.stats as st

distr_size = 200
distributions = {
    "uniform": np.random.uniform(low=5, high=7, size=distr_size),
    "gauss": np.random.normal(size=distr_size),
    "poisson": np.random.poisson(lam=9, size=distr_size),
    "exponential": np.random.exponential(scale=1 / 3, size=distr_size),
    "caushy": st.cauchy.rvs(loc=0, scale=2, size=distr_size)
}

gauss = distributions["gauss"]
for i in range(len(gauss)):
    gauss[i] = 17 + 22 ** 0.5 * gauss[i]

means = {}
for distr in distributions:
    means[distr] = sum(distributions[distr]) / distr_size
print("Sample means : ", means)

medians = {}
quartile_1_4 = {}
quartile_3_4 = {}
for distr in distributions:
    vals = distributions[distr]
    vals.sort()
    quartile_1_4[distr] = (vals[distr_size // 4 - 1] + vals[distr_size // 4]) / 2
    medians[distr] = (vals[distr_size // 2 - 1] + vals[distr_size // 2]) / 2
    quartile_3_4[distr] = (vals[3 * distr_size // 4 - 1] + vals[3 * distr_size // 4]) / 2

print("Sample quartile 1/4: ", quartile_1_4)
print("Sample medians: ", medians)
print("Sample means 3/4: ", quartile_3_4)

variance = {}
for distr in distributions:
    variance[distr] = sum((distributions[distr] - means[distr]) ** 2) / distr_size
print("Sample variance: ", variance)

corr_variance = {}
correction = distr_size / (distr_size - 1)
for distr in distributions:
    corr_variance[distr] = correction * variance[distr]
print("Corrected sample variance: ", corr_variance)

assymetry = {}
for distr in distributions:
    moment_3 = sum((distributions[distr] - means[distr]) ** 3) / distr_size
    assymetry[distr] = moment_3 / (variance[distr] ** (3 / 2))
print("Assymetry factor: ", assymetry)

kurt = {}
for distr in distributions:
    moment_4 = sum((distributions[distr] - means[distr]) ** 4) / distr_size
    kurt[distr] = moment_4 / (variance[distr] ** 2) - 3
print("Kurtosis: ", kurt)

variation = {}
for distr in distributions:
    variation[distr] = (variance[distr] ** (1 / 2)) / abs(means[distr])
print("Variation factor: ", variation)

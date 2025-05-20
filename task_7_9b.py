from scipy.stats import chi2
import numpy as np

n = 100
mean = 17.29
s = 5.7932
gamma = 0.99

chi2_upper = chi2.ppf((1 - gamma)/2, df=n-1)
chi2_lower = chi2.ppf((1 + gamma)/2, df=n-1)

lower_bound = np.sqrt((n - 1) * s**2 / chi2_lower)
upper_bound = np.sqrt((n - 1) * s**2 / chi2_upper)

print(f"Доверительный интервал для σ: [{lower_bound:.2f}, {upper_bound:.2f}]")
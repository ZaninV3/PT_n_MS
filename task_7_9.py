from scipy.stats import t
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2

n = 100
mean = 17.29
s = 5.7932
gamma = 0.99

t_critical = t.ppf((1 + gamma)/2, df=n-1)
margin = t_critical * s / np.sqrt(n)

chi2_upper = chi2.ppf((1 - gamma)/2, df=n-1)
chi2_lower = chi2.ppf((1 + gamma)/2, df=n-1)

lower_bound = np.sqrt((n - 1) * s**2 / chi2_lower)
upper_bound = np.sqrt((n - 1) * s**2 / chi2_upper)

# График для μ
plt.figure(figsize=(10, 4))
plt.errorbar(1, mean, yerr=margin, fmt='o', capsize=5, label='μ (среднее)')
plt.xlim(0.5, 1.5)
plt.ylim(10, 25)
plt.title('Доверительный интервал для генеральной средней (γ=0.99)')
plt.legend()
plt.grid()
plt.xticks([])
plt.show()

# График для σ
plt.figure(figsize=(10, 4))
plt.errorbar(1, s, yerr=[[s - lower_bound], [upper_bound - s]], fmt='o', capsize=5, label='σ (СКО)')
plt.xlim(0.5, 1.5)
plt.ylim(3, 8)
plt.title('Доверительный интервал для генерального СКО (γ=0.99)')
plt.legend()
plt.grid()
plt.xticks([])
plt.show()
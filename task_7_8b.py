import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

intervals = [(2, 5), (5, 8), (8, 11), (11, 14), (14, 17), (17, 20), (20, 23), (23, 26), (26, 29), (29, 32)]
n_i = [2, 6, 3, 10, 23, 18, 23, 8, 5, 2]
n = 100
p_i = [count / n for count in n_i]  # относительные частоты

mu, sigma = 17.29, 5.7932
theoretical_p = [norm.cdf(b, mu, sigma) - norm.cdf(a, mu, sigma) for a, b in intervals]
midpoints = [(a + b)/2 for a, b in intervals]  # середины интервалов

# Гистограмма теоретических вероятностей
plt.figure(figsize=(12, 6))
plt.bar(midpoints, theoretical_p, width=2.8, alpha=0.3, color='red', label='Теоретические $p_i$')

# Кривая плотности f(x)
x = np.linspace(2, 32, 100)
f_x = norm.pdf(x, mu, sigma)
plt.plot(x, f_x, 'r-', linewidth=2, label='$f(x)$')

# Настройки графика
plt.title('Гистограмма теоретических вероятностей и плотность $f(x)$')
plt.xlabel('Значения')
plt.ylabel('Плотность')
plt.legend()
plt.grid()
plt.show()
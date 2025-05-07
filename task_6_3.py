import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Параметры распределения
a, sigma = 12, 5
gamma = 0.8064

# Нахождение границ интервала
z_critical = norm.ppf((1 + gamma) / 2)  # Квантиль для 0.9032
k = z_critical * sigma
lower, upper = a - k, a + k

# Данные для графика
x = np.linspace(a - 4*sigma, a + 4*sigma, 1000)
y = norm.pdf(x, loc=a, scale=sigma)

# Построение графика
plt.figure(figsize=(10, 5))
plt.plot(x, y, 'b-', linewidth=2, label=f'$N({a}, {sigma}^2)$')
plt.axvline(a, color='red', linestyle='--', label=f'Среднее $a = {a}$')
plt.title(f'Симметричный интервал для вероятности $\gamma = {gamma}$')
plt.xlabel('x')
plt.ylabel('Плотность вероятности')
plt.legend()
plt.grid(True)
plt.show()

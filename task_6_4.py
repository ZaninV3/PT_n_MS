import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Параметры распределения
a, sigma = 12, 5
lower, upper = a - 3*sigma, a + 3*sigma  # Правило трёх сигм

# Данные для графика
x = np.linspace(a - 4*sigma, a + 4*sigma, 1000)
y = norm.pdf(x, loc=a, scale=sigma)

# Построение графика
plt.figure(figsize=(10, 5))
plt.plot(x, y, 'b-', linewidth=2, label=f'$N({a}, {sigma}^2)$')
plt.axvline(a, color='red', linestyle='--', label=f'Среднее $a = {a}$')
plt.title('Интервал, содержащий практически все значения $X$')
plt.xlabel('x')
plt.ylabel('Плотность вероятности')
plt.legend()
plt.grid(True)
plt.show()
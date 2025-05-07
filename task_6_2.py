import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Параметры распределения
a, sigma = 12, 5
lower, upper = -10, 34

# Данные для графика (увеличим диапазон, чтобы точно охватить интервал [-10, 34])
x = np.linspace(a - 6*sigma, a + 6*sigma, 1000)  # Увеличили число точек и диапазон
y = norm.pdf(x, loc=a, scale=sigma)

# Создание графика
plt.figure(figsize=(10, 5))
plt.plot(x, y, 'b-', linewidth=2, label=f'$N({a}, {sigma}^2)$')

# Подписи и оформление
plt.title(f'Вероятность $P(|X - {a}| < 22) = P(-10 < X < 34) = 1$')
plt.xlabel('x')
plt.ylabel('Плотность вероятности')
plt.legend()
plt.grid(True)
plt.show()